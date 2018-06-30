"""Common field types."""

from schematics.types import (
    StringType as BaseStringType,
    ListType as BaseListType,
    FloatType as BaseFloatType,
    BooleanType as BaseBooleanType,
    ModelType as BaseModelType,
)


class BaseType(object):
    """Subclass that allows field agnostic metadata."""

    _sources = []


class StringType(BaseType, BaseStringType):
    """A wrapper subclass."""


class FloatType(BaseType, BaseFloatType):
    """A wrapper subclass."""


class BooleanType(BaseType, BaseBooleanType):
    """A wrapper subclass."""


class ModelType(BaseType, BaseModelType):
    """A wrapper subclass."""


class ListType(BaseType, BaseListType):
    """A wrapper subclass."""
