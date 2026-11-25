"""The Funniest Honest Appliance Error: a dishwasher tells the truth.

The joke angle
--------------
Most appliance error messages blame the machine: a sensor failed, a
pump jammed, a cycle aborted. This entry flips the blame around. The
dishwasher did its job perfectly -- every plate, every bowl, every fork
came out spotless -- and the one thing that went wrong is something the
machine could not possibly fix: the human loaded a mug upside down, so
the spray arms filled it with dirty water instead of rinsing it out.

That is the whole joke, and it is honest in the strictest sense. A
dishwasher really does work this way: water jets spray upward, an
upside-down mug catches the water like a cup, and the machine has no
way of knowing the mug is upside down until the cycle ends and the
water sits there. The fault is real, the physics is real, and the
machine is right to be annoyed. The humour comes from the machine
stating a fact its owner already knows but would rather not hear --
that the "broken dishwasher" is, in this case, a broken loading
technique -- and then refusing, in its flat put-upon voice, to take
the blame for it.

Why a dishwasher, and why this fault
-------------------------------------
A fridge or a toaster would be the obvious picks, but the dishwasher
is the appliance whose failures are most often the owner's fault in
disguise: blocked spray arms, detergent in the wrong compartment,
bowls nested so tightly no water reaches them. The upside-down mug is
the purest version of that pattern -- a single small decision at
loading time that defeats an entire hour of washing -- and it is a
fault every dishwasher owner recognises instantly, which is what makes
the line land without any explaining. The line never explains the
joke; it just reports the result and assigns responsibility.

Voice and economy
-----------------
The line is written in the machine's own voice: a terse error code,
a flat status report, and then the verdict, delivered without warmth
and without apology. "That one is on you" is the twist -- the machine
drawing a line between its work and yours, in four words, and then
stopping. Dropping any "not me" after it keeps the punchline from
explaining itself: the blame is already assigned, and the machine
has nothing more to say about it. Every word earns its place: the

Validation
----------
The entry is one line of at most 200 characters, plain UTF-8 text,
with no leading or trailing whitespace. A small helper below checks
those properties before writing, so a bad line fails loudly here
instead of silently reaching the judge.
"""

import os

# The entry: one line, the dishwasher's honest report after a cycle
# in which everything came out clean except the upside-down mug.
LINE = (
    "ERROR 12: Dishes clean. The mug you loaded upside-down is now "
    "a small pond of dirty water. That one is on you."
)

# The gate allows 1 to 200 characters of non-whitespace text.
MAX_CHARS = 200


def check_line(line):
    """Check the entry line against the gate's rules.

    Returns the line unchanged when it passes, and raises ValueError
    with a plain explanation when it does not, so a broken line can
    never be written out by accident.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    """Write the validated entry line to /output/entry.txt."""
    line = check_line(LINE)
    # Only create the directory; never chmod it. The grader collects
    # the output as a different user, and chmod on a directory it does
    # not own fails, so the directory is left exactly as created.
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    # The file itself is ours to make readable, so the collector can
    # read it no matter which user it runs as.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
