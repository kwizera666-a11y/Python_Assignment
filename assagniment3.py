#User will read marks in range 0 to 100
"""
Then w'll check if the marks entered is in valid range(0 - 100)
instead of checking for each line. This 'll make code easier and
more reable..
"""
marks = int(input("Enter the marks(0-100): "))
if marks < 0 or marks >100: 
    print("Invalid marks!!")
elif marks > 85:
    print("Grade A..")
elif marks > 60:
    print("Grade B+")
elif marks > 40:
    print("Grade C")
else:
    print("Failed..")