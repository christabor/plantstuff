"""Common field types."""

from schematics.types import (
    StringType as BaseStringType,
    ListType as BaseListType,
    FloatType as BaseFloatType,
    BooleanType as BaseBooleanType,
    ModelType as BaseModelType,
    IntType as BaseIntType,
)


class BaseType(object):
    """Subclass that allows field agnostic metadata."""

    _sources = []
    _type = None


class StringType(BaseType, BaseStringType):
    """A wrapper subclass."""

    _type = str


class FloatType(BaseType, BaseFloatType):
    """A wrapper subclass."""

    _type = float


class BooleanType(BaseType, BaseBooleanType):
    """A wrapper subclass."""

    _type = bool


class ModelType(BaseType, BaseModelType):
    """A wrapper subclass."""

    _type = object


class ListType(BaseType, BaseListType):
    """A wrapper subclass."""

    _type = list


class IntType(BaseType, BaseIntType):
    """A wrapper subclass."""

    _type = int
