# Database Analysis

## Overview 
This folder contains scripts and data for analyzing RNA structural ensembles from energy landscape explorations and precomputed simulations. It focuses on 48 nucleotide wild-type (WT) RNA and 32 nucleotide RNAs (WT and mutants B1, M3, B2). Analyses include base-pairing patterns, RMSF per residue, sugar puckering, and disconnectivity graphs. The goal is to explore structural changes in RNA sequences and how they affect LARP6 recognition.

## Working directory 

## Requirements
- Python 3.9
- Mdtraj
- numpy
- matplotlib
- seaborn
- scipy
- Barnaba
- AMBERTOOLS

## Notes 

- 32nt RNAs serve as minimal binding elements compared to the 48nt WT.
- RMSF analysis identifies flexible regions.
- Sugar puckering analysis characterizes nucleotide geometries.
- Base-pair annotation uses Barnaba to generate dot-bracket files.
- Disconnectivity graphs visualize energy relationships between minima and transition states

## References 
- Röder, K., Joseph, J. A., Husic, B. E., & Wales, D. J. *Energy Landscapes for Proteins: From Single Funnels to Multifunctional Systems.* Adv. Theory Simul. 2, 1800175 (2019). [https://doi.org/10.1002/adts.201800175](https://doi.org/10.1002/adts.201800175) 
- Barnaba RNA Analysis Toolkit: [Barnaba GitHub](https://github.com/srnas/barnaba)  
- MDTraj: [MDTraj Documentation](https://www.mdtraj.org/)  
- DisconnectionDPS (Energy Landscape Analysis): Wales, D. J. et al., *J. Chem. Phys.*
