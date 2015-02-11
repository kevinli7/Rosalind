filename = 'rosalind_revc.txt'
s = open(filename, 'r').read()
if s[-2:] == '\n':
	s = s[:-2]
print(s)
s = s[::-1]

comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', '\n': ''}
u = ''

for char in s:
	u += comp[char]

with open("Output.txt", "w") as text_file:
    print(u, file=text_file)