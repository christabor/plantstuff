"""Foliage categories."""
from schematics.models import Model

from plantstuff.schema.types import (
    ListType,
    ModelType,
    BooleanType,
    StringType,
)
from plantstuff.schema import common


class FoliagePhase(Model):
    """Foliage characteristic specific to a phase of its life, or season."""

    anatomy = ListType(StringType(
        choices=[
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
        ],
    ))
    arrangement = StringType(
        choices=[
            'whorled',
            'alternate',
            'spiral',
            'opposite',
        ],
    )
    color = ListType(StringType())
    texture = ListType(StringType())
    striped = BooleanType()
    variegated = BooleanType()
    seasonal_phase = StringType(choices=common.PLANT_SEASONS)
    # TODO: better choices
    life_phase = StringType(
        choices=common.PLANT_LIFE_PHASES,
    )


class Foliage(Model):
    """The plant foliage type."""

    retention = StringType(
        choices=[
            "brevideciduous",
            "deciduous",
            "evergreen",
            "broadleaf-evergreen",
            "marcescence"
        ],
    )
    phases = ListType(ModelType(FoliagePhase))
    porosity_summer = StringType(choices=[])
    porosity_winter = StringType(choices=[])
