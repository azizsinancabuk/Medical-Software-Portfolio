# DNA Sequence Analyzer for Bioinformatics
# Developer: Aziz Sinan Cabuk

def analyze_dna(dna_sequence):
    dna_sequence = dna_sequence.upper()
    valid_nucleotides = ['A', 'T', 'G', 'C']
    
    # Input validation
    if not all(nuc in valid_nucleotides for nuc in dna_sequence):
        return "Error: Invalid DNA sequence! It must only contain A, T, G, C."
    
    length = len(dna_sequence)
    counts = {nuc: dna_sequence.count(nuc) for nuc in valid_nucleotides}
    
    # GC Content Calculation (Crucial in bioinformatics)
    gc_content = ((counts['G'] + counts['C']) / length) * 100
    
    # Transcription (DNA -> RNA conversion)
    rna_sequence = dna_sequence.replace('T', 'U')
    
    print("--- Bioinformatics DNA Analysis Report ---")
    print(f"Sequence Length: {length} bases")
    for nuc, count in counts.items():
        print(f"{nuc} Count: {count}")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"RNA Equivalent: {rna_sequence}")
    print("------------------------------------------")

# Sample Test Data
test_dna = "ATGCGATCGATCGATCGATCGATCGATC"
analyze_dna(test_dna)