"""Schema proposal.

# TODO: https://en.wikipedia.org/wiki/Glossary_of_botanical_terms
# https://en.wikipedia.org/wiki/Dehiscence_(botany)
# All of that would be supremely useful.
"""

PROPAGATION_METHODS = [
    {"type": "corm", "recommended_months": []},
    {
        "type": "sprigs", "recommended_months": []
    },
    {
        "type": "tubers", "recommended_months": []
    },
    {
        "type": "bulb", "recommended_months": []
    },
    {
        "type": "seed",
        "success_factors": [
            {
                "name": "scarification", "value": True,
                "recommended_months": ["april", "may"]
            },
            {
                "name": "stratification", "value": True,
                "recommended_months": ["april", "may"]
            },
        ]
    },
    {
        "type": "sod", "recommended_months": []
    },
    {
        "type": "tissue_culture", "recommended_months": []
    },
    {
        "type": "vegetative_cutting_semiripe",
        "success_factors": [
            {"name": "IBA", "value": "1000", "units": "PPM"},
            {"name": "NAA", "value": "1000", "units": "PPM"},
            {"name": "IAA", "value": "1000", "units": "PPM"},
        ],
        "recommended_months": []
    },
    {
        "type": "vegetative_cutting_greenwood", "recommended_months": []
    },
    {
        "type": "vegetative_cutting_hardwood", "recommended_months": []
    },
    {
        "type": "vegetative_cutting_softwood", "recommended_months": []
    },
    {
        "type": "bare_root", "recommended_months": []
    },
    {
        "type": "root_division",
        "recommended_months": ["october", "november", "december"]
    }
]

GROWTH_REQUIREMENTS = {
    "aspect_hours": 6.0,
    "aspect": "sun/half-shade",
    "moisture_use": "medium",
    "ph": {
        "min": 5.0,
        "max": 4.0
    },
    "planting_density_per_acre": None,
    "precipitation": {
        "min": None,
        "max": None
    },
    "temperature": {
        "min": -40,
        "max": 90
    },
    "tolerance": {
        "fire": "high",
        "salinity": "intermediate",
        "shade": "medium",
        "drought": "low",
        "frost_free_days_min": None,
        "hedge": "medium",
    },
    "soil": {
        "preferred_type": "sandy-loam",
        "adaptations": {
            "coarse_texture": False,
            "medium_texture": False,
            "fine_texture": True,
            "anaerobic_tolerance": None,
            "calcareous_tolerance": None,
        }
    },
    "water_requirements": "mostly_wet",
    "drainage": "well-drained",
    "hardiness": {
        "usda_zone": [1, 2, 3],
        "sunset_zone": [],
    },
    "root": {
        "depth": None,
        "type": "taproot",
    }
}

TAXONOMY = {
    "cultivars": [
        {
            "name": str,
            "flower_colors": [str],
            "description": str,
        },
    ],
    "category": "gymnosperm",
    "scientific_name": "acaena caesiiglauca",
    "family": {
        "name": "rosaceae",
        "common_name": "acanthus",
        "smybol": None,
    },
    "genus": None,
    "order": None,
    "subclass": None,
    "class": None,
    "subdivision": None,
    "division": None,
    "superdivision": None,
    "subkingdom": None,
    "kingdom": None,
    "itis_tns": None,
    "national_common_name": "sheepburr",
    "common_aliases": []
}
LEGAL = {
    "copyrighted": False,
    "gmo": False,
    "patented": False,
    "us_federal_noxious_status": None,
    "us_federal_noxious_common_name": None,
    "us_state_noxious_status": None,
    "us_plant_invasive_status": None,
    "us_federal_te_status": None,
    "us_federal_te_common_name": None,
    "us_state_te_status": None,
    "us_state_te_common_name": None,
    "us_national_wetland_indicator_status": None,
    "us_regional_wetland_indicator_region": None,
    "us_regional_wetland_indicator_status": None
}

REPRODUCTION = {
    "fertility_requirement": "low",
    # hermaphroditic or unisexual
    "sexual_organs": "hermaphroditic",
    # monoecious or dioecious
    "unisex_type": "monoecious",
    "stamens": None,
    "pistil": None,
    "pollination": {
        # https://en.wikipedia.org/wiki/Flower#Attraction_methods
        "attraction_method": "nectar",
        "attraction_speciality": "ultraviolet",
        "mechanism": [
            "entomophilous",
            "anemophilous",
        ],
        "methods": {
            "abiotic": [
                "wind (anemophily)",
                "water (hydrophily)"
            ],
            "biotic": [
                "insects (entomophily)",
                "birds (ornithophily)",
                "bats (chiropterophily)"
            ]
        },
    },
    "bloom_period": "spring",
    "commercial_availability": None,
    "fruit_seed": {
        "dispersal": {
            # https://en.wikipedia.org/wiki/Biological_dispersal#Types_of_dispersal

            # density-dependent
            # density-independent
            # breeding
            # natal
            "type": "density-dependent",
            "shape": None,
            "spread_rate": "slow",
            "range": None,
            "per_pound": {
                "min": 10,
                "max": 9999
            },
        },
        "seedling_vigor": "medium",
        "small_grain": True,
        "color": None,
        "conspicous": None,
        "abundance": "low",
        "period": {
            "begin": "spring",
            "end": "fall",
            "persistence": True
        }
    }
}

SCHEMA = {
    "taxonomy": TAXONOMY,
    "ecology": {
        "duration": "perennial",
        "growth_habitat": "forb",
        "native_status": None
    },
    "distribution": {
        "locales": [
            "US/Washington",
            "US/Hawaii",
            "EUR/Germany",
            "ASIA/Japan",
        ],
        "endemic": False
    },
    "hardwood": False,
    "hardwood_scale": None,
    "propagation_methods": PROPAGATION_METHODS,
    "tags": [
        "showy-flowers",
        "container-use",
        "cut-flowers"
    ],
    "legal": LEGAL,
    "morphology_and_physiology": {
        # http://www.backyardnature.net/treebark.htm
        "bark": {
            "type": [
                "smooth",
                "scaly",
                "plated",
                "warty",
                "shaggy",
                "papery",
                "furrowed",
                "fibrous"
            ],
            "thickness": None,
            "color": None
        },
        "active_growth_period": None,
        "after_harvest_regrowth_rate": None,
        "bloat": None,
        "c_to_n_ratio": None,
        "coppice_potential": None,
        "fall_conspicous": None,
        "fire_resistance": None,
        "flower": {
            "flower_type": "rosate",
            "inflorescence": True,
            "color": None,
            "conspicous": None,
            # https://en.wikipedia.org/wiki/Floral_formula
            "floral_formula": "↯ K3 [C3 A1°–3°+½:2°] Ğ(3)"
        },
        "foliage": {
            "type": [
                "brevideciduous",
                "deciduous",
                "evergreen",
                "broadleaf-evergreen",
                "marcescence"
            ],
            "anatomy": "pinnately-compound",
            "foliage_color": "green",
            "porosity_summer": None,
            "porosity_winter": None,
            "texture": None,
            "striped": False,
            "variegated": False
        },
        "growth": {
            "form": None,
            "vegetate_spread_rate": "moderate",
            "avg_root_depth": "2ft",
            "avg_spread": "3ft",
            "avg_landscape_size": "Fast grower to 24 to 36 in.",
            "avg_per_year": "2ft",
        },
        "height": {
            "avg": "5in",
            "at_base_max": 0.0,
            "avg_at_maturity": 9.0,
        },
        "leaf_retention": True,
        "lifespan": "moderate",
        "low_growing_grass": None,
        "nitrogen_fixation": None,
        "resprout_ability": None,
        "shape_and_orientation": None,
    },
    "concerns": {
        "allelopathic": False,
        "toxicity": "moderate",
        "toxicity_locations": ["root", "leaf", "stem"]
    },
    "reproduction": REPRODUCTION,
    "growth_requirements": GROWTH_REQUIREMENTS,
    # https://plants.usda.gov/adv_search.html
    # "Suitability/Use" section.
    "suitability_use": {
        "berry_nut_seed": None,
        "christmas_tree": None,
        "fodder": None,
        "fuelwood": None,
        "lumber": True,
        "naval_store_product": True,
        "nursery_stock_product": True,
        "palatable_browse_animal": None,
        "post_product": None,
        "protein_potential": None,
        "pulpwood_product": None,
        "veneer_product": None,
        "carbon_sequestration": "medium",
    },
}
