"""Plant applications."""
from schematics.models import Model

from plantstuff.schema.types import (
    StringType,
)


class Application(Model):
    """A potential commercial/industrial/other application of this plant."""

    name = StringType(choices=[
        "berry_nut_seed",
        "christmas_tree",
        "fodder",
        "lumber",
        "naval_store_product",
        "nursery_stock_product",
        "palatable_browse_animal",
        "palatable_animal_grazing",
        "post_product",
        "pulpwood_product",
        "veneer_product",
    ], required=True)


class ApplicationRange(Model):
    """A potential commercial/industrial/other application of this plant.

    Differentiated for applications that have a standard range of values.
    """

    name = StringType(choices=[
        "carbon_sequestration",
        "fuelwood",
        "protein_potential_condition",
    ], required=True)
    value = StringType(choices=["low", "medium", "high"])
