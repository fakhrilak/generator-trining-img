import os
listimage = os.listdir("from/")
typepath = ""

if os.name == "nt":
    typepath = "\\"
elif os.name == "posix":
    typepath = "/"
    

for count, filename in  enumerate(listimage):
    os.system("move from"+typepath+filename+" from"+typepath+str(count)+".png")