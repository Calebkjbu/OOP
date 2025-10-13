file1 = open("test.txt", "w")

file1.writelines("hello there")
file1.writelines("nuh uh")

file1.close()
file2 = open("test.txt", "r")
for x in file2:
    print(x)
file2.close()