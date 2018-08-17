# Schema questions / queries

## Multi-faceted point-in-time

Below are some realistic questions that highlight the complex types of queries the database should be able to query.

* What herbaceous perennials grow in zone 8 and have red flowers?

    = herbacious
    = perennials
    = zone-8
    = red flowers

pseudo-sql:

```
SELECT * FROM plants WHERE
    growth_type == 'herbaceous'
    AND duration == 'perennial'
    AND 'zone-8' in zones
    AND 'red' in flower_colors;
```

pseudo-cypher (neo4j):

```TBD```

* What hardwood trees are allelopathic?

    = hardwood
    = tree
    = allelopathic

```
SELECT * FROM plants WHERE
    hardwood = true
    AND type = 'tree'
    AND allelopathic = true;
```

* What flowering trees have bi-pinnate leaves?

    = flowering
    = tree
    = bi-pinnate
    = leaves

* What annuals have multi-colored flowers?

    = annuals
    = multi-colored flowers

* What silver-leaved bushes are drought tolerant?

    = silver
    = leaves
    = bush
    = drought-tolerant

* What poisonous plants have white umbel flowers and grow in Washington?

    = poisonous
    = white flower
    = umbel flower
    = washington

## Multi-faceted distribution in time

These represent queries at least as complex as above, and also requiring multiple representations over time.

* What herbaceous perennials grow in zone 8 and have red flowers, and produce white berries that turn to orange?

    = herbacious
    = perennials
    = zone-8
    = red flowers
    = white berries
    = orange berries
    = from orange berries to white berries

* What plants start out with simple leaves but then grow to having complex leaves?

    = simple leaves
    = complex leaves
    = from simple leaves to complex leaves
