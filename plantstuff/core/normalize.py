"""Cleanup/normalization."""


def clean(text):
    """Clean up text."""
    if not isinstance(text, (str, unicode)):
        return
    text = text.replace('\r', '')
    text = text.replace('\n', '')
    text = text.replace('  ', '')
    text = text.replace(':', '')
    return text.strip().lower()
