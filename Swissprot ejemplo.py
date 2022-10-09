from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from random import randint

# There should be one and only one record, the entire genome:
mito_record = SeqIO.read("sequence.gb", "genbank")

mito_frags = []
limit = len(mito_record.seq)
for i in range(0, 500):
    start = randint(0, limit - 200)
    end = start + 200
    mito_frag = mito_record.seq[start:end]
    record = SeqRecord(mito_frag, "fragment_%i" % (i + 1), "", "")
    mito_frags.append(record)
print(mito_frags)
SeqIO.write(mito_frags, "mitofrags.fasta", "fasta")


