"""Taxonomy, naming categories."""

from marshmallow import Schema, fields
from marshmallow import validate


class Duration(Schema):
    """The plant duration."""

    type = fields.Str(required=True, validate=validate.Onef([
        "annual",
        "biennial",
        "perennial",
        "unknown",
    ]))
