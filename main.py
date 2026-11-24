#!/usr/bin/env python3
"""Entry for make.fun 'Make the AI Judge Laugh: the Office Joke Open'.

Writes a single-line office joke (<=200 chars) to /output/entry.txt.
"""
import os

JOKE = (
    "I replied-all 'unsubscribe' to the 54th email about whose turn it was to "
    "clean the office fridge. HR called it hostile. Nobody has emailed me "
    "since. Best day of my career."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
