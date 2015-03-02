AMINO_ACIDS = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

posmRNA = dict()
for key in AMINO_ACIDS:
    if AMINO_ACIDS[key] not in posmRNA:
        posmRNA[AMINO_ACIDS[key]] = 1
    else:
        posmRNA[AMINO_ACIDS[key]] += 1

def prot_to_possible(aa_seq):
    count = 3
    for aa in aa_seq:
        count *= posmRNA[aa]
        count = count % 1000000
    return count


filename = "rosalind_mrna.txt"
s = open(filename, 'r').read()

if s[-1:] == '\n':
    s = s[:-1]


u = prot_to_possible(s)

with open("Output.txt", "w") as text_file:
    print(u, file=text_file)