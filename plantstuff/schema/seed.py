"""Seed categories and characteristics."""

from schematics.models import Model

from plantstuff.schema.types import (
    ListType,
    BooleanType,
    ModelType,
    StringType,
)


class SeedDispersal(Model):
    """Ways of seed dispersal.

    https://en.wikipedia.org/wiki/Biological_dispersal#Types_of_dispersal
    """

    type = StringType(choices=[
        "density-independent",
        "density-dependent",
        "breeding",
        "natal",
    ])
    spread_rate = StringType(choices=[
        "slow",
        "fast"
    ])


class Seed(Model):
    """Seed specific attributes."""

    abundance = StringType(choices=[
        "low",
        "medium",
        "high"
    ])
    persistence = BooleanType()
    small_grain = BooleanType(default=False)
    per_pound = StringType(choices=[
        "10-99999",
        "100000-199999",
        "200000-299999",
        "300000-399999",
        "400000-499999",
        "500000-999999",
        "1000000-1499999",
        "1500000-9999999",
        "10000000-19999999",
        "20000000-29999999",
        "30000000-39999999",
        "40000000-49999999",
    ])
    color = StringType(choices=[
        "black",
        "blue",
        "brown",
        "green",
        "orange",
        "purple",
        "red",
        "white",
        "yellow",
    ])
    spread_rate = StringType(choices=[
        "none",
        "slow",
        "moderate",
        "rapid"
    ])
    # "fruit_cspc_ind" = Unicode
    #     "type": "bool",
    # },
    # "fruit_start_condition": [
    #     "spring",
    #     "summer",
    #     "fall",
    #     "winter",
    #     "year-round",
    # ],
    # "fruit_end_condition" = Unicode
    #     "type": "string",
    #     "anyof": [
    #         "spring",
    #         "summer",
    #         "fall",
    #         "winter",
    #         "year-round",
    #     ],
    # },
    # "color": None,
    # "conspicous": None,
    # "abundance": "low",
    # "period" = Unicode
    #     "begin": "spring",
    #     "end": "fall",
    #     "persistence" = Unicode
    #         "type": "bool",
    #         "default": False,
    #         "nullable": True,

    dispersion = ListType(ModelType(SeedDispersal))
