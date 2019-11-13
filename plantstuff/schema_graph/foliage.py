"""Foliage categories."""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    RelationshipTo,
)

from plantstuff.schema import common


class FoliagePhase(Model):
    """Foliage characteristic specific to a phase of its life, or season."""

    anatomy = ListProp(StringProp(
        choices={c: c for c in [
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
        ]},
    ))
    arrangement = StringProp(
        choices={c: c for c in [
            'whorled',
            'alternate',
            'spiral',
            'opposite',
        ]},
    )
    color = ListProp(StringProp())
    texture = ListProp(StringProp())
    striped = BooleanProp()
    variegated = BooleanProp()
    seasonal_phase = StringProp(choices={
        c: c for c in common.PLANT_SEASONS})
    # TODO: better choices
    life_phase = StringProp(
        choices={c: c for c in common.PLANT_LIFE_PHASES},
    )


class Foliage(Model):
    """The plant foliage type."""

    retention = StringProp(
        choices={c: c for c in [
            "brevideciduous",
            "broadleaf-evergreen",
            "deciduous",
            "evergreen",
            "herbaceous",
            "marcescence",
        ]},
    )
    phases = RelationshipTo(FoliagePhase, 'HAS_FOLIAGE_PHASE')
    porosity_summer = StringProp(choices={})
    porosity_winter = StringProp(choices={})
