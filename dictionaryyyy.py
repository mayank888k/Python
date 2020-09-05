lst=[["Mayank",19],["Keertika",20],["Astha",20],["Kazim",19]]
name=["Mayank","Keetika","Astha","Kazim"]
age=[19,20,20,19]

dicy={"Mayank":3,"Aryan":3,"Riya":2, "Dad":5}
dicy2=dict(lst)
dicy2["Astha"]={"Real":20,"Fake":19}
dicy3={a:b for a,b in lst }

for a,b in dicy3.items():
    print(a,"is",b,"Years Old\n")

del dicy2["Kazim"]
print(dicy2)