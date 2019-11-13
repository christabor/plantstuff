DB=bolt://neo4j:password@localhost:7687

all:
	neomodel_remove_labels --db $(DB)
	neomodel_install_labels models.py --db $(DB)
