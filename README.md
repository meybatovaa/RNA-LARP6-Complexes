# Role of RNA in LARP6 complexes
This repository contains computational workflows and analysis scripts from my dissertation project investigating the structure and dynamics of RNA stem-loop elements from collagen mRNAs and their interaction with the RNA-binding protein LARP6. The study integrates molecular dynamics (MD) simulations and energy landscape analysis to investigate how RNA sequence and structural variation modulate LARP6 recognition.

## Methods Overview

- Secondary structures predicted with RNAfold (minimum free energy models).

3D models generated using RNAComposer.

- Molecular Dynamics Simulations

Performed with AMBER (pmemd).

System setup: RNA solvated in an OPC water box, neutralised with chloride ions.

Production runs: Five independent 500-ns simulations for each RNA construct (WT and mutants) under NPT at 300 K.

- Trajectory Analysis

CPPTRAJ (AMBER Tools) used for:

RMSD, RMSF, sugar puckering

MDTraj and Barnaba used for additional structural characterisation (sugar puckering, dot-bracket secondary structure).

- Energy Landscape Analysis

Pre-computed energy landscapes provided (minima, transition states, connectivity).

Disconnectivity graphs generated with DisconnectionDPS to visualise RNA folding pathways.

Structural features of minima extracted with Barnaba and MDTraj.

## Requirements

Python 3.9+

Jupyter Notebook

AMBER Tools (including CPPTRAJ)

Packages: numpy, scipy, pandas, matplotlib, mdtraj, barnaba
