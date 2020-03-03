"""Plant concerns."""
from neomodel import (
    ArrayProperty as ListProp,
    StructuredNode as Model,
    StringProperty as StringProp,
)


class BiologicalConcern(Model):
    """A potential concern or danger of a plant."""

    name = StringProp(choices={c: c for c in [
        "allelopathic",
        "noxious",
        "invasive",
        "poisonous",
    ]})
    intensity = StringProp(choices={c: c for c in [
        "slight",
        "moderate",
        "severe",
    ]})
    location = ListProp(StringProp(choices={c: c for c in [
        "flower",
        "leaf",
        "root",
        "seed",
        "stem",
    ]}))


class RegulationConcern(Model):
    """Business/legal regulatory concerns to be aware of."""

    name = ListProp(StringProp(choices={c: c for c in [
        "copyrighted",
        "gmo",
        "patented",
        "restricted",
    ]}))


class USNoxiousStatus(Model):
    """Noxious plant concerns."""

    federal_status = StringProp(choices={c: c for c in [
        "with federal status",
        "--noxious weed",
        "--quarantine",
        "without federal status"
    ]})
    state_status = StringProp(choices={c: c for c in [
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
    ]})


class USInvasiveStatus(Model):
    """Invasive plant concerns."""

    federal_status = StringProp(choices={c: c for c in [
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
    ]},
        required=True,
    )

# TODO: add
# "us_state_noxious_status",
# "us_plant_invasive_status",
# "us_federal_te_status",
# "us_federal_te_common_name",
# "us_state_te_status",
# "us_state_te_common_name",
