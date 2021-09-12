#! /usr/bin/env python3
from .generator_interface import CodeGenerator


class DartGenerator(CodeGenerator):
    """Generator of from ln spec to dart code"""

    def generate_msg_type(self, name, output_file, options):
        pass

    def generate_subtype(self, name, output_file, options):
        pass

    def get_primitive_cmp(self, x: str, cmp_symbol: str, y: str):
        pass

    def write_variable(
        self, name_var: str, value_var: str = None, type_var: str = None
    ):
        pass

    def write_preamble_filed_from_wire(
        self, field, filed_type, all_fields, output_file
    ):
        pass

    def write_filed_from_wire(
        self, field, filed_type, is_array, cmp_str, all_fields, output_file
    ):
        pass

    def generate_tlv_type(self, tlv_type: "TlvMessageType", output_file, options):
        pass

    def write_increment_wire(self, field, all_fields, output_file, options):
        pass

    def write_size_array_to_wire(self, field, all_fields, output_file, options):
        pass

    def write_array_type_to_wire(self, field, all_fields, output_file, options):
        pass

    def write_length_field_to_wire(self, field, all_fields, output_file, options):
        pass

    def write_unknown_filed_to_wire(self, field, all_fields, output_file, options):
        pass
