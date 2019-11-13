"""Root characteristics."""
from neomodel import (
    BooleanProperty as BooleanProp,
    StructuredNode as Model,
    FloatProperty as FloatProp,
    StringProperty as StringProp,
    RelationshipTo,
    RelationshipFrom,
)


class RootAccumulation(Model):
    """Root nutrient/chemical accumulation."""

    name = StringProp(unique_index=True, required=True)
    ppm = FloatProp(required=True)

    accumulator = RelationshipFrom('Root', 'ACCUMULATED_BY')


class Root(Model):
    """General root characteristics."""

    avg_depth_inches = FloatProp(
        # min=0.1,
        # max=12000,  # 1,000 feet.
    )
    is_taproot = BooleanProp()
    dominant_root_type = StringProp(choices={c: c for c in [
        "wide",
        "shallow",
        "fibrous",
    ]})
    # So called "dynamic accumulator"
    accumulates = RelationshipTo(RootAccumulation, 'ACCUMULATES')
