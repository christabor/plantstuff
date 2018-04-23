"""Foliage categories."""
from marshmallow import Schema, fields
from marshmallow import validate

FOLIAGE_TYPES = [
    "brevideciduous",
    "deciduous",
    "evergreen",
    "broadleaf-evergreen",
    "marcescence"
]
FOLIAGE_ARRANGEMENT_TYPES = [
    'whorled',
    'alternate',
    'spiral',
    'opposite',
]
FOLIAGE_MORPHOLOGY_TYPES = [
    # Simple
    "ovate",
    "linear",
    "peltate",
    "hastate",
    "cordate",
    "reniform",
    "orbiculate",
    "spatulate",
    "lanceolate",
    "undulate",
    "sinuate",
    "serrate",
    "dentate",
    "lobate",
    "scalloped",
    "palmate",
    "digitate",
    "palmapartite",
    "pinnapartite",
    "pinnatifid",
    # Compound-pinnate
    "unipinnate",
    "geminate-pinnate",
    "tetrapinnate",
    "tripinnate",
    "bipinnate",
    "paripinnate",
    "imparipinnate",
    "alternipinnate",
    "pinnately-lobed",
    "pinnately-cleft",
    "pinnately-cleft",
    "pinnately-divided",
    "pinnately-trifoliate",
    "palmately-trifoliate",
    "biternate",
    "palmatisect",
    "palmatibolate",
    "pedate",
    "bipartite",
    "tripartite",
    "bipinnatisect",
    "tripinnatisect",
    "pinnatisect",
]


class Foliage(Schema):
    """The plant foliage type."""

    type = fields.Str(validate=validate.OneOf(FOLIAGE_TYPES))
    anatomy = fields.List(fields.Str(
        validate=validate.OneOf(FOLIAGE_MORPHOLOGY_TYPES)
    ))
    arrangement = fields.Str(
        validate=validate.OneOf(FOLIAGE_ARRANGEMENT_TYPES))
    color = fields.List(fields.Str)
    texture = fields.List(fields.Str)
    striped = fields.Bool(fields.Str)
    variegated = fields.Bool(fields.Str)

    porosity_summer = fields.Str()
    porosity_winter = fields.Str()
