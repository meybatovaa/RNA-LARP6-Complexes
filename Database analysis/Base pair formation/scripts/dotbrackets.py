#!/usr/bin/env python3
"""
generate_dotbracket.py

Converts Barnaba base-pairing results into dot-bracket notation.
"""

import barnaba as bb

# Load previously annotated pairings
bp_file = "trajectory_basepairs.txt"

traj_file = "example.mdcrd"
top_file = "example.pdb"

stackings, pairings, res = bb.annotate(traj_file, topology=top_file)

dotbrackets, seq = bb.dot_bracket(pairings, res)

db_file = "dotbrackets.txt"
with open(db_file, "w") as f:
    f.write(f">{seq}\n")
    for db in dotbrackets:
        f.write(db + "\n")

print(f"Dot-bracket annotations saved to {db_file}")
