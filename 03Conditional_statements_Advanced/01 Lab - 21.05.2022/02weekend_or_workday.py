day = input()
# day = ["Monday" ,"Tuesday","Wednesday","Thursday","Friday"]
if day == "Monday" or \
        day == "Tuesday" or \
        day == "Wednesday" or \
        day == "Thursday" or \
        day == "Friday":
    print("Working day")
elif day == "Sunday" or \
        day == "Saturday":
    print("Weekend")
else:
    print("Error")
