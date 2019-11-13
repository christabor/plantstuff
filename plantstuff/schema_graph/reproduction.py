"""Reproduction related aspects."""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    FloatProperty as FloatProp,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
)


class PropagationMethod(Model):
    """The plant propagation type."""

    name = StringProp(
        required=True,
        choices={c: c for c in [
            "bare_root",
            "bulb",
            "corm",
            "root_division",
            "seed",
            "sod",
            "tissue_culture",
            "tuber",
            "vegetative_cutting_greenwood",
            "vegetative_cutting_hardwood",
            "vegetative_cutting_softwood",
        ]},
    )

    recommended_months = ListProp(StringProp(choices={c: c for c in [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]}))


class PropagationFactor(Model):
    """A type of factor that increases success of a given type."""

    name = StringProp(
        choices={c: c for c in [
            "scarification",
            "stratification",
            "hormone_iba",
            "hormone_naa",
        ]},
        required=True,
    )
    # e.g. if hormone, value most likely would be IBA/IAA
    # for Indole-3-Butyric Acid, or Indole-Acetic Acid.
    value = FloatProp()
    # e.g. if hormone, units should be PPM
    units = StringProp()
