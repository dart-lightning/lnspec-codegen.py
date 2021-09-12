#! /usr/bin/env python3
from .generator_interface import CodeGenerator
from lnspec_codegen.utils.type_field import TypeField


class JavascriptGenerator(CodeGenerator):
    """TODO:add doc her"""

    def generate_subtype(self, name, output_file, options):
        print(
            "function towire_{tlvname}(value)\n"
            "{{\n"
            "    let _n = 0;\n"
            "    let buf = Buffer.alloc(0);".format(tlvname=name.name),
            file=output_file,
        )
        for f in name.fields:
            self.generate_towire_field(f, name.fields, output_file, options)
        print(
            "    assert(value.length == _n);\n" "    return buf;\n" "}\n",
            file=output_file,
        )
        print(
            "function fromwire_{tlvname}(buffer)\n"
            "{{\n"
            "    let _n = 0;\n"
            "    let retarr;\n"
            "    value = {{}};".format(tlvname=name.name),
            file=output_file,
        )
        for f in name.fields:
            self.generate_fromwire_field(f, name.fields, output_file, options)
        print("\n" "    return [value, buffer];\n" "}\n", file=output_file)

    def generate_msg_type(self, name, output_file, options):
        print(
            "function towire_{tlvname}(value)\n"
            "{{\n"
            "    let _n = 0;\n"
            "    let buf = Buffer.alloc(0);".format(tlvname=name.name),
            file=output_file,
        )

        for f in name.fields:
            self.generate_towire_field(f, name.fields, output_file, options)
        print(
            "    assert(value.length == _n);\n" "    return buf;\n" "}\n",
            file=output_file,
        )
        print(
            "function fromwire_{tlvname}(buffer)\n"
            "{{\n"
            "    let _n = 0;\n"
            "    let retarr;\n"
            "    value = {{}};".format(tlvname=name.name),
            file=output_file,
        )

        for f in name.fields:
            self.generate_fromwire_field(f, name.fields, output_file, options)
        print("\n" "    return [value, buffer];\n" "}\n", file=output_file)

    def generate_tlv_type(self, tlv_type: "TlvMessageType", output_file, options):
        pass

    def get_primitive_cmp(self, x: str, cmp_symbol: str, y: str):
        return "{} {} {}".format(x, cmp_symbol, y)

    def write_variable(
        self, name_var: str, value_var: str = None, type_var: str = None
    ):
        return "{} {} = {}".format(type_var, name_var, value_var)

    def write_preamble_filed_from_wire(
        self, field, filed_type, all_fields, output_file
    ):
        is_array = True
        limit_str = None
        if filed_type == TypeField.SIZE_ARRAY_TYPE:
            self.write_variable(
                "size", value_var=field.fieldtype.arraysize, type_var="const"
            )
            limit_str = self.get_primitive_cmp("i", "<", "size")
        elif filed_type == TypeField.DYNAMIC_ARRAY_TYPE:
            self.write_variable(
                "size",
                "lenfield_{}".format(field.fieldtype.lenfield.name),
                type_var="const",
            )
            limit_str = self.get_primitive_cmp("i", "<", "size")
        elif filed_type == TypeField.ELLIPSIS_ARRAY_TYPE:
            limit_str = self.get_primitive_cmp("len(buffer)", "!=", "0")
            self.write_variable("size", "len(buffer)", type_var="const")
        else:
            is_array = False
        return limit_str, is_array

    def write_filed_from_wire(
        self, field, filed_type, is_array, cmp_str, all_fields, output_file
    ):
        # limit_str, is_array = self.write_preamble_filed_from_wire(field, filed_type, all_fields, output_file)
        assert cmp_str is not None

        if is_array:
            # UTF-8 arrays are special
            if field.fieldtype.elemtype.name == "utf8":
                print(
                    "    retarr = fromwire_array_utf8(buffer, codegen_size});\n"
                    '    value["{fname}"] = retarr[0];\n'
                    "    buffer = retarr[1]".format(fname=field.name),
                    file=output_file,
                )
            else:
                print(
                    "    v = [];\n"
                    "    for (let i = 0; {limit}; i++) {{\n"
                    "        retarr = fromwire_{ftype}(buffer);\n"
                    "        v.push(retarr[0]);\n"
                    "        buffer = retarr[1];\n"
                    "    }}\n"
                    '    value["{fname}"] = v;'.format(
                        fname=field.name,
                        ftype=field.fieldtype.elemtype.name,
                        limit=cmp_str,
                    ),
                    file=output_file,
                )
        elif filed_type == TypeField.LENGTH_FIELD_TYPE:
            print(
                "    retarr = fromwire_{ftype}(buffer);\n"
                "    let lenfield_{fname} = retarr[0];\n"
                "    buffer = retarr[1];".format(
                    fname=field.name, ftype=field.fieldtype.underlying_type.name
                ),
                file=output_file,
            )
        else:
            print(
                "    retarr = fromwire_{ftype}(buffer);\n"
                '    value["{fname}"] = retarr[0];'
                "    buffer = retarr[1];".format(
                    fname=field.name, ftype=field.fieldtype.name
                ),
                file=output_file,
            )

    def write_unknown_filed_to_wire(self, field, all_fields, output_file, options):
        print(
            '    buf = Buffer.concat([buf, towire_{ftype}(value["{fname}"])]);'.format(
                fname=field.name, ftype=field.fieldtype.name
            ),
            file=output_file,
        )

    def write_length_field_to_wire(self, field, all_fields, output_file, options):
        # FIXME: Make sure that all fields which use this length are the same!
        # FIXME: length() is not correct if field is utf8!
        for f in all_fields:
            if f.name == field.fieldtype.len_for[0].name:
                assert f.fieldtype.elemtype.name != "utf8"
        print(
            '    buf = Buffer.concat([buf, towire_{ftype}(value["{lenfield}"].length)]);\n'.format(
                ftype=field.fieldtype.underlying_type.name,
                lenfield=field.fieldtype.len_for[0].name,
            ),
            file=output_file,
        )

    def write_array_type_to_wire(self, field, all_fields, output_file, options):
        # UTF-8 arrays are special
        if field.fieldtype.elemtype.name == "utf8":
            print(
                '    buf = Buffer.concat([buf, towire_array_utf8(value["{fname}"])]);\n'.format(
                    fname=field.name
                ),
                file=output_file,
            )
        else:
            print(
                '    for (let v of value["{fname}"]) {{\n'
                "        buf = Buffer.concat([buf, towire_{ftype}(v)]);\n"
                "    }}".format(fname=field.name, ftype=field.fieldtype.elemtype.name),
                file=output_file,
            )

    def write_size_array_to_wire(self, field, all_fields, output_file, options):
        # FIXME: UTF-8 arrays are special: length we want is in bytes!
        # However, only fixed-length UTF-8 array is currency, which is ASCII
        print(
            '    assert.equal(value["{fname}"].length == {fixedlen})'.format(
                fname=field.name, fixedlen=field.fieldtype.arraysize
            ),
            file=output_file,
        )

    def write_increment_wire(self, field, all_fields, output_file, options):
        print("    _n += 1", file=output_file)
