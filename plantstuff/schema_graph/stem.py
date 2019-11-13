"""Stem categories."""
from neomodel import (
    StructuredNode as Model,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)


class Stem(Model):
    """The stem morphology."""
