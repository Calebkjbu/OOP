##file1 = open("test.txt", "w")

##file1.writelines("hello there\n")
##file1.writelines("nuh uh")

##file1.close()
##file2 = open("test.txt", "r")
##for x in file2:
    ##print(x)
##file2.close()

import pickle
d = {"stu1": {"Name":"Caleb", "age":"21", "if": "30"},
     "stu2": {"Name": "m,eh", "age": "30", "if": "3212"}
     }

with open("myUsers.dat", "wb") as file1:
    pickle.dump(d, file1)
file1.close()

with open("myUsers.dat", "rb") as file2:
    myDict = pickle.load(file2)

i = 1

for x in myDict:
    var = "stu"+ str(i)
    print(myDict[var]["Name"])
    i +=1



