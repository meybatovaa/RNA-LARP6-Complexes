# Role of RNA in LARP6 complexes
This repository contains computational workflows and analysis scripts from my dissertation project investigating the structure and dynamics of RNA stem-loop elements from collagen mRNAs and their interaction with the RNA-binding protein LARP6. The study integrates molecular dynamics (MD) simulations and energy landscape analysis to investigate how RNA sequence and structural variation modulate LARP6 recognition. It focuses on comparing multiple RNA sequences and variants to understand how sequence changes impact folding, base-pairing, sugar puckering, and flexibility. 

---

## Methods Overview
1. Molecular dynamic simulations
- The objective is to characterise flexibility and dynamic behaviour of three RNA stem loops from collagen mRNAs (WT and variants).
- Secondary structures predicted using `RNAfold`, converted to 3D models via `RNAComposer`.
- Systems solvated in explicit water and neutralised with Cl- ions.
- Simulation involved energy minimisation, gradual heating to 300K, equilibrations, followed by multiple 500 ns production runs using `pmemd` program from `AmberTools` programs collection.
- Analysis involved calculation of root-mean-square fluctuations to quantify per residue flexibility.

2. Database derived RNA Analysis of 32nt and 48nt sequences.
- The objective is to explore the energy landscape and structural features of RNA sequences.
- Provided data includes `min.data`, `ts.data`, `points.min` for each RNA.
- For energy landscape visualisation, the `DisconnectionDPS` script was used to generate disconnectivity graphs illustrating connectivity between minima and energy barriers.
- `dumpTraj` reformats minima coordinates to trajectories compatible with MD analysis tool.
- Base pairing analysis identifies pairing interactions per frame using `Barnaba`.
- RMSF was computed per residue using `MDTraj` to reveal flexible regions.
- Sugar puckering was calculated with `CPPTRAJ`, providing pseudorotation angles for nucleotides.

---

## Requirements

- Python 3.9+ with libraries mdtraj, numpy, matplotlib, seaborn, scipy
- Barnaba
- AMBER Tools (including CPPTRAJ)

## References 

## References

1. **Röder, K., Joseph, J. A., Husic, B. E., & Wales, D. J. (2019).**  
   *Energy Landscapes for Proteins: From Single Funnels to Multifunctional Systems.*  
   Advanced Theory and Simulations, 2(4), 1800175.  
   [https://doi.org/10.1002/adts.201800175](https://doi.org/10.1002/adts.201800175)

2. **RNAfold web server**  
   [http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi](http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi)

3. **RNAComposer**  
   [https://rnacomposer.ibch.poznan.pl/](https://rnacomposer.ibch.poznan.pl/)

4. **AMBER software suite**  
   [http://ambermd.org/](http://ambermd.org/)

5. **Barnaba**  
   [https://github.com/srnas/barnaba](https://github.com/srnas/barnaba)

6. **MDTraj**  
   [https://www.mdtraj.org/](https://www.mdtraj.org/)

7. **DisconnectionDPS**  
   Wales, D. J. et al., *J. Chem. Phys.*, 20XX






