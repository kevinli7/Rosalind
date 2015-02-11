filename = 'rosalind_gc.txt'
s = open(filename, 'r')
contents_lib = dict()
next_name = s.readline()
while True:
	try:
		name = next_name
		strand = ''
		still_DNA = True
		while still_DNA:
			temp = s.readline()
			if temp == '': break
			if temp[0] == '>':
				next_name = temp
				still_DNA = False
			else:
				strand += temp	
		GC = 0
		AT = 0
		for nuc in strand:
			if (nuc == "G" or nuc == "C"):
				GC += 1
			elif (nuc == "A" or nuc == "T"):
				AT += 1
		if (AT+GC) == 0: break
		contents_lib[name] = GC/(AT+GC)*100
	except EOFError:
		break

name = ""
greatest = 0
for key in contents_lib:
	if contents_lib[key] > greatest:
		name = key
		greatest = contents_lib[key]

with open("Output.txt", "w") as text_file:
	print(name[1:] + str(greatest), file=text_file)