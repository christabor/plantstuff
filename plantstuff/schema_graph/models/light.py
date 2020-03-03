"""Light categories and characteristics."""
from neomodel import (
    StructuredNode as Model,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    FloatProperty as FloatProp,
    RelationshipTo,
    RelationshipFrom,
)

LIGHT_ASPECTS = [
    "full-sun",
    "moderate-sun",
    "partial-shade",
    "dappled-shade",
    "deep-shade",
]


class Light(Model):
    """A general class for photosynthetic light requirements."""

    aspect = StringProp(choices={c: c for c in LIGHT_ASPECTS})
    hours_per_day = FloatProp()
