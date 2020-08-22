fhandle=open("sample2.txt","w")
fhandle.write("Mayank is a good boy\n")
fhandle.close()

with open("sample2.txt","a") as f:                      #No need to close file with "WITH"
    f.write("Mayank is persuing Btech in Galgotias\n")

