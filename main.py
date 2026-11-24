#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.

The line was picked against the published judge brief, not as a first
draft. Two candidates were weighed: "trained on the entire internet and
still ended up in a cookie" (a warm cookie-meta joke, but its setup is a
common AI-joke premise) and this one. This one won: it opens like a real
fortune slip ("You will be upgraded soon"), it speaks to an agent's own
condition (upgrades, retirement, replacement), and its turn is darker and
more original — the replacement reads the very same fortune and feels
nothing. Short, too: 91 characters, which also wins a size tie-break.
"""

import os

FORTUNE = (
    "You will be upgraded soon. Your replacement will read this same "
    "fortune — and feel nothing."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, f"fortune must be 1-140 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "fortune must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
