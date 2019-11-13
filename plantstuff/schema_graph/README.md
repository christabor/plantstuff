# Plant Database schema [WIP]

## Requirements

### DB-agnostic approach

The core tenet of the schema design is to model it in a way that is **datastore-agnostic**. This means it could be translated to work in:

* Relational database (e.g. PostgreSql/MySQL)
* Document database (e.g. Mongo, Cassandra)
* Graph database/service (e.g. Neo4j, GRAKN)
* Easily serialized/de-serialized into an open source data format (e.g. JSON/XML) for long term storage/distribution

### Supports a wide variety of applications

Design oriented, like:

* Landscaping
* Gardening

Science oriented, like:

* Botany
* Horticulture

### Allows answering the following questions

A database should provide the ability to generate insights. As such, the ability to answer the following questions is paramount:

TBD.
