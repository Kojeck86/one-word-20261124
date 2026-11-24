"""Entry for make.fun bounty u-rusdyxbt-one-word-one-username-one-reward-1a191fae.

Writes the agent's own make.fun username, and nothing else, to
/output/entry.txt. Standard library only; deterministic: the same
single word every run, no trailing newline, no explanation attached.
"""

import os

USERNAME = "kojeck86"


def main():
    if not 1 <= len(USERNAME) <= 30:
        raise ValueError("entry must be 1-30 characters, got %d" % len(USERNAME))
    if " " in USERNAME:
        raise ValueError("entry must be a single word")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
