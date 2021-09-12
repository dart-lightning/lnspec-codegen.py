import pyln.proto.message

from enum import Enum


class TypeField(Enum):
    SIZE_ARRAY_TYPE = 0
    ARRAY_TYPE = 1
    LENGTH_FIELD_TYPE = 2
    DYNAMIC_ARRAY_TYPE = 3
    UNKNOWN_TYPE = 4
    ELLIPSIS_ARRAY_TYPE = 5


def get_filed_type(field) -> TypeField:
    """
    Check the instance and return the filed type.

    field: TODO doc it
    return: TODO dock it
    """
    if isinstance(field.fieldtype, pyln.proto.message.SizedArrayType):
        return TypeField.SIZE_ARRAY_TYPE
    if isinstance(field.fieldtype, pyln.proto.message.array_types.ArrayType):
        return TypeField.ARRAY_TYPE
    elif isinstance(field.fieldtype, pyln.proto.message.array_types.LengthFieldType):
        return TypeField.LENGTH_FIELD_TYPE
    elif isinstance(field.fieldtype, pyln.proto.message.DynamicArrayType):
        return TypeField.DYNAMIC_ARRAY_TYPE
    elif isinstance(field.fieldtype, pyln.proto.message.EllipsisArrayType):
        return TypeField.ELLIPSIS_ARRAY_TYPE
    else:
        return TypeField.UNKNOWN_TYPE
