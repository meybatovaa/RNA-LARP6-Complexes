import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks

sns.set_style("white")

#
trajectories = {
    "WT": {"traj": ".mdcrd",
           "top": ".prmtop"},
    "M3": {"traj": ".mdcrd",
           "top": ".prmtop"},
}

threshold = 1.4  # RMSF peak threshold in Å
output_png = "RMSF_comparison.png"
rmsf_atom_indices = None  # Use all atoms

def atom_to_residue_rmsf(traj, rmsf_atoms):
    """Convert atom RMSF to residue RMSF by averaging over atoms in each residue."""
    res_rmsf = np.zeros(traj.n_residues)
    count = np.zeros(traj.n_residues)
    for i, atom in enumerate(traj.topology.atoms):
        res_idx = atom.residue.index
        res_rmsf[res_idx] += rmsf_atoms[i]
        count[res_idx] += 1
    return res_rmsf / count
  
rmsf_data = {}
peaks_data = {}

for label, files in trajectories.items():
    traj = md.load(files["traj"], top=files["top"])
    traj.superpose(traj[0])
    
    rmsf_atoms = md.rmsf(traj, traj, frame=0, atom_indices=rmsf_atom_indices) * 10  # nm -> Å
    rmsf_res = atom_to_residue_rmsf(traj, rmsf_atoms)
    
    rmsf_data[label] = rmsf_res
    peaks, _ = find_peaks(rmsf_res, height=threshold)
    peaks_data[label] = peaks
    
    print(f"{label} average RMSF: {rmsf_res.mean():.2f} Å")
    print(f"{label} peaks at residues: {peaks}")

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
colors = ["darkseagreen", "coral"]
linestyles = ["-", "--"]

for i, (label, rmsf_res) in enumerate(rmsf_data.items()):
    ax.plot(rmsf_res, color=colors[i], linestyle=linestyles[i], linewidth=2.2, label=label)
    for peak in peaks_data[label]:
        ax.axvline(peak, color=colors[i], linestyle=":", linewidth=1.5)

ax.set_xlabel("Residue Index", fontsize=14, weight='bold')
ax.set_ylabel("RMSF (Å)", fontsize=14, weight='bold')
ax.set_title("Backbone RMSF Comparison", fontsize=16, weight='bold')
ax.set_xlim(0, len(next(iter(rmsf_data.values()))) - 1)
ax.legend(loc='upper right', fontsize=12, frameon=False)

plt.tight_layout()
plt.savefig(output_png, dpi=300)
plt.show()
