"""Soil categories and characteristics."""
from neomodel import (
    StructuredNode as Model,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)

SOIL_TYPES = [
    # TODO: add all!
    # Or find a better way to represent this
    # with the triangle soil diagram in mind!
    "loam",
    "clay",
    "sand",
    "sandy-loam",
    "clay-loam",
]


class SoilType(Model):
    """A general class of soil."""

    name = StringProp(choices={s: s for s in SOIL_TYPES})
    description = StringProp()
    is_preferred = BooleanProp()
    drainage = StringProp(choices={
        d: d for d in ['poor', 'moderate', 'excellent']
    })
