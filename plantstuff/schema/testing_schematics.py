from pprint import pprint as ppr

from plantstuff.schema.plant import Plant


data_example = {
    "name": "african daisy",
    "scientific_name": "gazania krebsiana",
    "growth_habit": ["subshrub"],
    "growth_habit_condition": ["bunch"],
    "duration": [
        {"type": "perennial"},
    ],
    "light": [
        {"aspect": "moderate-sun"},
        {"aspect": "full-sun"},
    ],
    "foliage": {
        "retention": "herbaceous",
        "phases": [
            {
                "anatomy": ["ovate", "linear"],
                "arrangement": "whorled",
                "color": ["red"],
                "texture": ["variegated"],
                "striped": False,
                "seasonal_phase": "spring",
                "life_phase": "young"
            },
            {
                "anatomy": ["ovate", "linear"],
                "arrangement": "whorled",
                "color": ["green"],
                "texture": ["variegated"],
                "striped": False,
                "seasonal_phase": "summer",
                "life_phase": "young"
            }
        ]
    },
    "hierarchy": {
        "kingdom": "plantae",
        "subkingdom": "tracheobionta",
        "order": "asterales",
        "family": "asteraceae",
        "genus": "aster",
    },
    "root": {
        "avg_depth_inches": 1.23,
        "is_taproot": False,
        "dominant_root_type": "wide",
        "accumulates": [
            {"name": "phosphorous", "ppm": 100},
            {"name": "nitrogen", "ppm": 100},
        ]
    },
    "bark": {
        "type": ["scaly", "papery"]
    },
    "flower": {
    },
    "tags": ['scented', 'interesting', 'colorful', 'trumpet'],
    "propagation_factors": [
        {"name": "hormone_iba", "value": 100, "units": "ppm"},
        {"name": "hormone_naa", "value": 100, "units": "ppm"},
        {"name": "stratification", "value": None, "units": None},
    ],
    "cultivars": [
        "Hantamberg Orange",
    ],
    # "growth_profile": {
    #     "vegetate_spread_rate": "medium"
    # },
    "companions": [
        "festuca glauca",
        "salvia",
        "sedum",
        "rudbeckia",
        "gaillardia",
    ],
    "propagation_methods": [
        {
            "name": "vegetative_cutting_greenwood",
            "recommended_months": [
                "april", "may", "june", "july", "august"
            ]
        },
        {
            "name": "vegetative_cutting_softwood",
            "recommended_months": [
                "july", "august", "september"
            ]
        },
    ],
}


forsythia = Plant(data_example)
forsythia.validate()

ppr(forsythia.to_primitive())
