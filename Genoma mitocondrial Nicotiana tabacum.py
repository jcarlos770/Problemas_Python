"""Este script leerá un archivo Genbank con un genoma mitocondrial
completo (por ejemplo, la mitocondria del tabaco, Nicotiana tabacum mitochondrion NC_006581),
creará 500 registros que contienen fragmentos aleatorios de este genoma y los guardará como un archivo fasta.
Estas subsecuencias se crean utilizando puntos de partida aleatorios y una longitud fija de 200."""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from random import randint

# There should be one and only one record, the entire genome:
"""Nicotiana tabacum mitochondrion, complete genome."""
genoma_mitocondrial = SeqIO.read("sequence.gb", "genbank")

mito_frags = []
limit = len(genoma_mitocondrial.seq)
for i in range(0, 500):
    start = randint(0, limit - 200)
    end = start + 200
    mito_frag = genoma_mitocondrial.seq[start:end]
    record = SeqRecord(mito_frag, "fragment_%i" % (i + 1), "", "")
    mito_frags.append(record)
print(mito_frags[4])
SeqIO.write(mito_frags, "mitofrags.fasta", "fasta")


