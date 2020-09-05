try:
    print("Hello")
    #print(a)

except Exception as i:
    print(i)   #print error             #from except and else only one will execute

else:
    
    print("Else Will execute when except will not execute")     

finally:

    print("This Will Execute Always")

    
    