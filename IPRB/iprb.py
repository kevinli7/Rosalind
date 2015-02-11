filename = "rosalind_iprb.txt"
s = open(filename, 'r').read().split()
for i in range(len(s)):
	s[i] = int(s[i])

def iprb(k,m,n):
	population = k + m + n
	#Case of double homozygous recessive 
	negative = (n/population)*((n-1)/(population-1))	
	#Hetero + homozygous recessive
	heteroneg = (n/population)*(m/(population-1))*(.5) + (n/(population-1))*(m/population)*(.5)
	#Hetero with Hetero
	hetero = (m/population)*((m-1)/(population-1))*(1/4)
	return 1 - (negative + hetero + heteroneg)

u = iprb(s[0],s[1],s[2])
with open("Output.txt", "w") as text_file:
    print(u, file=text_file)