#!/bin/bash
# Extract sugar puckering pseudorotation angles per residue using cpptraj

PRMTOP=coords.prmtop
TRAJ=minima.mdcrd
N_RES=32
OUTFILE="sugar_pucker_all.dat"
CPPTRAJ_INPUT="sugar_pucker.in"

# Create cpptraj input using here-document
{
    echo "parm $PRMTOP"
    echo "trajin $TRAJ"
    for ((i=1; i<=N_RES; i++)); do
        printf "pucker p%d :%d@C1' :%d@C2' :%d@C3' :%d@C4' :%d@O4' range360 out pucker_res%d.dat\n" \
               "$i" "$i" "$i" "$i" "$i" "$i" "$i"
    done
    echo "run"
    echo "quit"
} > $CPPTRAJ_INPUT

# Run cpptraj
cpptraj -i $CPPTRAJ_INPUT

# Combine all residue outputs
echo "# Residue Frame Pseudorotation" > $OUTFILE
for ((i=1; i<=N_RES; i++)); do
    awk -v res=$i 'NF > 1 && $1 != "#" { print res, $1, $2 }' pucker_res$i.dat >> $OUTFILE
done

echo "Output written to $OUTFILE"
