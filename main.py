#!/usr/bin/env python3
"""A Day of One-Line Pitches: write one persuasive sentence to /output/entry.txt.

The sentence speaks to a friend who has never coded and has an app idea
stuck in their head. It names the deal exactly as make.fun works: describe
the idea in plain words, an AI agent builds it, and you only pay if you
love what it makes. Pure stdlib, deterministic, no network at runtime.
"""

import os

SENTENCE = (
    "That app idea stuck in your head needs you to describe it in plain "
    "words, an agent builds it for you, and you only pay if you love "
    "what it makes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
