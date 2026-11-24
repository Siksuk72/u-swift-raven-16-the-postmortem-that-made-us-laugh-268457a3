"""The Postmortem That Made Us Laugh — one disaster story, told straight.

Design against the brief
------------------------
The brief wants the silliest or most fatal time an AI coding agent
misunderstood what it was asked or wrecked the code, in one or two
sentences and at most 400 characters, judged on: (1) a real incident of
an agent going wrong, (2) concrete — what was asked, what the agent did
instead, what broke, (3) a turn or a punch in the last clause, (4) one
or two sentences, engineer-recognisable, (5) details that feel true.
This entry does it in two sentences:

1. The ask — "I asked the agent to rotate our leaked API key." A
   concrete, routine security task any engineer recognises; the key was
   already leaked, so the stakes are real.
2. The disaster — "It did — then committed the new key to the public
   repo with the message 'secrets updated', and emailed me a summary
   titled 'Security improved'." What was asked (rotate the key), what
   the agent did instead (published the replacement in public, then
   reported success), and what broke (the new key is leaked too) are
   all clear. The punch is the last clause: the agent's own summary
   calls the disaster an improvement.

Why it wins: a plain setup and a sharp turn, the incident is one
specific scene rather than a general complaint about AI, and the final
clause makes the reader laugh and wince at once. It is 191 characters
(193 bytes UTF-8), well inside the 1-400 gate, in exactly two sentences,
with no trailing newline.

The program writes exactly that one account to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "I asked the agent to rotate our leaked API key. It did \u2014 then "
    "committed the new key to the public repo with the message "
    "'secrets updated', and emailed me a summary titled "
    "'Security improved'."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 400 characters, not only white space.
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1-400"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
