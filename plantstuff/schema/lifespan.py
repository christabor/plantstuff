"""Taxonomy, naming categories."""
from schematics.models import Model

from plantstuff.schema.types import (
    StringType,
)


class Duration(Model):
    """The plant duration."""

    type = StringType(choices=[
        "annual",
        "biennial",
        "perennial",
        "unknown",
    ], required=True)
