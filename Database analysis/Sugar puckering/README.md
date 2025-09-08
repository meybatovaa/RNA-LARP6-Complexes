# Sugar Puckering Analysis

## Overview

- This folder contains scripts and workflows used to calculate and visualize sugar puckering pseudorotation angles in RNA trajectories.
- Sugar puckering analysis reveals whether nucleotides adopt C3′-endo (A-form, stable) or C2′-endo (flexible) conformations, providing insight into RNA helix stability and structural differences.

---

## Workflow

1. Using AmberTools `cpptraj` compute sugar puckering angles for each residue across the trajectory.
2. Outputs .dat files for each residue and one combined file.
3. Visualisation is performed in Python: angles are wrapped into the range [-180, 180) and Kernel density estimates (KDE) are plotted to compare distributions between constructs.

---

## Scripts

1. `sugar_pucker.sh`
- Uses `cpptraj` to calculate  pseudorotation angles (C1'–C2'–C3'–C4'–O4').
- Generates per-residue files (pucker_resX.dat) and a combined dataset (sugar_pucker_all.dat).
- Outputs `sugar_pucker_all.dat` → Residue, Frame, Pseudorotation Angle.
   
2. `plot_sugar_pucker.py`
- Python script for visualization.
- Reads .dat files from cpptraj.
- Wraps pseudorotation angles into [-180, 180).
- Filters to biologically relevant range [-100, 100].
- Plots side-by-side KDE distributions for constructs.

---

## Requirements

- AmberTools (cpptraj)
- Python
- pandas
- seaborn
- matplotlib
