def funct1(num, strr,  *args, **kwargs):
    print("Number is num=",num)
    print(strr)
    
    for value in args:                                  #from *args we can pass list into function
        print(value)                                    #from **kwargs we can pass dictionary in the funct 

    for key, value in kwargs.items():
        print(f"Name = {key} and Age = {value}")

if __name__ == "__main__":                      #__name__ =main only if it is run from here 
    num=546987                                  #not equal to main if imported to other file
    xyz="Mayank is 19 year old"                             
    lst=[1,2,3,4,5]
    dicy={"Maynak":19, "Keertika":20, "Astha":20 }

    funct1(num,xyz,*lst,**dicy)
    