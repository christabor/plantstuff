"""Foliage categories."""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    StringProperty as StringProp,
    IntegerProperty as IntegerProp,
    FloatProperty as FloatProp,
)

from plantstuff.schema import common


class GrowthProfile(Model):
    """An overall growth profile."""

    # active_growth_period
    # after_harvest_regrowth_rate
    avg_spread_foot = FloatProp()
    avg_spread_foot = FloatProp()
    avg_per_year_foot = FloatProp()
    avg_mature_height_foot = FloatProp()
    avg_height_at_base_max_foot = FloatProp()
    avg_height_at_maturity_max_foot = FloatProp()
    vegetative_spread_rate = StringProp(choices={c: c for c in [
        "slow",
        "moderate",
        "rapid",
    ]})
    min_frost_free_days = IntegerProp()
    seedling_vigor = StringProp(choices={c: c for c in [
        'low', 'medium', 'high',
    ]})
    # "water_requirements": "mostly_wet",
    growth_period_active_condition = ListProp(StringProp(
        choices={c: c for c in common.PLANT_SEASONS},
    ))
