filename = 'rosalind_perm.txt'
s = open(filename, 'r').read()
n = int(s)

def generate_perms(n):
	lst = []
	if n == 1:
		return [[1]]
	lst2 = generate_perms(n-1)
	for item in lst2:
		for i in range(len(item)+1):
			lst.append(item[:i]+[n]+item[i:])
	return lst

lst = generate_perms(n)
u = str(len(lst)) + "\n"
for item in lst:
	for number in item:
		u += str(number) + ' '
	u += '\n'

