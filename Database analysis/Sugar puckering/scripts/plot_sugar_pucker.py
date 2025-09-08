import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(filepath):
    data = pd.read_csv(
        filepath,
        sep=r'\s+',
        comment="#",
        names=["Residue", "Frame", "Angle"],
        engine='python',
        on_bad_lines='skip'
    )
    data["Angle"] = ((data["Angle"] + 180) % 360) - 180
    return data[(data["Angle"] >= -100) & (data["Angle"] <= 100)]

def plot_comparison(data_dict, output_file="sugar_pucker_comparison.png"):
    n = len(data_dict)
    fig, axes = plt.subplots(1, n, figsize=(6*n, 6), constrained_layout=True)

    if n == 1:
        axes = [axes]

    for ax, (label, data) in zip(axes, data_dict.items()):
        sns.kdeplot(
            data["Angle"],
            bw_adjust=1.5,
            fill=True,
            color="darkseagreen",
            linewidth=2,
            ax=ax
        )
        ax.set_title(label, weight="bold")
        ax.set_xlabel("Pseudorotation Angle (°)", weight="bold")
        ax.set_ylabel("Normalized Density", weight="bold")
        ax.set_xlim(-100, 100)
        ax.grid(False)

    plt.savefig(output_file, dpi=300)
    plt.show()

def main():
    # Provide relative paths or filenames for your datasets
    files = {
        "32nt WT": "sugar_pucker32.dat",
        "32nt B1": "sugar_pucker_B1.dat",
        "32nt B2": "sugar_pucker_B2.dat",
        "32nt M3": "sugar_pucker_M3.dat",
        "48nt WT": "sugar_pucker48.dat"
    }

    data_dict = {label: load_data(path) for label, path in files.items()}

    plot_comparison(data_dict, output_file="sugar_pucker_all_constructs.png")

if __name__ == "__main__":
    main()
