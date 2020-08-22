lst=[["Mayank",19],["Keertika",20],["Astha",20],["Kazim",19]]
for i,j in lst:
    print(i,"is",j,"years old")
print()

strr="Mayank"
lst=[a for a in strr if a !='a']
print(lst,"\n")

lst2=[a for a in range(0,20) if a<10]
print(lst2)
lst2.append(10)
lst2.remove(2)
print(lst2.pop(0))
lst2.insert(5,69)
print(lst2)
print(len(lst2))
lst2.sort()
print(lst2)

