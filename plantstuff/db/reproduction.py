"""Reproduction related aspects."""
from marshmallow import Schema, fields
from marshmallow import validate


class PropagationMethod(Schema):
    """The plant propagation type."""

    name = fields.Str(required=True, validate=validate.OneOf([
        "bare_root",
        "bulb",
        "corm",
        "root_division",
        "seed",
        "sod",
        "tissue_culture",
        "tuber",
        "vegetative_cutting_greenwood",
        "vegetative_cutting_hardwood",
        "vegetative_cutting_softwood",
    ]))
    recommended_months = fields.List(fields.Str(validate=validate.OneOf([
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ])))


class PropagationFactor(Schema):
    """A type of factor that increases success of a given type."""

    name = fields.Str(required=True, validate=validate.OneOf([
        "scarification",
        "stratification",
        "hormone",
    ]))
    # e.g. if hormone, value most likely would be IBA/IAA
    # for Indole-3-Butyric Acid, or Indole-Acetic Acid.
    value = fields.Float()
    # e.g. if hormone, units should be PPM
    units = fields.Str()
