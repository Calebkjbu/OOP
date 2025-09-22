course1 = float(input("what is your Grade for your first class"))
course2 = float(input("what is your Grade for your second class"))
course3 = float(input("what is your Grade for your third class"))
course4 = float(input("what is your Grade for your fourth class"))
course5 = float(input("what is your Grade for your fifth class"))

total = course5 +  course4 +  course3 +course2 + course1

total_perc = (total/500)*100

if total_perc <100 and total_perc > 90:
    print("you currently have an A on avrage in you classes ")
elif total_perc < 90 and total_perc > 80:
    print("you currently have an B on avrage in you classes ")
elif total_perc <80 and total_perc > 70:
    print("you currently have an C on avrage in you classes ")
elif total_perc < 70 and total_perc >60:
    print("you currently have an D on avrage in you classes ")
elif total_perc < 60 and total_perc > 0:
    print("you currently have an F on avrage in you classes ")
else:
    print("something went wrong mate, if your grade is in the negaitves that is tuffffff ")

print(total_perc)
