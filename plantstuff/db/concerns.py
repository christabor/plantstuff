"""Plant concerns."""
from marshmallow import Schema, fields
from marshmallow import validate


class BiologicalConcern(Schema):
    """A potential concern or danger of a plant."""

    name = fields.Str(required=True, validate=validate.OneOf([
        "allelopathic",
        "noxious",
        "invasive",
        "poisonous",
    ]))
    intensity = fields.Str(required=True, validate=validate.OneOf([
        "slight",
        "moderate",
        "severe",
    ]))
    location = fields.List(
        fields.Str,
        required=True,
        validate=validate.OneOf([
            "flower",
            "leaf",
            "root",
            "seed",
            "stem",
        ]))


class BusinessRegulationConcern(Schema):
    """Business/legal regulatory concerns to be aware of."""

    name = fields.List(fields.Str, required=True, validate=validate.OneOf([
        "copyrighted",
        "gmo",
        "patented",
    ]))


class USNoxiousStatus(Schema):
    """Federal noxious plant concerns."""

    federal_status = fields.Str(
        required=True,
        validate=validate.OneOf([
            "with federal status",
            "--noxious weed",
            "--quarantine",
            "without federal status"
        ]),
    )
    state_status = fields.Str(
        required=True,
        validate=validate.OneOf([
            "with state status",
            "--alaska",
            "--alabama",
            "--arkansas",
            "--arizona",
            "--california",
            "--colorado",
            "--connecticut",
            "--delaware",
            "--florida",
            "--hawaii",
            "--iowa",
            "--idaho",
            "--illinois",
            "--indiana",
            "--kansas",
            "--kentucky",
            "--louisiana",
            "--massachusetts",
            "--maryland",
            "--maine",
            "--michigan",
            "--minnesota",
            "--missouri",
            "--mississippi",
            "--montana",
            "--north carolina",
            "--north dakota",
            "--nebraska",
            "--new hampshire",
            "--new mexico",
            "--nevada",
            "--ohio",
            "--oklahoma",
            "--oregon",
            "--pennsylvania",
            "--south carolina",
            "--south-dakota",
            "--tennessee",
            "--texas",
            "--utah",
            "--virginia",
            "--vermont",
            "--washington",
            "--wisconsin",
            "--west-virginia",
            "--wyoming",
            "without state status",
        ]),
    )


# TODO: add
# "us_state_noxious_status",
# "us_plant_invasive_status",
# "us_federal_te_status",
# "us_federal_te_common_name",
# "us_state_te_status",
# "us_state_te_common_name",
