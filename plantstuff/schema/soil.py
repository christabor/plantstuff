"""Soil categories and characteristics."""
from schematics.models import Model

from plantstuff.schema.types import (
    BooleanType,
    StringType,
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

    name = StringType(choices=SOIL_TYPES)
    description = StringType()
    preferred = BooleanType()
    drainage = StringType(choices=['poor', 'moderate', 'excellent'])
