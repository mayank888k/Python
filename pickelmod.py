import pickle

lst=[[1,"Mk"],[2,"RK"]]
print(lst)

f=open("picketlst.py","wb")        
pickle.dump(lst,f)              #to preserve data(lst, can be dict) in a file (f)
f.close()

f=open("picketlst.py","rb")
newlst=pickle.load(f)          #to get data from file

print(newlst)