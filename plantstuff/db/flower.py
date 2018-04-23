"""Foliage categories."""
from marshmallow import Schema, fields
from marshmallow import validate


class BioticPollinationFactor(Schema):
    """A Biotic factor specific to pollination."""

    name = fields.Str(validate=validate.OneOf([
        "wind--anemophily",
        "water--hydrophily",
    ]))


class AbioticPollinationFactor(Schema):
    """An Abiotic factor specific to pollination."""

    name = fields.Str(validate=validate.OneOf([
        "insects--entomophily",
        "birds--ornithophily",
        "bats--chiropterophily"
    ]))


class PollinationMethod(Schema):
    """A way a plant flower can be pollinated."""

    attraction_method = fields.Str(validate=validate.OneOf([
        "nectar",
    ]))
    # e.g. ultraviolet
    attraction_speciality = fields.List(fields.Str)
    mechanicsm = fields.Str(validate=validate.OneOf([
        "entomophilous",
        "anemophilous",
    ]))


class Flower(Schema):
    """The flower morphology and reproduction details.

    https://en.wikipedia.org/wiki/Flower#Structure
    """

    color = fields.List(fields.Str)
    # https://en.wikipedia.org/wiki/Floral_formula
    floral_formula = fields.Str()
    inflorescence = fields.Bool()
    conspicous = fields.Bool()
    bloom_period = fields.List(fields.Str(validate=validate.OneOf([
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
    fertility_requirement = fields.Str(validate=validate.OneOf([
        "low",
        "medium",
        "hight",
    ]))
    sex_type = fields.Str(validate=validate.OneOf([
        "hermaphroditic",
        "unisexual",
    ]))
    unisex_type = fields.Str(validate=validate.OneOf([
        "monoecious",
        "dioecious",
    ]))
    # stamens = fields.Str()
    # pistil = fields.Str()
    # pollination_factors = TODO: abiotic/biotic.
