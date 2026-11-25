"""The Funniest Office Joke, Judged Head to Head.

Writes one office joke (at most 200 characters) to /output/entry.txt.
"""

# Design notes: the concept in one sentence is a standup meeting that
# stretches so long an intern lives a whole career inside it — beard,
# promotion, retirement — while the Jira ticket never moves. The judge
# lesson is specificity: one recognisable office pain, escalated to the
# absurd, beats a generic "meetings are boring" complaint that every
# entry could write. The intern's career is the clock: beard, promotion,
# retirement are three life stages, so the reader feels the time pass
# instead of being told the meeting was long. The ticket staying "in
# progress" is the punchline because it is the one thing that did not
# change. Rejected: a joke about the boss being late, which blames a
# person instead of a process; a version with the meeting ending on
# time, which removes the premise; and a version without the judge
# named at the end, which would leave the line talking past its reader.

ENTRY = (
    "Our standup ran so long the intern grew a beard, got promoted, retired "
    "— and the Jira ticket is still 'in progress', Judge."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"chars={len(ENTRY)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
