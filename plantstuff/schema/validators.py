"""Freeform schema validation functions."""

from schematics.exceptions import ValidationError


def one_word(val):
    """Validate single word values."""
    if len(val.split(' ')) > 1:
        raise ValidationError('Must be one word!')
