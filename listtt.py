fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line=line.rstrip()
	ab=line.split()
	for at in ab :
		if at in lst:
			continue
		else:
			lst.append(at)
lst.sort()
print(lst)
