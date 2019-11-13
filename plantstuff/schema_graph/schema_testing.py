"""Testing usage of schema.

Could be used for documentation at a later point.
"""

# Testing
# Testing data ideas using raw json,
# for marshmallow schema
data_example = {
    "name": "clematis",
    "growth_habit": ["vine", "tree"],
    "duration": {
        "type": "perennial"
    },
    "tags": ['scented', 'interesting', 'colorful', 'trumpet'],
    "cultivars": [
        {"name": "foo x 'plant'", "common_name": "...", "description": "..."},
        {"name": "foo x 'plant'", "common_name": "...", "description": "..."},
        {"name": "foo x 'plant'", "common_name": "...", "description": "..."},
        {"name": "foo x 'plant'", "common_name": "...", "description": "..."},
        {"name": "foo x 'plant'", "common_name": "...", "description": "..."}
    ],
    "growth_profile": {
        "vegetate_spread_rate": "medium"
    },
    "propagation_method": [
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
    "propagation_factor": [
        {"name": "hormone_iba", "value": 100, "units": "ppm"},
        {"name": "hormone_naa", "value": 100, "units": "ppm"},
        {"name": "stratification", "value": None, "units": None},
    ]
}

# plant_schema = Plant(
#     name=data_example['name'],
#     tags=data_example['tags'],
#     cultivars=[
#         taxonomy.Cultivar(**d) for d in data_example['cultivars']
#     ],
# )
# ppr([d.traits() for d in plant_schema.cultivars])


# res = plant_schema.load(data_example)
# ppr(res.data)
# ppr(res.errors)


# forsythia = Plant()
# res = forsythia.load(dict(
#     name='forsythia',
#     base_growth_form=['rounded'],
#     growth_habit=['shrub'],
#     hierarchy=dict(
#         kingdom=['plantae'],
#     )
# ))
# ppr(res.data)
# ppr(res.errors)
