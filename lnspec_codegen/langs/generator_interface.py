import pyln.proto.message
from abc import ABC, abstractmethod
from lnspec_codegen.utils import TypeField, get_filed_type


class CodeGenerator(ABC):
    @abstractmethod
    def get_primitive_cmp(self, x: str, cmp_symbol: str, y: str):
        """"""
        pass

    @abstractmethod
    def write_variable(
        self, name_var: str, value_var: str = None, type_var: str = None
    ):
        """
        Write a declaration variable in the code
        """
        pass

    @abstractmethod
    def write_increment_wire(self, field, all_fields, output_file, options):
        """
        TODO: Add doc gene
        """
        pass

    @abstractmethod
    def write_size_array_to_wire(self, field, all_fields, output_file, options):
        """TODO: add docs"""
        pass

    @abstractmethod
    def write_array_type_to_wire(self, field, all_fields, output_file, options):
        """TODO: add docs"""
        pass

    @abstractmethod
    def write_length_field_to_wire(self, field, all_fields, output_file, options):
        """TODO: add docs"""
        pass

    @abstractmethod
    def write_unknown_filed_to_wire(self, field, all_fields, output_file, options):
        pass

    @abstractmethod
    def write_preamble_filed_from_wire(
        self, field, filed_type, all_fields, output_file
    ):
        """
        Method called before the write_filed_from_wire to init the variable and
        generate all the necessary code to call the method write_filed_from_wire.

        It return a comparison string, used to read the stream of bytes, and it return
        also a string to say it the type it is an array.
        """
        pass

    @abstractmethod
    def write_filed_from_wire(
        self, field, filed_type, is_array, cmp_str, all_fields, output_file
    ):
        pass

    def generate_towire_field(self, field, all_fields, output_file, options):
        """TODO:"""
        field_type = get_filed_type(field)
        if field_type == TypeField.SIZE_ARRAY_TYPE:
            self.write_array_type_to_wire(field, all_fields, output_file, options)

        if field_type == TypeField.ARRAY_TYPE:
            self.write_array_type_to_wire(field, all_fields, output_file, options)
        elif field_type == TypeField.LENGTH_FIELD_TYPE:
            self.write_length_field_to_wire(field, all_fields, output_file, options)
        else:
            self.write_unknown_filed_to_wire(field, all_fields, output_file, options)

        self.write_increment_wire(field, all_fields, output_file, options)

    def generate_fromwire_field(self, field, all_fields, output_file, options):
        pass

    @abstractmethod
    def generate_tlv_type(self, tlv_type: "TlvMessageType", output_file, options):
        pass

    @abstractmethod
    def generate_msg_type(self, name, output_file, options):
        pass

    @abstractmethod
    def generate_subtype(self, name, output_file, options):
        pass

    def generate(self, output_file, proto_ns, types_select: list, options: dict = {}):
        """TODO: add doc
        The option filed allow to add propriety for custom generator
        or future change in the generator
        """
        for type_name in types_select:
            tlv_type = proto_ns.get_tlvtype(type_name)
            if tlv_type:
                self.generate_tlv_type(tlv_type, output_file, options)
                continue

            msg_type = proto_ns.get_msgtype(type_name)
            if msg_type:
                self.generate_msg_type(msg_type, output_file, options)
                continue

            subtype = proto_ns.get_subtype(type_name)
            if subtype:
                self.generate_subtype(subtype, output_file, options)
                continue

            raise ValueError("Unknown type {}".format(type_name))
