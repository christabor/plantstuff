"""Freeform schema validation functions."""


def one_word(val):
    """Validate single word values."""
    if len(val.split(' ')) > 1:
        raise ValueError('Must be one word!')
