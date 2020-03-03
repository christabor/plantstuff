import json

from neomodel import config

from plantstuff.schema_graph.models import (
    flower,
    plant,
    soil,
    root,
    reproduction,
    stem,
    bark,
    light,
    lifespan,
    growth,
)

# https://neomodel.readthedocs.io/en/latest/getting_started.html


config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'

# for soil_type in soil.SOIL_TYPES:
#     soilobj = soil.SoilType(name=soil_type)
#     soilobj.save()


# forsythia = models.Plant(name='Forsythia').save()
# for color in ['red', 'yellow', 'blue', 'green']:
#     flower = models.Flower(color='yellow').save()
#     forsythia.flower.connect(flower)

# cultivar = models.Cultivar(name='lynwood').save()
# forsythia.cultivars.connect(cultivar)


def add_plants(file_path):
    data = json.loads(open(file_path, 'r').read())
    for item in data:
        _flower = flower.Flower(color=[
            item['characteristics']['flower_colors']]).save()
        _plant_comp = plant.Plant(
            name='fake_companion',
            national_common_name='fake_companion',
        ).save()
        _plant = plant.Plant(
            name=item['common_name'],
            national_common_name=item['common_name'],
            usda_zone=item['needs']['hardiness_zones'],
            cultivars=[item['variety']],
        ).save()
        _plant.flower.connect(_flower)
        _plant.companions.connect(_plant_comp)

for file in os.listdir('')
