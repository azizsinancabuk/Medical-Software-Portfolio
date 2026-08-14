# Medical & Bioinformatics Software Portfolio

This repository contains a collection of software projects developed for applications in medical informatics, hospital management, and bioinformatics.

## Projects Included:
1. **Hospital Triage System (`hospital_triage.cpp`)**: A C++ application utilizing priority queues to simulate patient urgency sorting in emergency departments.
2. **DNA Analyzer (`dna_analyzer.py`)**: A Python program designed for bioinformatics tasks, including DNA sequence analysis and transcription tracking.
3. **Forensic Data Management (`forensic_management.cpp`)**: A C++ system designed to structure and secure case tracking within forensic pathology workflows.
4. **DNA Letter Count (`DNA_Letter_Count.py`)**: A custom core script focused on processing specific genetic sequence occurrences.

*Developed as part of academic and practical research in biomedical software development.*


---

# DNA String Matching Algorithm

This project focuses on string matching algorithms and includes an implementation of the Naive Exact Matching algorithm in Python.

## Key Concepts Covered

- Strings and sequences
- Pattern and text analysis
- Exact matching
- Naive string matching logic
- Character comparisons
- Match positions (offsets)

## Example

Text:

AACCGAACCG

Pattern:

ACCG

Output:

[1, 6]

The pattern occurs at positions 1 and 6 in the text (using 0-based indexing).

## How It Works

The algorithm checks the pattern at every possible position in the text.
It compares the characters one by one.
If all characters match, the position is recorded.

---

# Biological Sequence Analysis with Biopython and NCBI

This project demonstrates how to use the Biopython library to work with biological sequence data. 

It utilizes the NCBI Entrez system to programmatically retrieve a DNA sequence and uses Biopython to parse and analyze the retrieved sequence.

## Key Concepts Covered

- Biopython library
- NCBI Entrez database access
- FASTA file processing
- `SeqIO` module
- DNA sequence analysis

## How It Works

The script performs the following operations:

1. Connects to the NCBI database using Entrez.
2. Retrieves a specific DNA sequence record.
3. Reads and parses the sequence using Biopython.
4. Outputs the sequence ID.
5. Outputs the total sequence length.
6. Displays the first 50 bases of the sequence.

## Example Output

ID: NM_000546

Length: ...

First 50 bases: ...

---

# DNA to Protein Translation Tool

This project provides a Python implementation for translating DNA sequences into their corresponding amino acid sequences. It demonstrates how to handle biological data using key-value mapping and string manipulation techniques.

## Key Concepts Covered

- **Python Dictionaries:** Utilizing key-value pairs for efficient codon-to-amino acid mapping.
- **String Slicing:** Processing DNA sequences in triplet chunks (codons).
- **Functions:** Modular code structure for reusability.
- **Data Handling:** Graceful error handling for undefined codons using the `.get()` method.

## How It Works

The program reads a provided DNA sequence three bases at a time. It searches for each triplet (codon) in a predefined dictionary (`CODON_TABLE`) and concatenates the resulting amino acids into a final protein string.

## Example

**Input (DNA Sequence):**
`ATGGCCATTGTA`

**Translation Process:**
* `ATG` ➔ `M`
* `GCC` ➔ `A`
* `ATT` ➔ `I`
* `GTA` ➔ `V`

**Output (Protein):**
`MAIV`

---

# DNA GC Content Calculator

This project features a Python script designed to calculate the GC (Guanine-Cytosine) content of a given DNA sequence. GC content is a fundamental metric in genomics, often used to analyze the stability of a DNA molecule.

## Key Concepts Covered

- **String Iteration:** Using `for` loops to process a DNA sequence base by base.
- **Conditional Logic:** Identifying specific nucleotides ('G' and 'C') within a sequence.
- **Mathematical Operations:** Calculating percentages based on total sequence length.
- **Bioinformatics Fundamentals:** Understanding and applying the concept of GC content algorithmically.

## How It Works

The program takes a DNA sequence as input and iterates through each character. It keeps a running count of every Guanine (G) and Cytosine (C) base. Finally, it divides this count by the total length of the sequence and multiplies by 100 to return the percentage.

## Example

**Input (DNA Sequence):**
`AGCTATCGGC`

**Calculation:**
The sequence has a total length of 10 bases. It contains 6 'G' or 'C' bases.
(6 / 10) * 100 = 60.0%

**Output:**
`GC Content: 60.0 %`