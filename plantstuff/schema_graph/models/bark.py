"""Bark categories and characteristics."""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    FloatProperty as FloatProp,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)

BARK_TYPES = [
    "fibrous",
    "fissured",
    "furrowed",
    "papery",
    "plated",
    "scaly",
    "shaggy",
    "smooth",
    "warty",
]


class Bark(Model):
    """Bark of a plant."""

    # http://www.backyardnature.net/treebark.htm
    type = ListProp(StringProp(choices={b: b for b in BARK_TYPES}))
    color = StringProp()
    # Unit should be in XXX
    thickness = FloatProp()
