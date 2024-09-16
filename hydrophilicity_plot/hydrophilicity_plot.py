import subprocess
import importlib
import os
import re
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def run():
    print("Hydrophilicity Plot: Kyte-Doolittle Analysis Tool v0.5")
    print(" ")


def check_biopython():
    try:
        importlib.import_module("Bio")
        print("Biopython is already installed.")
    except ImportError:
        install_biopython()


def check_matplotlib():
    try:
        importlib.import_module("matplotlib")
        print("Matplotlib is already installed.")
    except ImportError:
        install_matplotlib()


def install_biopython():
    user_input = input("Biopython is not installed. Do you want to install it? (Y/N): ").strip().lower()
    if user_input == 'y':
        print("Installing Biopython...")
        subprocess.run([sys.executable, "-m", "pip", "install", "biopython"], check=True)
        print("Biopython installation complete.")
    else:
        print("Biopython installation skipped.")
        sys.exit()


def install_matplotlib():
    user_input = input("Matplotlib is not installed. Do you want to install it? (Y/N): ").strip().lower()
    if user_input == 'y':
        print("Installing Matplotlib...")
        subprocess.run([sys.executable, "-m", "pip", "install", "matplotlib"], check=True)
        print("Matplotlib installation complete.")
    else:
        print("Matplotlib installation skipped.")
        sys.exit()


def parse_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences[record.id] = str(record.seq)
    return sequences


def calculate_kyte_doolittle(sequence, window_size=9):
    hydropathy_values = {
        'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
        'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
        'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
        'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
    }

    scores = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        score = sum(hydropathy_values.get(aa, 0) for aa in window) / window_size
        scores.append(score)
    return scores


def plot_hydropathy(sequences):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib is not installed. Exiting.")
        sys.exit()

    for header, sequence in sequences.items():
        scores = calculate_kyte_doolittle(sequence)
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(scores) + 1), scores, color='b')
        plt.title(f'Hydropathy Plot for {header}')
        plt.xlabel('Amino Acid Position')
        plt.ylabel('Hydropathy Score')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.show()


def main():
    check_biopython()
    check_matplotlib()

    print("Enter the path to the FASTA file:")
    fasta_path = input().strip()

    if not os.path.exists(fasta_path):
        print("File not found. Exiting.")
        sys.exit()

    sequences = parse_fasta(fasta_path)
    plot_hydropathy(sequences)


if __name__ == "__main__":
    main()

