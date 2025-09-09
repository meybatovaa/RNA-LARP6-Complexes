# Analysis of Root Mean Square Fluctuation

## Overview
- This folder contains scripts and data used to calculate and visualize Root Mean Square Fluctuation (RMSF) per residue for RNA constructs.
- RMSF measures the average deviation of each atom (or residue) from its mean position over the course of a molecular dynamics (MD) trajectory. 
- It provides a quantitative estimate of the flexibility or mobility of different regions of a molecule.
- Low RMSF values indicate rigid, stable regions (e.g., helices, base-paired stems).
- High RMSF values indicate flexible or dynamic regions (e.g., loops, bulges, unpaired nucleotides).

---

## Requirements 
- Python 3.6+
- Numpy
- Scipy
- Seaborn
- Mdtraj 1.9
- future

---

# Workflow

1. Load input files – trajectory (`.mdcrd`) and topology (`.prmtop`) are read using MDTraj.
2. Align frames to the first one, superimpose trajectories. 
3. Calculate per-atom RMSF and average to per-residue values.
4. Identify flexible regions by detecting resiues with higher RMSD values.
5. Visualise results.

---

# Scripts

- `rmsf_WT_vs_mutant.py`
  - Computes and plots backbone root mean square fluctuation (RMSF) per residue for two RNAs.
  - Inputs: trajectory and topology files for WT and mutants.
  - Outputs: png plot comparing RMSF profiles between the two constructs, with peaks highlighted.
  - Console output reporting the average RMSF values and the residue indices where peaks occur.
    
