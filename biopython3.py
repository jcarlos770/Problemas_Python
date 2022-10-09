from Bio.Seq import Seq
secuencia = Seq('ATCG')

print (secuencia)
print(len(secuencia))

print(secuencia[2:3])

print(secuencia[::-1])

print(secuencia.count('AT'))

print(secuencia.complement())
print(secuencia.reverse_complement())

secuencia = Seq('ATGGCCATTGT')
secuencia2 = Seq('ATGGCCATTGT')
print(secuencia)
print(secuencia2)
print(secuencia == secuencia2)

print(str(secuencia) == str(secuencia2))

print(id(secuencia) == id(secuencia2))

print(id(secuencia))
print(id(secuencia2))
