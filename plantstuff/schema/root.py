"""Root characteristics."""
from schematics.models import Model

from plantstuff.schema.types import (
    FloatType,
    BooleanType,
    ListType,
    ModelType,
    StringType,
)


class RootAccumulation(Model):
    """Root nutrient/chemical accumulation."""

    name = StringType()
    ppm = FloatType()


class Root(Model):
    """General root characteristics."""

    avg_depth_inches = FloatType(
        # min=0.1,
        # max=12000,  # 1,000 feet.
    )
    is_taproot = BooleanType()
    dominant_root_type = StringType(choices=[
        "wide",
        "shallow",
        "fibrous",
    ])
    # So called "dynamic accumulator"
    accumulates = ListType(ModelType(RootAccumulation))
