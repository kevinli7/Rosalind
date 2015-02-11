"""calculates rabbit populations after 
   n months with litter size k"""
cache = dict()
def rabbits(n, k):
	if (n<3): return 1
	if n in cache:
		return cache[n]
	temp = rabbits(n-1,k) + k*rabbits(n-2, k)
	cache[n] = temp
	return temp

filename = "rosalind_fib.txt"
lst = open(filename, 'r').read().split()
n = int(lst[0])
k = int(lst[1])

with open("Output.txt", "w") as text_file:
    print(rabbits(n,k), file=text_file)
