from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom)


config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


class Plant(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

    flower = RelationshipFrom('Flower', 'HAS_A')
    cultivars = RelationshipFrom('Cultivar', 'HAS_A')


class Flower(StructuredNode):
    uid = UniqueIdProperty()
    shape = StringProperty(default='radial')
    color = StringProperty(index=True, required=True)

    plant = RelationshipTo(Plant, 'IS_PART_OF')


class Cultivar(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()

    plant = RelationshipTo(Plant, 'IS_CHILD_OF')
