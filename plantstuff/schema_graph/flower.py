"""Foliage categories."""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    FloatProperty as FloatProp,
    StringProperty as StringProp,
    BooleanProperty as BooleanProp,
    IntegerProperty,
    UniqueIdProperty,
    RelationshipTo,
    RelationshipFrom,
)

from plantstuff.schema_graph.formatters import basic_choice


class BioticPollinationFactor(Model):
    """A Biotic factor specific to pollination."""

    name = StringProp(choices=basic_choice([
        "wind--anemophily",
        "water--hydrophily",
    ]))


class AbioticPollinationFactor(Model):
    """An Abiotic factor specific to pollination."""

    name = StringProp(choices=basic_choice([
        "insects--entomophily",
        "birds--ornithophily",
        "bats--chiropterophily"
    ]))


class PollinationMethod(Model):
    """A way a plant flower can be pollinated."""

    attraction_method = StringProp(choices=basic_choice([
        "nectar",
    ]))
    # e.g. ultraviolet
    attraction_speciality = ListProp(StringProp())
    mechanism = StringProp(choices=basic_choice([
        "entomophilous",
        "anemophilous",
    ]))


class Flower(Model):
    """The flower morphology and reproduction details.

    https://en.wikipedia.org/wiki/Flower#Structure
    """

    color = ListProp(StringProp(), required=True)
    # https://en.wikipedia.org/wiki/Floral_formula
    floral_formula = StringProp()
    inflorescence = BooleanProp()
    conspicous = BooleanProp()
    bloom_period = ListProp(StringProp(choices=basic_choice([
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
    ])))
    fertility_requirement = StringProp(choices=basic_choice([
        "low",
        "medium",
        "hight",
    ]))
    sex_type = StringProp(choices=basic_choice([
        "hermaphroditic",
        "unisexual",
    ]))
    unisex_type = StringProp(choices=basic_choice([
        "monoecious",
        "dioecious",
    ]))
    # stamens = StringProp()
    # pistil = StringProp()

    # pollination_methods = RelationshipTo(PollinationMethod, '')
    # abiotic_pollination_factors = RelationshipTo(AbioticPollinationFactor, '')
    # biotic_pollination_factors = RelationshipTo(AbioticPollinationFactor, '')
