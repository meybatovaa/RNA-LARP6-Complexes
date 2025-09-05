import matplotlib.pyplot as plt
import os

def parse_dotbracket_file(dot_file):
    """Read dot-bracket file and return sequence and structures."""
    with open(dot_file) as f:
        lines = [line.strip() for line in f if line.strip()]
    sequence = lines[0][1:] if lines[0].startswith(">") else lines[0]
    structures = lines[1:] if lines[0].startswith(">") else lines
    return sequence, structures

def count_dotbracket_states(dotbrackets):
    """Count per-residue opening '(', closing ')', and unpaired '.'."""
    length = len(dotbrackets[0])
    opens, closes, unpaired = [0]*length, [0]*length, [0]*length

    for db in dotbrackets:
        for i, c in enumerate(db):
            if c == "(": opens[i] += 1
            elif c == ")": closes[i] += 1
            elif c == ".": unpaired[i] += 1
    return opens, closes, unpaired

def plot_basepair_subplot(ax, sequence, opens, closes, unpaired, title=None, label=None):
    positions = range(len(sequence))
    ax.bar(positions, closes, color='darkseagreen', label=")", zorder=2)
    ax.bar(positions, opens, bottom=closes, color='coral', label="(", zorder=2)
    bottom_stack = [closes[i]+opens[i] for i in positions]
    ax.bar(positions, unpaired, bottom=bottom_stack, color='lemonchiffon', label=".", zorder=2)
    ax.set_xticks(positions)
    ax.set_xticklabels([str(p+1) for p in positions], fontsize=7)
    ax.set_yticks([])
    if title: ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    if label: ax.text(-0.05, 1.07, label, transform=ax.transAxes,
                      fontsize=13, color='black', ha='left', va='bottom')

def main():
    # List of constructs: (name, dotbracket_file)
    constructs = [
        ("WT 32nt", "32nt_WT_dotbracket.txt"),
        ("B1", "32nt_B1_dotbracket.txt"),
        ("B2", "32nt_B2_dotbracket.txt"),
        ("M3", "32nt_M3_dotbracket.txt"),
        ("WT 48nt", "48nt_WT_dotbracket.txt")
    ]
    corner_labels = ["a)", "b)", "c)", "d)", "e)"]

    fig, axes = plt.subplots(2, 3, figsize=(18,8), constrained_layout=True)
    axes = axes.flatten()

    for i, ((name, file), ax) in enumerate(zip(constructs, axes)):
        if not os.path.exists(file):
            print(f"File not found: {file}")
            continue
        seq, dotbrackets = parse_dotbracket_file(file)
        opens, closes, unpaired = count_dotbracket_states(dotbrackets)
        plot_basepair_subplot(ax, seq, opens, closes, unpaired, title=name, label=corner_labels[i])

    # Remove extra subplot if fewer constructs than axes
    for j in range(len(constructs), len(axes)):
        fig.delaxes(axes[j])

    # Legend
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='center left', bbox_to_anchor=(1.02,0.5), fontsize=12, frameon=False)

    plt.suptitle("Base Pairing Profiles of RNA Variants", fontsize=18, fontweight='bold', y=1.03)
    plt.savefig("basepairing_all.png", dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
