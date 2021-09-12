#! /usr/bin/env python3
from .generator_interface import CodeGenerator
from lnspec_codegen.utils.type_field import TypeField


class PythonGenerator(CodeGenerator):
    """TODO: doc this"""

    def generate_subtype(self, name, output_file, options):
        print(
            "\n\ndef towire_{tlvname}(value):\n"
            "    _n = 0\n"
            "    buf = bytes()".format(tlvname=name.name),
            file=output_file,
        )
        for f in name.fields:
            self.generate_towire_field(f, name.fields, output_file, options)
        print("    assert len(value) == _n\n" "    return buf", file=output_file)
        print(
            "\n\ndef fromwire_{tlvname}(buffer):\n"
            "    value = {{}}".format(tlvname=name.name),
            file=output_file,
        )
        for f in name.fields:
            self.generate_fromwire_field(f, name.fields, output_file, options)
        print("\n" "    return value, buffer", file=output_file)

    def generate_msg_type(self, name, output_file, options):
        print(
            "\n\ndef towire_{tlvname}(value):\n"
            "    _n = 0\n"
            "    buf = bytes()".format(tlvname=name.name),
            file=output_file,
        )

        for f in name.fields:
            self.generate_towire_field(f, name.fields, output_file, options)
        print("    assert len(value) == _n\n" "    return buf", file=output_file)
        print(
            "\n\ndef fromwire_{tlvname}(buffer):\n"
            "    value = {{}}".format(tlvname=name.name),
            file=output_file,
        )
        for f in name.fields:
            self.generate_fromwire_field(f, name.fields, output_file, options)
        print("\n" "    return value, buffer", file=output_file)

    def generate_tlv_type(self, tlv_type: "TlvMessageType", output_file, options):
        """
        Generate the fromwire / towire routines
        """
        for f in tlv_type.fields:
            # If there's only one value, we just collapse it
            if len(f.fields) == 1:
                singleton = f.fields[0]
            else:
                singleton = None

            ## TODO add method to generate functions int he code generator
            print(
                "\n\ndef towire_{tlvname}_{fname}(value):\n"
                "    _n = 0\n"
                "    buf = bytes()".format(tlvname=tlv_type.name, fname=f.name),
                file=output_file,
            )
            # Singletons are collapsed, expand as generated code expects
            if singleton:
                print(
                    '    value = {{"{fname}": value}}'.format(fname=singleton.name),
                    file=output_file,
                )
            for sub_filed in f.fields:
                self.generate_towire_field(sub_filed, f.fields, output_file, options)
            print(
                "    # Ensures there are no extra keys!\n"
                "    assert len(value) == _n\n"
                "    return buf",
                file=output_file,
            )
            # Create a new function
            print(
                "\n\ndef fromwire_{tlvname}_{fname}(buffer):\n"
                "    value = {{}}".format(tlvname=tlv_type.name, fname=f.name),
                file=output_file,
            )
            for sub_filed in f.fields:
                self.generate_fromwire_field(sub_filed, f.fields, output_file, options)

            # Collapse singletons:
            if singleton:
                print(
                    "\n"
                    '    return value["{fname}"], buffer'.format(fname=singleton.name),
                    file=output_file,
                )
            else:
                print("\n" "    return value, buffer", file=output_file)

        # Now, generate table
        # TODO: add method in the generator to generate this table
        print("\n\ntlv_{} = {{".format(tlv_type.name), file=output_file)
        for f in tlv_type.fields:
            print(
                '    {num}: ("{fname}", towire_{tlvname}_{fname}, fromwire_{tlvname}_{fname}),'.format(
                    num=f.number, tlvname=tlv_type.name, fname=f.name
                ),
                file=output_file,
            )
        print("}", file=output_file)

    def write_preamble_filed_from_wire(
        self, field, filed_type, all_fields, output_file
    ):
        limit_str = None
        if filed_type == TypeField.SIZE_ARRAY_TYPE:
            is_array = True
            self.write_variable("size", value_var=field.fieldtype.arraysize)
            limit_str = self.get_primitive_cmp("i", "<", "size")
        elif filed_type == TypeField.DYNAMIC_ARRAY_TYPE:
            is_array = True
            self.write_variable(
                "size", "lenfield_{}".format(field.fieldtype.lenfield.name)
            )
            limit_str = self.get_primitive_cmp("i", "<", "size")
        elif filed_type == TypeField.ELLIPSIS_ARRAY_TYPE:
            is_array = True
            limit_str = self.get_primitive_cmp("len(buffer)", "!=", "0")
            self.write_variable("size", "len(buffer)")
        else:
            is_array = False
        return limit_str, is_array

    def write_variable(
        self, name_var: str, value_var: str = None, type_var: str = None
    ):
        print(f"codegen_{name_var} = {value_var}")

    def get_primitive_cmp(self, x: str, cmp_symbol: str, y: str) -> str:
        return "{} {} {}".format(x, cmp_symbol, y)

    def write_filed_from_wire(
        self, field, filed_type, is_array, cmp_str, all_fields, output_file
    ):
        # limit_str, is_array = self.write_preamble_filed_from_wire(field, filed_type, all_fields, output_file)
        assert cmp_str is not None
        if is_array:
            # UTF-8 arrays are special
            if field.fieldtype.elemtype.name == "utf8":
                print(
                    '    value["{fname}"], buffer = fromwire_array_utf8(buffer, codegen_size)'.format(
                        fname=field.name
                    ),
                    file=output_file,
                )
            else:
                print(
                    "    v = []\n"
                    "    i = 0\n"
                    "    while {limit}:\n"
                    "        val, buffer = fromwire_{ftype}(buffer)\n"
                    "        v.append(val)\n"
                    "        i += 1\n"
                    '    value["{fname}"] = v'.format(
                        fname=field.name,
                        ftype=field.fieldtype.elemtype.name,
                        limit=cmp_str,
                    ),
                    file=output_file,
                )
        elif filed_type == TypeField.LENGTH_FIELD_TYPE:
            print(
                "    lenfield_{fname} = fromwire_{ftype}(buffer)".format(
                    fname=field.name, ftype=field.fieldtype.underlying_type.name
                ),
                file=output_file,
            )
        else:
            print(
                "    val, buffer = fromwire_{ftype}(buffer)\n"
                '    value["{fname}"] = val'.format(
                    fname=field.name, ftype=field.fieldtype.name
                ),
                file=output_file,
            )

    def write_increment_wire(self, field, all_fields, output_file, options):
        print("    _n += 1", file=output_file)

    def write_size_array_to_wire(self, field, all_fields, output_file, options):
        print(
            '    assert len(value["{fname}"]) == {fixedlen}'.format(
                fname=field.name, fixedlen=field.fieldtype.arraysize
            ),
            file=output_file,
        )

    def write_array_type_to_wire(self, field, all_fields, output_file, options):
        if field.fieldtype.elemtype.name == "utf8":
            print(
                '    buf += towire_array_utf8(value["{fname}"])'.format(
                    fname=field.name
                ),
                file=output_file,
            )
        else:
            print(
                '    for v in value["{fname}"]:\n'
                "        buf += towire_{ftype}(v)".format(
                    fname=field.name, ftype=field.fieldtype.elemtype.name
                ),
                file=output_file,
            )

    def write_length_field_to_wire(self, field, all_fields, output_file, options):
        for f in all_fields:
            if f.name == field.fieldtype.len_for[0].name:
                assert f.fieldtype.elemtype.name != "utf8"
        print(
            '    buf += towire_{ftype}(len(value["{lenfield}"]))'.format(
                ftype=field.fieldtype.underlying_type.name,
                lenfield=field.fieldtype.len_for[0].name,
            ),
            file=output_file,
        )

    def write_unknown_filed_to_wire(self, field, all_fields, output_file, options):
        print(
            '    buf += towire_{ftype}(value["{fname}"])'.format(
                fname=field.name, ftype=field.fieldtype.name
            ),
            file=output_file,
        )
