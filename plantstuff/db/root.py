"""Foliage categories."""
from marshmallow import Schema, fields
from marshmallow import validate


ROOT_DEPTH_MIN_RANGE = [
    "1-2",
    "3-5",
    "6-8",
    "9-11",
    "12-14",
    "15-17",
    "18-20",
    "21-23",
    "24-26",
    "27-29",
    "30-32",
    "33-35",
    "36-38",
    "39-41",
    "42-44",
    "45-47",
    "48-51",
    "52-120",
]


class Root(Schema):
    """General root characteristics."""

    avg_depth_inches = fields.Int()
    is_taproot = fields.Bool()
    dominant_root_type = fields.Str(
        required=True,
        # TODO: better options.
        validate=validate.OneOf([
            "wide",
            "shallow",
            "fibrous",
        ]),
    )
