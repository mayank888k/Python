for a in range(10):
    print(a,end=" ")

else:
    print("\nLoop is terminated Correctly No break encountered")

for a in range(1,10):
    print(a,end=" ")
    if(a%3==0):
        break

else:
    print("\nBreak Encountered else will not execute")