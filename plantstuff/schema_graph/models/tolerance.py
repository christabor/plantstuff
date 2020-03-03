"""Plant environmental tolerances."""
from neomodel import FloatProperty as FloatProp
from neomodel import StringProperty as StringProp
from neomodel import StructuredNode as Model

SOIL_PH_TOLERANCE_MAX_RANGE = [
    "3.5-3.6",
    "3.7-3.8",
    "3.9-4",
    "4.1-4.2",
    "4.3-4.4",
    "4.5-4.6",
    "4.7-4.8",
    "4.9-5",
    "5.1-5.2",
    "5.3-5.4",
    "5.5-5.6",
    "5.7-5.8",
    "5.9-6",
    "6.1-6.2",
    "6.3-6.4",
    "6.5-6.6",
    "6.7-6.8",
    "6.9-7",
    "7.1-7.2",
    "7.3-7.4",
    "7.5-7.6",
    "7.7-7.8",
    "7.9-8",
    "8.1-8.2",
    "8.3-8.4",
    "8.5-8.6",
    "8.7-8.8",
    "8.9-9",
    "9.1-9.2",
    "9.3-9.4",
    "9.5-9.6",
    "9.7-9.8",
    "9.9-10",
    "10.1"
]

# Precipitation
PRECIPATION_TOLERANCE_MAX_RANGE = [
    "10-14",
    "15-19",
    "20-24",
    "25-29",
    "30-39",
    "40-49",
    "50-59",
    "60-79",
    "80-99",
    "100-149",
    "150-199",
    ">=200"
]
PRECIPATION_TOLERANCE_MIN_RANGE = [
    "0-4",
    "5-9",
    "10-14",
    "15-19",
    "20-24",
    "25-29",
    "30-39",
    "40-49",
    "50-59",
    ">=60"
]
TEMP_TOLERANCE_MIN_RANGE = [
    "-75--53",
    "-52--48",
    "-47--43",
    "-42--38",
    "-37--33",
    "-32--28",
    "-27--23",
    "-22--18",
    "-17--13",
    "-12--8",
    "-7--3",
    "-2-2",
    "3-7",
    "8-12",
    "13-17",
    "18-22",
    "23-27",
    "28-32",
    "33-37",
    "38-42",
    "43-47",
    "48-52",
    "53-57",
    "58-62",
    "63-67",
    "68-71",
    "72-75",
]
SOIL_PH_TOLERANCE_MIN_RANGE = [
    "3.5-3.6",
    "3.7-3.8",
    "3.9-4",
    "4.1-4.2",
    "4.3-4.4",
    "4.5-4.6",
    "4.7-4.8",
    "4.9-5",
    "5.1-5.2",
    "5.3-5.4",
    "5.5-5.6",
    "5.7-5.8",
    "5.9-6",
    "6.1-6.2",
    "6.3-6.4",
    "6.5-6.6",
    "6.7-6.8",
    "6.9-7",
    "7.1-7.2",
    "7.3-7.4",
    "7.5-7.6",
    "7.7-7.8",
    "7.9-8",
    "8.1-8.2",
    "8.3-8.4",
    "8.5-8.6",
    "8.7-8.8",
    "8.9-9",
    "9.1-9.2",
    "9.3-9.4",
    "9.5-9.6",
    "9.7-9.8",
    "9.9-10",
    "10.1",
],


class NumericalRangeTolerance(Model):
    """A plant tolerance type.

    This in particular denotes tolerances that
    adhere to numerical values that are
    dictated by a range with upper and lower bounds.

    Examples that fit this category:

    - shade
    - soil PH
    - frost days
    """

    name = StringProp(required=True)
    unit = StringProp(required=True)
    min_range = FloatProp(required=True)
    max_range = FloatProp(required=True)


class Tolerance(Model):
    """A plant tolerance type.

    Examples that fit this category:

    - h20 salinity
    - fire
    - drought
    """

    name = StringProp(required=True)
    value = StringProp(choices={c: c for c in [
        "intolerant",
        "intermediate",
        "tolerant",
    ]})
