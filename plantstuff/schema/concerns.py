"""Plant concerns."""
from schematics.models import Model

from plantstuff.schema.types import (
    ListType,
    StringType,
)


class BiologicalConcern(Model):
    """A potential concern or danger of a plant."""

    name = StringType(choices=[
        "allelopathic",
        "noxious",
        "invasive",
        "poisonous",
    ])
    intensity = StringType(choices=[
        "slight",
        "moderate",
        "severe",
    ])
    location = ListType(StringType(choices=[
        "flower",
        "leaf",
        "root",
        "seed",
        "stem",
    ]))


class RegulationConcern(Model):
    """Business/legal regulatory concerns to be aware of."""

    name = ListType(StringType(choices=[
        "copyrighted",
        "gmo",
        "patented",
    ]))


class USNoxiousStatus(Model):
    """Noxious plant concerns."""

    federal_status = StringType(choices=[
        "with federal status",
        "--noxious weed",
        "--quarantine",
        "without federal status"
    ])
    state_status = StringType(choices=[
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
    ])


class USInvasiveStatus(Model):
    """Invasive plant concerns."""

    federal_status = StringType(choices=[
        "with invasive status",
        "--cal-ipc-exotic pest plant list",
        "--fleppc-invasive plant list",
        "--hear-information index for selected alien plants in hawaii",
        "--ky-weeds of kentucky and adjacent states: a field guide",
        "--n'east-weeds of the northeast",
        "--ne&gp-weeds of nebraska and the great plains",
        "--seeppc-invasive exotic pest plants in tennessee",
        "--state-state noxious weed lists for 35 states",
        "--swss-weeds of the united states and canada",
        "--us-federal noxious weed list",
        "--wi-wisconsin manual of control recommendations for ecologically invasive plants",
        "--wsws-weeds of the west",
        "without invasive status",
    ],
        required=True,
    )

# TODO: add
# "us_state_noxious_status",
# "us_plant_invasive_status",
# "us_federal_te_status",
# "us_federal_te_common_name",
# "us_state_te_status",
# "us_state_te_common_name",
