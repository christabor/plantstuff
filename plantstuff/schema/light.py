"""Light categories and characteristics."""
from schematics.models import Model

from plantstuff.schema.types import (
    FloatType,
    StringType,
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

    aspect = StringType(choices=LIGHT_ASPECTS)
    hours_per_day = FloatType()
