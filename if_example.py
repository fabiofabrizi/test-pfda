# Import the below so that we can work with dates and times.
import datetime

# Check if it's Tuesday
print("Check if it's Tuesday!")

# datetime has a data structure called datetime, and inside that 
# data structure there's another data structure called today(). 
# All this is stored in a variable called today
# So package (datetime) datastructure (datetime) datastructure (today())
today = datetime.datetime.today()

dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("It's Tuesday")
elif dayOfWeek == 2:
    print("It's Wednesday")
else:
    (print("It's not Tuesday or Wednesday"))
