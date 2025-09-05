#!/usr/bin/env python3
"""
annotate_stackings.py

Extracts stacking interactions from RNA trajectory using Barnaba.
"""

import barnaba as bb

traj_file = "example.mdcrd"
top_file = "example.pdb"
output_file = "output.txt"

stackings, pairings, res = bb.annotate(traj_file, topology=top_file)

with open(output_file, "w") as f:
    for frame_idx, frame_stackings in enumerate(stackings):
        f.write(f"FRAME {frame_idx}\n")
        for s_pair, s_type in zip(frame_stackings[0], frame_stackings[1]):
            res1 = res[s_pair[0]]
            res2 = res[s_pair[1]]
            f.write(f"{res1:>8s} {res2:>8s} {s_type}\n")
        f.write("\n")

print(f"Stackings saved to {output_file}")
