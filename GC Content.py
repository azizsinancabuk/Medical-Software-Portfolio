def gc_content(dna):
    gc = 0

    for base in dna:
        if base == "G" or base == "C":
            gc += 1

    return (gc / len(dna)) * 100


dna = "AGCTATCGGC"

result = gc_content(dna)

print("DNA:", dna)
print("GC Content:", result, "%")