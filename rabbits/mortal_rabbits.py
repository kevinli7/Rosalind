"""calculates rabbit populations after 
   n months with litter size k"""
cache = dict()
def rabbits(n, m):
	if (n<3): return 1
	if n in cache:
		return cache[n]
	temp = rabbits(n-1,m) + rabbits(n-2, m)
	if not n-m < 1:
		temp -= rabbits(n-(m+1),m)
	cache[n] = temp
	return temp

filename = "rosalind_fibd.txt"
lst = open(filename, 'r').read().split()
n = int(lst[0])
k = int(lst[1])

with open("OutputD.txt", "w") as text_file:
    print(rabbits(n,k), file=text_file)
