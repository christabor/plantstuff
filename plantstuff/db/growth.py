"""Foliage categories."""
from marshmallow import Schema, fields
from marshmallow import validate


class GrowthProfile(Schema):
    vegetate_spread_rate = [
        "slow",
        "moderate",
        "rapid"
    ]


class GrowthCharacteristic(Schema):
    """A growth characteristic that is not isolated to one specific area."""


"active_growth_period
"after_harvest_regrowth_rate


"growth": {
    "avg_root_depth": "2ft",
    "avg_spread": "3ft",
    "avg_landscape_size": "Fast grower to 24 to 36 in.",
    "avg_per_year": "2ft",
},
"height": {
    "avg": "5in",
    "at_base_max": {
        "type": "float",
        "default": 0.0,
    },
    "at_maturity_range": {
        "type": "string",
        "anyof": [
            "0-0.9",
            "1-1.9",
            "2-2.9",
            "3-3.9",
            "4-5.9",
            "6-9.9",
            "10-19.9",
            "20-39.9",
            "40-59.9",
            "60-99.9",
            "100-149.9",
            "150-199.9",
            "200-250",
        ],
    },
},

# "lifespan": "moderate",

GROWTH_REQUIREMENTS = {
    "aspect_hours": {
        "type": "float",
        "min": 0.0,
    },
    "aspect": "sun/half-shade",
    "moisture_use": "medium", "planting_density_per_acre
    "seedling_vigor": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high",
        ],
    },
    "water_requirements": "mostly_wet",
    "drainage": "well-drained",
    "root": {
        "depth": {
            "type": "string",
            "anyof": ROOT_DEPTH_MIN_RANGE,
        },
        "primary_type": "taproot",
    }
}
