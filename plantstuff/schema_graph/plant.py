"""Schema proposal.

TODO - resources for info/schema/data:
    https://en.wikipedia.org/wiki/Glossary_of_botanical_terms
    https://en.wikipedia.org/wiki/Dehiscence_(botany)
    https://en.wikipedia.org/wiki/Dendrology
    https://plants.usda.gov/charinfo.html


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
"""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    IntegerProperty as IntegerProp,
    FloatProperty as FloatProp,
    RelationshipTo,
    RelationshipFrom,
)

from plantstuff.schema_graph import validators
from plantstuff.schema_graph import (
    lifespan,
    reproduction,
    taxonomy,
    concerns,
    bark,
    foliage,
    flower,
    light,
    growth,
    root,
    seed,
    soil,
    stem,
    tolerance,
)

"""
NOTES:
attribution metafields??
Making sourcing/attribution/auditing of data really important
and upfront (from Andrew)

class Prop():
    _sources = ListProp(str)
    _type = None

    def __init__(self, type, **kwargs):
        self._type = type
        for k, v in kwargs.items():
            setattr(self, k, v)


class Tag(Model):
    name = Prop(str, required=True)
    description = Prop(str, required=True)


class Relationship():
    start = None
    end = None
    relname = Prop(str, required=True)


class Plant():
    pass


clematis = Plant(name='clematis')
clematis.tags = [
    Tag(name=Prop('loopy', sources=['...', '...']),
                  description='Some desc...'),
]
clematis.cultivars = [
    Cultivar(),
    Cultivar(),
]
"""


class Plant(Model):
    """The most generalized plant object."""

    name = StringProp(required=True)
    scientific_name = StringProp()
    national_common_name = StringProp()
    common_aliases = ListProp(StringProp())
    growth_form = ListProp(StringProp(choices={c: c for c in [
        "climbing",
        "columnar",
        "conical",
        "decumbent",
        "erect",
        "irregular",
        "oval",
        "open",
        "prostrate",
        "pyramidal",
        "rounded",
        "semi-erect",
        "vase",
        "weeping",
    ]}))
    growth_habit = ListProp(
        StringProp(choices={c: c for c in [
            "forb/herb",
            "graminoid",
            "lichenous",
            "nonvascular",
            "shrub",
            "subshrub",
            "tree",
            "vine",
        ]}),
    )
    growth_habit_condition = ListProp(StringProp(choices={
        c: c for c in [
            "bunch",
            "colonizing",
            "multiple-stem",
            "rhizomatous",
            "single-crown",
            "single-stem",
            "stoloniferous",
            "thicket-forming",
        ]
    }))
    usda_zone = ListProp(StringProp(choices={c: c for c in [
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
    ]}))
    sunset_zone = ListProp(StringProp(choices={}))
    avg_lifespan_years = IntegerProp()

    # ----- many to many or many to many rels --------------------
    propagation_methods = RelationshipTo(reproduction.PropagationMethod,
                                         'HAS_PROPAGATION_METHODS')
    propagation_factors = RelationshipTo(reproduction.PropagationFactor,
                                         'HAS_PROPAGATION_FACTORS')
    cultivars = ListProp(StringProp())
    tags = ListProp(StringProp(validators=[validators.one_word]))
    duration = RelationshipTo(lifespan.Duration, 'HAS_DURATION')

    # Broad, common categories with complex sub-relationships.
    hierarchy = RelationshipTo(taxonomy.TaxonomicRank, 'HAS_RANKS')

    bark = RelationshipTo(bark.Bark, 'HAS_BARK_TYPES')
    flower = RelationshipTo(flower.Flower, 'HAS_FLOWER_TYPES')
    root = RelationshipTo(root.Root, 'HAS_ROOT_TYPES')
    foliage = RelationshipTo(foliage.Foliage, 'HAS_FOLIAGE_TYPES')

    soil = RelationshipTo(soil.SoilType, 'HAS_SOIL_TYPES')
    seed = RelationshipTo(seed.Seed, 'HAS_SEED_TYPES')
    stem = RelationshipTo(stem.Stem, 'HAS_STEM_TYPES')

    companions = RelationshipTo('Plant', 'HAS_COMPANION_PLANT')

    regulation_concerns = RelationshipTo(concerns.RegulationConcern,
                                         'HAS_REGULATION_CONCERNS')
    biological_concerns = RelationshipTo(concerns.BiologicalConcern,
                                         'HAS_BIOLOGICAL_CONCERNS')

    # TOLERANCES
    drought_tolerance = RelationshipTo(tolerance.Tolerance,
                                       'HAS_DROUGHT_TOLERANCE_LEVEL')
    fire_tolerance = RelationshipTo(tolerance.Tolerance,
                                    'HAS_FIRE_TOLERANCE_LEVEL')
    anaerobic_tolerance = RelationshipTo(tolerance.Tolerance,
                                         'HAS_ANAEROBIC_TOLERANCE_LEVEL')
    calcareous_tolerance = RelationshipTo(tolerance.Tolerance,
                                          'HAS_CACO3_TOLERANCE_LEVEL')

    # "soil_adaptations": {
    #     "coarse_texture": {
    #         "type": "bool",
    #         "default": False,
    #         "nullable": True,
    #     },
    #     "medium_texture": {
    #         "type": "bool",
    #         "default": False,
    #         "nullable": True,
    #     },
    #     "fine_texture": {
    #         "type": "bool",
    #         "default": True,
    #         "nullable": True,
    #     },

    # "itis_tns": None,
    # "hardwood": {
    #     "type": "BooleanType",
    #     "default": False,
    #     "nullable": True,
    # },
    # "hardwood_scale": None,

    growth = RelationshipTo(growth.GrowthProfile, 'HAS_GROWTH_PROFILE')
    light = RelationshipTo(light.Light, 'HAS_LIGHT_REQUIREMENTS')

    # water_aspect = RelationshipTo(GrowthAspect)

    # MORPHOLOGY_PHYSIOLOGY = {
    #     "bloat": None,
    #     "c_to_n_ratio": {
    #         "type": "string",
    #         "anyof": [
    #             "low",
    #             "medium",
    #             "high",
    #         ]
    #     },
    #     # "foliage": foliage.FOLIAGE_PHYSIOLOGY,
    #     "nitrogen_fixation": None,
    #     "resprout_ability": None,
    # }


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
    "soil_adp_c_txt_ind": {
        "type": "BooleanType",
    },
    "post_suit_ind": {
        "type": "BooleanType",
    },
    "plantguide_ind": [
        "only with plant guides",
        "only without plant guides",
    ],
    "vs_comm_avail": [
        "no known source",
        "routinely available",
        "contracting only",
        "field collections only"
    ],
    "nurs_stk_suit_ind": {
        "type": "BooleanType",
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
    "flwr_cspc_ind": {
        "type": "BooleanType",
    },
    "plywd_vnr_suit_ind": {
        "type": "BooleanType",
    },
    "foddr_suit_ind": {
        "type": "BooleanType",
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
    "soil_adp_m_txt_ind": {
        "type": "BooleanType",
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
        "type": "BooleanType",
    },
    "navl_stor_suit_ind": {
        "type": "BooleanType",
    },
    "moist_use_condition": {
        "type": "string",
        "anyof": [
            "low",
            "medium",
            "high"
        ],
    },
    "folg_txt_condition": {
        "type": "string",
        "anyof": [
            "fine",
            "medium",
            "coarse",
        ],
    },
    "fed_te_status": [
        "with federal status",
        "--endangered",
        "--threatened",
        "without federal status"
    ],
    "soil_adp_f_txt_ind": {
        "type": "BooleanType",
    },
    "grass_low_grw_ind": {
        "type": "BooleanType",
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
    "coppice_potential_indicator": [
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
    "alepth_ind": {
        "type": "BooleanType",
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
    "fall_conspicous_indicator": {
        "type": "BooleanType",
    },
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
        "type": "BooleanType",
    },
    "rsprt_able_ind": {
        "type": "BooleanType",
    },
    "foliage_porosity_wntr_condition": [
        "porous",
        "moderate",
        "dense",
    ],
    "foliage_porosity_sumr_condition": [
        "porous",
        "moderate",
        "dense",
    ],
}
