"""Schema proposal.

# TODO: https://en.wikipedia.org/wiki/Glossary_of_botanical_terms
# https://en.wikipedia.org/wiki/Dehiscence_(botany)
# All of that would be supremely useful.

Ways to organize information:

1. Giant document
    - nested
    - flat

2. Tables based on fully normalized traditional SQL design
    (1st, 2nd, 3rd normal form).

3. Tables with core information, then join tables with an medium level of
    denormalization to make queries simpler.

    e.g. categories like:

    - botany
    - landscaping
    - horticulture
    - genetics
    - etc


https://plants.usda.gov/charinfo.html
"""

from collections import namedtuple

from marshmallow import Schema, fields

from marshmallow import validate
from plantstuff.db import foliage, locales, taxonomy


class Plant(Schema):
    """The most generalized plant object."""

    name = fields.Str(required=True)
    scientific_name = fields.Str()
    national_common_name = fields.Str()
    common_aliases = fields.List(fields.Str)
    foliage_color = fields.Str()
    base_growth_form = fields.Str(validate=validate.OneOf([
        "climbing",
        "columnar",
        "conical",
        "decumbent",
        "erect",
        "irregular",
        "oval",
        "prostrate",
        "rounded",
        "semi-erect",
        "vase",
    ]))
    usda_zone = fields.List(fields.Str, validate=validate.OneOf([
        "1a", "1b",
        "2a", "2b",
        "3a", "3b",
        "4a", "4b",
        "5a", "5b",
        "6a", "6b",
        "7a", "7b",
        "8a", "8b",
        "9a", "9b",
        "10a", "10b",
        "11a", "11b",
        "12a", "12b",
        "13a", "13b",
    ]))
    sunset_zone = fields.List(fields.Str, validate=validate.OneOf([]))


class Tolerance(Schema):
    """A plant tolerance type."""

    name = fields.Str(required=True)
    unit = fields.Str(required=True)
    min_range = fields.Float(required=True)
    max_range = fields.Float(required=True)


class Tag(Schema):
    """A plant descriptor tag."""

    name = fields.Str(required=True)


class Bark(Schema):
    """Bark of a plant."""

    # http://www.backyardnature.net/treebark.htm
    type = fields.List(fields.Str(validate=validate.OneOf([
        "smooth",
        "scaly",
        "plated",
        "warty",
        "shaggy",
        "papery",
        "furrowed",
        "fibrous",
    ])))
    color = fields.Str()
    # Unit should be in XXX
    thickness = fields.Float()


SOIL_PH_TOLERANCE_MAX_RANGE = [
    "3.5-3.6",
    "3.7-3.8",
    "3.9-4",
    "4.1-4.2",
    "4.3-4.4",
    "4.5-4.6",
    "4.7-4.8",
    "4.9-5",
    "5.1-5.2",
    "5.3-5.4",
    "5.5-5.6",
    "5.7-5.8",
    "5.9-6",
    "6.1-6.2",
    "6.3-6.4",
    "6.5-6.6",
    "6.7-6.8",
    "6.9-7",
    "7.1-7.2",
    "7.3-7.4",
    "7.5-7.6",
    "7.7-7.8",
    "7.9-8",
    "8.1-8.2",
    "8.3-8.4",
    "8.5-8.6",
    "8.7-8.8",
    "8.9-9",
    "9.1-9.2",
    "9.3-9.4",
    "9.5-9.6",
    "9.7-9.8",
    "9.9-10",
    "10.1"
]

# Precipitation
PRECIPATION_TOLERANCE_MAX_RANGE = [
    "10-14",
    "15-19",
    "20-24",
    "25-29",
    "30-39",
    "40-49",
    "50-59",
    "60-79",
    "80-99",
    "100-149",
    "150-199",
    ">=200"
]
PRECIPATION_TOLERANCE_MIN_RANGE = [
    "0-4",
    "5-9",
    "10-14",
    "15-19",
    "20-24",
    "25-29",
    "30-39",
    "40-49",
    "50-59",
    ">=60"
]
ROOT_DEPTH_MIN_RANGE = [
    "1-2",
    "3-5",
    "6-8",
    "9-11",
    "12-14",
    "15-17",
    "18-20",
    "21-23",
    "24-26",
    "27-29",
    "30-32",
    "33-35",
    "36-38",
    "39-41",
    "42-44",
    "45-47",
    "48-51",
    "52-120",
]
# TODO: better classify.
MISC = {
    "palatable_animl_brs_condition": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high",
        ],
    },
    "synonyms": [
        "accepted names and synonyms",
        "accepted names only",
    ],
    "soil_adp_c_txt_ind": {
        "type": "bool",
    },
    "post_suit_ind": {
        "type": "bool",
    },
    "plantguide_ind": [
        "only with plant guides",
        "only without plant guides",
    ],
    "slin_tolerance_condition": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high",
        ]
    },
    "family_sym": taxonomy.FAMILY_SYMBOLS,
    "vs_comm_avail": [
        "no known source",
        "routinely available",
        "contracting only",
        "field collections only"
    ],
    "nurs_stk_suit_ind": {
        "type": "bool",
    },
    "epithet_rank": {
        "type": "string",
        "anyof": [
            "only genus epithet",
            "only species epithet",
            "only subspecies epithet",
            "only variety epithet",
            "only subvariety epithet",
            "only forma epithet"
        ],
    },
    "propagation_sprig_ind": {
        "type": "bool",
    },
    "temp_tolerance_min_range": [
        "-75--53",
        "-52--48",
        "-47--43",
        "-42--38",
        "-37--33",
        "-32--28",
        "-27--23",
        "-22--18",
        "-17--13",
        "-12--8",
        "-7--3",
        "-2-2",
        "3-7",
        "8-12",
        "13-17",
        "18-22",
        "23-27",
        "28-32",
        "33-37",
        "38-42",
        "43-47",
        "48-52",
        "53-57",
        "58-62",
        "63-67",
        "68-71",
        "72-75"
    ],
    "drght_tolerance_condition": [
        "none",
        "low",
        "medium",
        "high"
    ],
    "author_ranks": [
        "only genus author",
        "only species author",
        "only subspecies author",
        "only variety author",
        "only subvariety author",
        "only forma author"
    ],
    "flwr_cspc_ind": {
        "type": "bool",
    },
    "plywd_vnr_suit_ind": {
        "type": "bool",
    },
    "frut_seed_abund_condition": {
        "type": "string",
        "allof": [
            "none",
            "low",
            "medium",
            "high"
        ]
    },
    "foddr_suit_ind": {
        "type": "bool",
    },
    "state_te_status": {
        "type": "string",
        "anyof": [
            "with state status",
            "--arizona",
            "--arkansas",
            "--california",
            "--connecticut",
            "--florida",
            "--georgia",
            "--illinois",
            "--indiana",
            "--iowa",
            "--kentucky",
            "--maine",
            "--maryland",
            "--massachusetts",
            "--michigan",
            "--minnesota",
            "--missouri",
            "--nebraska",
            "--nevada",
            "--new hampshire",
            "--new jersey",
            "--new mexico",
            "--new york",
            "--north carolina",
            "--ohio",
            "--oregon",
            "--pennsylvania",
            "--puerto rico",
            "--rhode island",
            "--tennessee",
            "--texas",
            "--vermont",
            "--virginia",
            "--washington",
            "--wisconsin",
            "without state status"
        ],
    },
    "propagation_sod_ind": {
        "type": "bool",
    },
    "frut_seed_prst_ind": {
        "type": "bool",
    },
    "veg_sprd_rate_condition": {
        "type": "string",
        "anyof": [
            "none",
            "slow",
            "moderate",
            "rapid",
        ],
    },
    "fert_rqmt_condition": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high",
        ],
    },
    "lfspn_condition": {
        "type": "string",
        "anyof": [
            "short",
            "moderate",
            "long"
        ],
    },
    "cold_strat_ind": {
        "type": "bool",
    },
    "soil_adp_m_txt_ind": {
        "type": "bool",
    },
    "bloat_pot_condition": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high"
        ],
    },
    "palatable_human_ind": {
        "type": "bool",
    },
    "propagation_ctnr_ind": {
        "type": "bool",
    },
    "growth_habit_condition": {
        "type": "string",
        "anyof": [
            "bunch",
            "colonizing",
            "multiple stem",
            "rhizomatous",
            "single crown",
            "single stem",
            "stoloniferous",
            "thicket forming",
        ],
    },
    "fire_tolerance_condition": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high"
        ],
    },
    "navl_stor_suit_ind": {
        "type": "bool",
    },
    "growth_habit": {
        "type": "string",
        "anyof": [
            "forb/herb",
            "graminoid",
            "lichenous",
            "nonvascular",
            "shrub",
            "subshrub",
            "tree",
            "vine",
        ],
    },
    "moist_use_condition": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high"
        ],
    },
    "anerb_tolerance_condition": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high"
        ],
    },
    "family": {
        "type": "string",
        "anyof": taxonomy.FAMILY,
    },
    "hybrids": [
        "only hybrids",
        "only non-hybrids",
    ],
    "folg_txt_condition": {
        "type": "string",
        "anyof": [
            "fine",
            "medium",
            "coarse",
        ],
    },
    "leaf_retnt_ind": {
        "type": "bool",
    },
    "fed_te_status": [
        "with federal status",
        "--endangered",
        "--threatened",
        "without federal status"
    ],
    "soil_adp_f_txt_ind": {
        "type": "bool",
    },
    "plantfact_ind": [
        "only with fact sheets",
        "only without fact sheets",
    ],
    "grass_low_grw_ind": {
        "type": "bool",
    },
    "pfa": [
        "plants floristic area",
        "--north america",
        "\u00a0\u00a0--lower 48 u.s. states",
        "\u00a0\u00a0--alaska",
        "\u00a0\u00a0--canada",
        "\u00a0\u00a0--greenland (denmark)",
        "\u00a0\u00a0--st. pierre and miquelon (france)",
        "--hawaii",
        "--puerto rico",
        "--virgin islands",
        "not in plants floristic area"
    ],
    "coppice_pot_ind": [
        "yes",
        "no"
    ],
    "sm_grain_ind": [
        "yes",
        "no"
    ],
    "statefips": [
        "u.s. states",
        "--alabama",
        "--alaska",
        "--arizona",
        "--arkansas",
        "--california",
        "--colorado",
        "--connecticut",
        "--delaware",
        "--district of columbia",
        "--florida",
        "--georgia",
        "--hawaii",
        "--idaho",
        "--illinois",
        "--indiana",
        "--iowa",
        "--kansas",
        "--kentucky",
        "--louisiana",
        "--maine",
        "--maryland",
        "--massachusetts",
        "--michigan",
        "--minnesota",
        "--mississippi",
        "--missouri",
        "--montana",
        "--nebraska",
        "--nevada",
        "--new hampshire",
        "--new jersey",
        "--new mexico",
        "--new york",
        "--north carolina",
        "--north dakota",
        "--ohio",
        "--oklahoma",
        "--oregon",
        "--pennsylvania",
        "--rhode island",
        "--south carolina",
        "--south-dakota",
        "--tennessee",
        "--texas",
        "--utah",
        "--vermont",
        "--virginia",
        "--washington",
        "--west-virginia",
        "--wisconsin",
        "--wyoming",
        "u.s. territories and protectorates",
        "--puerto rico",
        "--virgin islands",
        "canada",
        "--alberta",
        "--british columbia",
        "--manitoba",
        "--new brunswick",
        "--newfoundland and labrador",
        "\u00a0\u00a0--labrador",
        "\u00a0\u00a0--newfoundland",
        "--northwest territories",
        "--nova scotia",
        "--nunavut",
        "--ontario",
        "--prince edward island",
        "--qu\u00e9bec",
        "--saskatchewan",
        "--yukon",
        "denmark",
        "--greenland",
        "france",
        "--st. pierre and miquelon",
    ],
    "image_ind": [
        "only with images",
        "--only with photos",
        "--only with drawings",
        "only without images",
    ],
    "alepth_ind": {
        "type": "bool",
    },
    "plant_den_low_range": [
        "10-299",
        "300-549",
        "550-799",
        "800-1299",
        "1300-1799",
        "1800-2999",
        "3000-3999",
        "4000-4999",
        "5000-12999",
        "13000-22999",
        "23000-32999",
        "33000-44000"
    ],
    "n_fix_pot_condition": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high"
        ]
    },
    "plant_den_high_range": {
        "type": "string",
        "anyof": [
            "50-499",
            "500-999",
            "1000-1499",
            "1500-2499",
            "2500-3499",
            "3500-4499",
            "4500-5499",
            "5500-10499",
            "10500-18999",
            "19000-71999",
            "72000-125000"
        ]
    },
    "frut_seed_color_condition": [
        "black",
        "blue",
        "brown",
        "green",
        "orange",
        "purple",
        "red",
        "white",
        "yellow"
    ],
    "seed_sprd_rate_condition": [
        "none",
        "slow",
        "moderate",
        "rapid"
    ],
    "frut_seed_cspc_ind": {
        "type": "bool",
    },
    "fall_cspc_ind": {
        "type": "bool",
    },
    "frut_seed_end_condition": {
        "type": "string",
        "anyof": [
            "spring",
            "summer",
            "fall",
            "winter",
            "year-round",
        ],
    },
    "invasive_pubs": [
        "with invasive status",
        "--cal-ipc-exotic pest plant list",
        "--fleppc-invasive plant list",
        "--hear-information index for selected alien plants in hawaii",
        "--ky-weeds of kentucky and adjacent states: a field guide",
        "--n'east-weeds of the northeast",
        "--ne&gp-weeds of nebraska and the great plains",
        "--seeppc-invasive exotic pest plants in tennessee",
        "--state-state noxious weed lists for 35 states",
        "--swss-weeds of the united states and canada",
        "--us-federal noxious weed list",
        "--wi-wisconsin manual of control recommendations for ecologically invasive plants",
        "--wsws-weeds of the west",
        "without invasive status",
    ],
    "plantchar_ind": [
        "only with characteristics data",
        "only without characteristics data",
    ],
    "caco3_tolerance_condition": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high",
        ],
    },
    "soil_ph_tolerance_min_range": [
        "3.5-3.6",
        "3.7-3.8",
        "3.9-4",
        "4.1-4.2",
        "4.3-4.4",
        "4.5-4.6",
        "4.7-4.8",
        "4.9-5",
        "5.1-5.2",
        "5.3-5.4",
        "5.5-5.6",
        "5.7-5.8",
        "5.9-6",
        "6.1-6.2",
        "6.3-6.4",
        "6.5-6.6",
        "6.7-6.8",
        "6.9-7",
        "7.1-7.2",
        "7.3-7.4",
        "7.5-7.6",
        "7.7-7.8",
        "7.9-8",
        "8.1-8.2",
        "8.3-8.4",
        "8.5-8.6",
        "8.7-8.8",
        "8.9-9",
        "9.1-9.2",
        "9.3-9.4",
        "9.5-9.6",
        "9.7-9.8",
        "9.9-10",
        "10.1",
    ],
    "height_max_base_age_range": [
        "1-1.9",
        "2-2.9",
        "3-3.9",
        "4-5.9",
        "6-9.9",
        "10-14.9",
        "15-19.9",
        "20-24.9",
        "25-29.9",
        "30-39.9",
        "40-59.9",
        "60-79.9",
        "80-130",
    ],
    "frut_body_suit_ind": {
        "type": "bool",
    },
    "rsprt_able_ind": {
        "type": "bool",
    },
    "palat_animl_grz_condition": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high",
        ],
    },
    "growth_prd_actv_condition": {
        "type": "string",
        "allof": [
            "spring",
            "spring and fall",
            "spring and summer",
            "spring, summer, fall",
            "summer",
            "summer and fall",
            "fall, winter and spring",
            "year-round",
        ],
    },
    "propagation_cut_ind": [
        "yes",
        "no",
    ],
    "folg_prsty_wntr_condition": [
        "porous",
        "moderate",
        "dense",
    ],
    "folg_prsty_sumr_condition": [
        "porous",
        "moderate",
        "dense",
    ],
    "frut_seed_start_condition": [
        "spring",
        "summer",
        "fall",
        "winter",
        "year-round",
    ],
}
SEED_PER_LB_RANGE = [
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
    "40000000-49999999"
]
GROWTH_TOLERANCES = {
    "fire": "high",
    "salinity": "intermediate",
    "shade": {
        "type": "string",
        "anyof": ["intolerant", "intermediate", "tolerant"]
    },
    "drought": "low",
    "frost_free_days_min": {
        "type": "string",
        "anyof": [
            "0-51",
            "52-66",
            "67-81",
            "82-96",
            "97-111",
            "112-126",
            "127-141",
            "142-156",
            "157-171",
            "172-186",
            "187-201",
            "202-216",
            "217-231",
            "232-246",
            "247-261",
            "262-276",
            "277-291",
            "292-306",
            "307-321",
            "322-336",
            "337-351",
            "352-365"
        ],
    },
    "hedge": {
        "type": "string",
        "anyof": [
            "none",
            "low",
            "medium",
            "high",
        ],
    },
    "soil": {
        "preferred_type": "sandy-loam",
        "adaptations": {
            "coarse_texture": {
                "type": "bool",
                "default": False,
                "nullable": True,
            },
            "medium_texture": {
                "type": "bool",
                "default": False,
                "nullable": True,
            },
            "fine_texture": {
                "type": "bool",
                "default": True,
                "nullable": True,
            },
            "anaerobic_tolerance": None,
            "calcareous_tolerance": None,
        }
    },
}

GROWTH_REQUIREMENTS = {
    "aspect_hours": {
        "type": "float",
        "min": 0.0,
    },
    "tolerance": GROWTH_TOLERANCES,
    "aspect": "sun/half-shade",
    "moisture_use": "medium",
    "ph": {
        "type": "string",
        "anyof": SOIL_PH_TOLERANCE_MAX_RANGE
    },
    "planting_density_per_acre": None,
    "precipitation": {
        "min": {
            "type": "string", "anyof": PRECIPATION_TOLERANCE_MAX_RANGE,
        },
        "max": {
            "type": "string", "anyof": PRECIPATION_TOLERANCE_MIN_RANGE,
        }
    },
    "temperature": {
        "min": -40,
        "max": 90
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
REPRODUCTION = {
    "commercial_availability": None,
    "fruit_seed": {
        "dispersal": {
            # https://en.wikipedia.org/wiki/
            #   Biological_dispersal#Types_of_dispersal
            "type": {
                "nullable": True,
                "type": "string",
                "anyof": [
                    "density-independent",
                    "density-dependent",
                    "breeding",
                    "natal",
                ],
            },
            "shape": None,
            "spread_rate": "slow",
            "range": None,
            "per_pound": {
                "type": "string",
                "anyof": SEED_PER_LB_RANGE,
            },
        },
        "seedling_vigor": {
            "type": "string",
            "anyof": [
                "low",
                "medium",
                "high",
            ],
        },
        "small_grain": {
            "type": "bool",
            "default": False,
            "nullable": True,
        },
        "color": None,
        "conspicous": None,
        "abundance": "low",
        "period": {
            "begin": "spring",
            "end": "fall",
            "persistence": {
                "type": "bool",
                "default": False,
                "nullable": True,
            }
        }
    }
}
MORPHOLOGY_PHYSIOLOGY = {
    # "bark": ...,
    "active_growth_period": None,
    "after_harvest_regrowth_rate": None,
    "bloat": None,
    "c_to_n_ratio": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high",
        ]
    },
    "coppice_potential": None,
    "fall_conspicous": None,
    "fire_resistance": {
        "type": "bool",
        "default": False,
    },
    # "foliage": foliage.FOLIAGE_PHYSIOLOGY,
    "growth": {
        "vegetate_spread_rate": {
            "type": "string",
            "anyof": [
                "slow",
                "moderate",
                "rapid"
            ],
        },
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
    "leaf_retention": {
        "type": "bool",
        "nullable": True,
    },
    "lifespan": "moderate",
    "low_growing_grass": None,
    "nitrogen_fixation": None,
    "resprout_ability": None,
    "shape_and_orientation": None,
}


"""
RELATIONSHIPS - SCHEMA TBD:

Plant -> hasCultivars -> Cultivar
Cultivar -> isA -> Plant

"""

# TODO: is this the right approach? Does Marshmallow have an equivalent?
Relationship = namedtuple('Relationship', 'start, edge_name, end, desc')

RELATIONSHIPS = [
    Relationship(
        start=Plant, edge_name='hasCultivar',
        end=taxonomy.Cultivar,
        desc=''),

    Relationship(
        start=taxonomy.Cultivar,
        edge_name='isA',
        end=Plant,
        desc=''),
]

SCHEMA = {
    "itis_tns": None,
    "ecology": {
        "growth_habitat": "forb",
        "native_status": None
    },
    # "distribution": DISTRIBUTION,
    "hardwood": {
        "type": "bool",
        "default": False,
        "nullable": True,
    },
    "hardwood_scale": None,
    "morphology_and_physiology": MORPHOLOGY_PHYSIOLOGY,
    "reproduction": REPRODUCTION,
    "growth_requirements": GROWTH_REQUIREMENTS,
}
