"""Reproduction related aspects."""
from schematics.models import Model

from plantstuff.schema.types import (
    FloatType,
    ListType,
    StringType,
)


class PropagationMethod(Model):
    """The plant propagation type."""

    name = StringType(
        required=True,
        choices=[
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
        ],
    )

    recommended_months = ListType(StringType(choices=[
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
    ]))


class PropagationFactor(Model):
    """A type of factor that increases success of a given type."""

    name = StringType(
        choices=[
            "scarification",
            "stratification",
            "hormone_iba",
            "hormone_naa",
        ],
        required=True,
    )
    # e.g. if hormone, value most likely would be IBA/IAA
    # for Indole-3-Butyric Acid, or Indole-Acetic Acid.
    value = FloatType()
    # e.g. if hormone, units should be PPM
    units = StringType()
