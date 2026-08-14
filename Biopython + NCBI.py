from Bio import Entrez, SeqIO

Entrez.email = "email@example.com"

handle = Entrez.efetch(
    db="nuccore",
    id="NM_000546",
    rettype="fasta",
    retmode="text"
)

record = SeqIO.read(handle, "fasta")
handle.close()

print("ID:", record.id)
print("Length:", len(record.seq))
print("First 50 bases:", record.seq[:50])