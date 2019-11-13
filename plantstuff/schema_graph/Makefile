DB=bolt://neo4j:password@localhost:7687

nukemodels:
	neomodel_remove_labels --db $(DB)
addmodels:
	neomodel_install_labels *.py --db $(DB)
ingest:
	python runner.py
all: nukemodels addmodels ingest
