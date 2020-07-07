#s = sum([n**2 for n in range(10**6)])
#s = sum(n**2 for n in range(10**6))
#s = sum([n**2 for n in range(10**8)]) #list with hundred million numbers: bad idea
s = sum(n**2 for n in range(10**8)) #not is a list

print(s)