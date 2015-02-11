filename = 'rosalind_hamm.txt'
dna_file = open(filename, 'r')
s = dna_file.readline()
t = dna_file.readline()

count = 0

for i in range(len(s)):
	if s[i] != t[i]:
		count += 1

with open("Output.txt", "w") as text_file:
	print(str(count), file=text_file)