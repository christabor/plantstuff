"""Soil categories and characteristics."""
from marshmallow import Schema, fields
from marshmallow import validate


class SoilType(Schema):
    """A general class of soil."""

    name = fields.Str(validators=validate.OneOf([
        # TODO: add all!
        # Or find a better way to represent this
        # with the triangle soil diagram in mind!
        "loam",
        "clay",
        "sand",
        "sandy-loam",
        "clay-loam",
    ]))
    description = fields.Str()

    # "preferred_type": "sandy-loam",
    # "adaptations": {
    #     "coarse_texture": {
    #         "type": "bool",
    #         "default": False,
    #         "nullable": True,
    #     },
    #     "medium_texture": {
    #         "type": "bool",
    #         "default": False,
    #         "nullable": True,
    #     },
    #     "fine_texture": {
    #         "type": "bool",
    #         "default": True,
    #         "nullable": True,
    #     },
    #     "anaerobic_tolerance": None,
    #     "calcareous_tolerance": None,
