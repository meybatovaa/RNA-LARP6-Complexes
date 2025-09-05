#!/usr/bin/env python3
"""
annotate_basepairs.py

Annotates RNA trajectory base-pair interactions using Barnaba
and outputs them frame by frame to a text file.
"""

import barnaba as bb

# User input files (update with your own paths)
traj_file = "trajectory.mdcrd"     
topology_file = "structure.pdb"   
output_file = "trajectory_basepairs.txt"

# Run Barnaba annotation
stackings, pairings, res = bb.annotate(traj_file, topology=topology_file)

# Save results
with open(output_file, "w") as f:
    for frame_idx, frame_pairings in enumerate(pairings):
        f.write(f"FRAME {frame_idx}\n")
        for pair, int_type in zip(frame_pairings[0], frame_pairings[1]):
            res1 = res[pair[0]]
            res2 = res[pair[1]]
            f.write(f"{res1:>8s} {res2:>8s} {int_type}\n")
        f.write("\n")

print(f"Base pairs saved to {output_file}")
