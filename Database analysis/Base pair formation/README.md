# Analysis of base pair formation

## Overview

- This folder contains scripts and tools for analyzing RNA structural dynamics of the 48 nucletoide wilf type (WT) and 32 nucleotide wild-type (WT) 5′SL RNA and its variants (B1, B2, M3). The pipeline extracts base-pair and stacking interactions from molecular dynamics (MD) simulations, converts them into dot-bracket representations, and visualizes base-pair formation per residue.
- The analysis is structure in three steps:
  - Annotation of base pairs and stacking from trajectories and topologies using Barnaba.
  - Dot bracket parsing of pairing states across all frames --> summary of base-pairing states per residue.
  - Visualisation of residue-level base-pairing frequencies.

---

## Requirements 

- Python 3.6+
- Scipy
- Mdtraj 1.9
- future
- Barnaba
- NumPy
- Pandas
- Matplotlib

---

## Scripts

1. `annotate_basepair.py`
- Uses barnana to annotate RNA trajectory base-pairs.
- Input a trajectory and topology ((All trajectory formats accepted by MDTRAJ (e.g. pdb, xtc, trr, dcd, binpos, netcdf, mdcrd, prmtop)).
- Outpt: `trajectory_basepairs.txt` listing per-frame base-pair interactions.
2. `dotbracket_parser.py`
- Parses dot-bracket files to compute per-residue pairing states.
- Distinguishes opening (, closing ), and unpaired . residues.
- Output: aggregated counts for each residue position across all frames.
3. `basepair_barplot.py`
- Generates bar plots of base-pairing per residue.


  


