filename = 'rosalind_rna.txt'
s = open(filename, 'r').read()
if s[-2:] == '\n':
	s = s[:-2]

u = ''
for char in s:
	if char == 'T':
		u += 'U'
	else:
		u += char

with open("Output.txt", "w") as text_file:
    print(u, file=text_file)