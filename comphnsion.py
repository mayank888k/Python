lst=[[a,b] for a in range(1,10) for b in range(11,20) ]  #list comprehension with two nested loops
lst1=[e for e in range(31) if e%3==0]     
print("\n")
print(lst,"\n")
print(lst1,"\n")

dict1={k:f"Item No {k}" for k in range(1,10)}    #dictionary comprehension
print(dict1,"\n")

dict2={v:k for k,v in dict1.items()}  #reversing key value pair using dict comprehension
print(dict2,"\n")

sett={a for a in [1,1,1,1,2,2,2,3,3,3,3,4,5,6,7,7,8,9,9,10]} #set comprehension only braces are changed
print(sett)