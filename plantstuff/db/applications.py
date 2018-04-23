"""Plant applications."""
from marshmallow import Schema, fields
from marshmallow import validate


class Application(Schema):
    """A potential commercial/industrial/other application of this plant."""

    name = fields.Str(required=True, validate=validate.OneOf([
        "berry_nut_seed",
        "christmas_tree",
        "fodder",
        "lumber",
        "naval_store_product",
        "nursery_stock_product",
        "palatable_browse_animal",
        "post_product",
        "pulpwood_product",
        "veneer_product",
    ]))
    value = fields.Bool()


class ApplicationRange(Schema):
    """A potential commercial/industrial/other application of this plant.

    Differentiated for applications that have a standard range of values.
    """

    name = fields.Str(required=True, validate=validate.OneOf([
        "carbon_sequestration",
        "fuelwood",
        "protein_potential_condition",
    ]))
    value = fields.Str(validate=validate.OneOf(["low", "medium", "high"]))
