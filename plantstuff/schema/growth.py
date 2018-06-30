"""Foliage categories."""
from schematics.models import Model

from plantstuff.schema import common
from plantstuff.schema.types import (
    FloatType,
    StringType,
    IntType,
    ListType,
)


class GrowthProfile(Model):
    """An overall growth profile."""

    # active_growth_period
    # after_harvest_regrowth_rate
    avg_spread_foot = FloatType()
    avg_spread_foot = FloatType()
    avg_per_year_foot = FloatType()
    avg_mature_height_foot = FloatType()
    avg_height_at_base_max_foot = FloatType()
    avg_height_at_maturity_max_foot = FloatType()

    vegetative_spread_rate = StringType(choices=[
        "slow",
        "moderate",
        "rapid",
    ])

    min_frost_free_days = IntType()
    # "seedling_vigor": {
    # "anyof": [
    #     "low",
    #     "medium",
    #     "high",
    # ],
    # },
    # "water_requirements": "mostly_wet",

    growth_period_active_condition = ListType(StringType(
        choices=common.PLANT_SEASONS,
    ))
