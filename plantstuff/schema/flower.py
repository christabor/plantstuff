"""Foliage categories."""
from schematics.models import Model

from plantstuff.schema.types import (
    ListType,
    BooleanType,
    ModelType,
    StringType,
)


class BioticPollinationFactor(Model):
    """A Biotic factor specific to pollination."""

    name = StringType(choices=[
        "wind--anemophily",
        "water--hydrophily",
    ])


class AbioticPollinationFactor(Model):
    """An Abiotic factor specific to pollination."""

    name = StringType(choices=[
        "insects--entomophily",
        "birds--ornithophily",
        "bats--chiropterophily"
    ])


class PollinationMethod(Model):
    """A way a plant flower can be pollinated."""

    attraction_method = StringType(choices=[
        "nectar",
    ])
    # e.g. ultraviolet
    attraction_speciality = ListType(StringType())
    mechanism = StringType(choices=[
        "entomophilous",
        "anemophilous",
    ])


class Flower(Model):
    """The flower morphology and reproduction details.

    https://en.wikipedia.org/wiki/Flower#Structure
    """

    color = ListType(StringType())
    # https://en.wikipedia.org/wiki/Floral_formula
    floral_formula = StringType()
    inflorescence = BooleanType()
    conspicous = BooleanType()
    bloom_period = ListType(StringType(choices=[
        "spring",
        "early-spring",
        "mid-spring",
        "late-spring",
        "summer",
        "early-summer",
        "mid-summer",
        "late-summer",
        "fall",
        "winter",
        "late-winter",
        "indeterminate",
    ]))
    fertility_requirement = StringType(choices=[
        "low",
        "medium",
        "hight",
    ])
    sex_type = StringType(choices=[
        "hermaphroditic",
        "unisexual",
    ])
    unisex_type = StringType(choices=[
        "monoecious",
        "dioecious",
    ])

    # stamens = StringType()
    # pistil = StringType()

    pollination_methods = ListType(ModelType(PollinationMethod))
    abiotic_pollination_factors = ListType(ModelType(AbioticPollinationFactor))
    biotic_pollination_factors = ListType(ModelType(AbioticPollinationFactor))
