#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
plt.rcParams['font.family'] = 'Arial'

# RMSF data files
files = {
    "alpha 2I": '/home/angelina/Documents/rmsf/rmsf_rna_byres2I.dat',
    "alpha 1I": '/home/angelina/Documents/rmsf/rmsf_rna_byres.dat',
    "alpha 1III": '/home/angelina/Documents/rmsf/rmsf_rna_byres1III.dat'
}

data = {name: np.loadtxt(path, comments=['#']) for name, path in files.items()}

# Extract residues and RMSF values
residues_rmsf = {name: (d[:, 0].astype(int), d[:, 1]) for name, d in data.items()}

# Compute averages and peaks
threshold = 2.4
for name, (residues, rmsf) in residues_rmsf.items():
    print(f"Average RMSF ({name}): {np.mean(rmsf):.3f} Å")
    peaks = residues[rmsf > threshold]
    print(f"Peaks in {name}:", peaks)

# Plot RMSF per residue
fig, ax = plt.subplots(figsize=(12, 6))
styles = {
    "alpha 2I": {'color':'mediumseagreen', 'linestyle':'-', 'linewidth':2.2},
    "alpha 1I": {'color':'coral', 'linestyle':'--', 'linewidth':2.2},
    "alpha 1III": {'color':'royalblue', 'linestyle':'-.', 'linewidth':2.2}
}

for name, (residues, rmsf) in residues_rmsf.items():
    ax.plot(residues, rmsf, label=name, **styles[name])

ax.set_xlabel('Residue Index', fontsize=14, weight='bold')
ax.set_ylabel('RMSF (Å)', fontsize=14, weight='bold')
ax.set_title('RMSF WT vs Alternative Collagen Stemloops', fontsize=16, weight='bold')
ax.legend(fontsize=12)
sns.despine()
plt.tight_layout()
plt.savefig('/home/angelina/Documents/rmsf_comparison.png', dpi=300)
plt.show()
