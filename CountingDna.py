filename = 'rosalind_dna.txt'
lst = open(filename, 'r').read()


nuc_count = dict()
for s in list(lst):
	if s in nuc_count:
		nuc_count[s] += 1
	else:
		nuc_count[s] = 1
	

for key in nuc_count:
	if key != "\n":
		print(key)
		print(nuc_count[key])