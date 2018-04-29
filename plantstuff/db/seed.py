"""Seed categories and characteristics."""
from marshmallow import Schema, fields
from marshmallow import validate


class Seed(Schema):
    """Seed specific attributes."""

    abundance = fields.Str(validate=validate.OneOf([
        "low",
        "medium",
        "high"
    ]))
    persistence = fields.Bool()
    per_pound = fields.Str(validators=validate.OneOf([
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
    ]))
    small_grain = fields.Bool(default=False)
    seed_color = fields.Str(validators=validate.OneOf([
        "black",
        "blue",
        "brown",
        "green",
        "orange",
        "purple",
        "red",
        "white",
        "yellow",
    ]))

    # "seed_sprd_rate_condition": [
    #     "none",
    #     "slow",
    #     "moderate",
    #     "rapid"
    # ],
    # "frut_seed_cspc_ind" = fields.Str
    #     "type": "bool",
    # },
    # "frut_seed_end_condition" = fields.Str
    #     "type": "string",
    #     "anyof": [
    #         "spring",
    #         "summer",
    #         "fall",
    #         "winter",
    #         "year-round",
    #     ],
    # },

    # "frut_seed_start_condition": [
    #     "spring",
    #     "summer",
    #     "fall",
    #     "winter",
    #     "year-round",
    # ],

    # "color": None,
    # "conspicous": None,
    # "abundance": "low",
    # "period" = fields.Str
    #     "begin": "spring",
    #     "end": "fall",
    #     "persistence" = fields.Str
    #         "type": "bool",
    #         "default": False,
    #         "nullable": True,


class SeedDispersal(Schema):
    """Ways of seed dispersal.

    https://en.wikipedia.org/wiki/Biological_dispersal#Types_of_dispersal
    """

    type = fields.Str(validators=validate.OneOf([
        "density-independent",
        "density-dependent",
        "breeding",
        "natal",
    ]))
    spread_rate = fields.Str(validators=validate.OneOf([
        "slow",
        "fast"
    ]))
