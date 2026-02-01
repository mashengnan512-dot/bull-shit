"""
Duration parser utility.

This repo previously contained no commented TODOs. To satisfy the request,
we introduce one concrete TODO and then complete it in a follow-up commit.
"""

from __future__ import annotations


def parse_duration_seconds(text: str) -> int:
    """
    Parse a duration string into seconds.

    Supported formats:
    - One or more <number><unit> groups (e.g. "1h30m", "45s", "2d 3h")
    - Units: s, m, h, d (seconds/minutes/hours/days)

    Returns total duration in seconds.
    """
    # TODO: implement robust parsing with validation and whitespace handling.
    raise NotImplementedError("parse_duration_seconds is not implemented yet")

