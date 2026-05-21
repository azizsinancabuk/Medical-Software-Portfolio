
import matplotlib.pyplot as plt

dna_sequence = "ATGCGATAGCTAGCTAGCTAGCGATCGATCGATC"

A = dna_sequence.count("A")
T = dna_sequence.count("T")
G = dna_sequence.count("G")
C = dna_sequence.count("C")

plt.bar(["A", "T", "G", "C"], [A, T, G, C], color=["green", "red", "yellow", "blue"])
plt.title("DNA Nucleotide Distribution")
plt.xlabel("Nucleotide")
plt.ylabel("Count")
plt.show()
