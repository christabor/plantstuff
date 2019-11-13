"""Taxonomy, naming categories."""
from neomodel import (
    StructuredNode as Model,
    StringProperty as StringProp,
)


class Duration(Model):
    """The plant duration."""

    type = StringProp(choices={c: c for c in [
        "annual",
        "biennial",
        "perennial",
        "unknown",
    ]}, required=True)
