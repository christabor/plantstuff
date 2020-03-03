"""Plant applications."""
from neomodel import (
    StructuredNode as Model,
    StringProperty as StringProp,
)


class Application(Model):
    """A potential commercial/industrial/other application of this plant."""

    name = StringProp(choices={c: c for c in [
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
    ]}, required=True)


class ApplicationRange(Model):
    """A potential commercial/industrial/other application of this plant.

    Differentiated for applications that have a standard range of values.
    """

    name = StringProp(choices={c: c for c in [
        "carbon_sequestration",
        "fuelwood",
        "protein_potential_condition",
    ]}, required=True)
    value = StringProp(choices={c: c for c in ["low", "medium", "high"]})
