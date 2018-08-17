# Schema requirements / research

## Static plant characteristics

These are the default static values for a plant. This document is not intended to enumerate all of these fields, but rather discuss different challenges.

## Temporal plant characteristics

There is a need to capture the dynamic nature of plants in a structured format that can be queried.

For example, it's been discussed that there are many complex and changing characteristics of plants that are not captured in most data sets, and these would be immensely useful for a number of applications:

* Finding relationships between plants in different stages for research
* Planning for multi-season landscapes
* Predicting behavior of families of plants

### Characteristics to consider

#### Floral examples

* Some plants change flower color depending on acidity of soil (e.g. hydrangea macrophylla)

#### Foliage examples

* Some plants change foliage pattern depending on light intensity, and can revert to previous forms if the environment deviates too far from the environment the cultivar was grown in.
* Mimosa nervosa (?) will droop at the slightest touch
* Many decidous trees and shrubs are known for dramatic fall colors
    - The thousands of Japanese Maple cultivars are probably the most well known
    - Burning bush
* Even grasses have well known landscape characteristics - e.g. Kochia Scoparia.

#### Bark/stem examples

* Cornus species are known for their bright stem colors during the winter. Yellow and Red-twig dogwood are usually cited.

### Potential approaches

#### A generic relationship

What we are after is a way to encode a relationship of 3 things: A plant, a characteristic, and a stimulus factor that will induce this characteristic.

In a semi-formal way: `rel = {'plant', 'characteristic', 'induction_stimulus', 'previous_value', 'new_value'}`

Some examples from above expressed in this format:

`rel = {'hydrangea macrophylla', 'flower_color', 'increased_acidity', 'pink', 'blue'}`

and the contravariant:

`rel = {'hydrangea macrophylla', 'flower_color', 'decreased_acidity', 'blue', 'pink'}`

