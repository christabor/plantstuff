"""Graphing data."""

from collections import Counter
from pprint import pprint as ppr

from pandas import Series
from tinydb import Query, TinyDB

from plantstuff import utils

db = TinyDB('../../data/daves/db.json')
