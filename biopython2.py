import Bio
from Bio.Seq import Seq
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
Sec=Seq("ATCG")
print(Sec)
print(Sec.reverse_complement())
print(Sec.complement())
Sec2=Seq("ATGGCCATTGT")
print(Sec2.translate())
Sec3=Seq("ATGGCCATTGT")
Sec4=Seq("ATGGCCATTGT")
print(SequenceMatcher(None, Sec3, Sec4).ratio())