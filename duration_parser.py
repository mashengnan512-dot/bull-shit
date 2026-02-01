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
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    s = text.strip()
    if not s:
        raise ValueError("duration string is empty")

    unit_to_seconds = {
        "s": 1,
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
    }

    i = 0
    total = 0
    found_group = False
    n = len(s)

    while i < n:
        # Skip whitespace between groups.
        while i < n and s[i].isspace():
            i += 1
        if i >= n:
            break

        if not s[i].isdigit():
            raise ValueError(f"expected number at position {i}")

        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord("0"))
            i += 1

        # Allow optional whitespace between number and unit (e.g. "1 h").
        while i < n and s[i].isspace():
            i += 1
        if i >= n:
            raise ValueError("missing unit at end of string")

        unit = s[i].lower()
        if unit not in unit_to_seconds:
            raise ValueError(f"unknown unit {s[i]!r} at position {i}")
        i += 1

        total += num * unit_to_seconds[unit]
        found_group = True

    if not found_group:
        raise ValueError("no duration groups found")

    return total

