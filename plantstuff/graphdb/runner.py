from plantstuff.graphdb import models

# https://neomodel.readthedocs.io/en/latest/getting_started.html


forsythia = models.Plant(name='Forsythia').save()
for color in ['red', 'yellow', 'blue', 'green']:
    flower = models.Flower(color='yellow').save()
    forsythia.flower.connect(flower)

cultivar = models.Cultivar(name='lynwood').save()
forsythia.cultivars.connect(cultivar)
