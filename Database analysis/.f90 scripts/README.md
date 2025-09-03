# F90 Scripts for RNA Database Analysis

## Overview
- This folder contains direction for using the Fortran 90 scripts for analyzing RNA energy landscape databases. 
- The scripts perform two main tasks:

  - **Trajectory conversion** (`minima.mdcrd`): convert minima coordinates into trajectory files for downstream structural analyses, such as RMSF, base-pairing, and secondary structure.
  - **Disconnectivity graphs**: visualize the RNA folding energy landscape and relationships between minima and transition states. 

---

## Requirements
- Fortran 90 compiler (e.g., `gfortran`, `ifort`)  
- Input files for each system:
  - `min.data`: Energy minima  
  - `ts.data`: Transition states linking minima  
  - `dinfo`: Options and parameters for disconnectivity graph construction  
  - `points.min`: Cartesian coordinates of minima (for trajectory conversion)
  - `coords.prmtop`: Amber topology file for RNA system
  - `coords.inpcrd`: Amber coordinate file for RNA system
---

## Working directory 
- Work from /scratch/prj/roeder_lido_rna/Databases with subdirectories for each RNA (48nt_WT, 32nt WT, B1, M3, B2)
- Each subdirectory contains the required files described above

## Compilation
- Compile the scripts using a Fortran 90 compiler:

```bash
f95 dumpTraj.f90 -o dumpTraj
f95 DisconnectionDPS.f90 -o DisconnectionDPS
```

## Usage
1. **Trajectory conversion**
- Converts the minima database into a trajectory file compatible with MD analysis tools.
- <num_atoms> specifies the number of atoms in the system.
- Requires points.min to be present in the working directory.

```bash
./dumpTraj <num_atoms>
```

2. **Disconectivity graphs**
- Produces `tree.ps`, a PostScript file visualizing the RNA energy landscape.

```bash
./DisconnectionDPS
```

- View in `gv tree.ps` or convert to PDF:

```bash
ps2pdf tree.ps
```
---

## Notes

- Each RNA system may have specific distance or plotting parameters; ensure the dinfo file corresponds to the system being analyzed.
- The minima.mdcrd trajectories can be used with Barnaba or MDTraj for downstream analyses including RMSF calculations, base-pairing, and secondary structure assignments.
- Scripts should be executed in the directory containing the respective database files.

---

## References

- Konstantin Röder, Joseph JA, Husic BE, Wales DJ. *Energy Landscapes for Proteins: from Single Funnels to Multifunctional Systems.* Advanced Theory and Simulations, 2019 Jan 8 ;2(4). Available from: [https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adts.201800175](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adts.201800175)
- Dr. Miller M. *disconnectionDPS: Fortran Program to Generate Disconnectivity Graphs from Stationary Point Databases*, 2014 . Available from: [http://www-wales.ch.cam.ac.uk/software.html](http://www-wales.ch.cam.ac.uk/software.html)






















