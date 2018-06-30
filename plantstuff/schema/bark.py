"""Bark categories and characteristics."""
from schematics.models import Model

from plantstuff.schema.types import (
    ListType,
    StringType,
    FloatType,
)


class Bark(Model):
    """Bark of a plant."""

    # http://www.backyardnature.net/treebark.htm
    type = ListType(StringType(choices=[
        "fibrous",
        "fissured",
        "furrowed",
        "papery",
        "plated",
        "scaly",
        "shaggy",
        "smooth",
        "warty",
    ]))
    color = StringType()
    # Unit should be in XXX
    thickness = FloatType()
