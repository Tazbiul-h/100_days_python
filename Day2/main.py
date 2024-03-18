print("Welcome to the tip Calculator.")
total_bill = float(input("What is the total bill?\n"+"$"))
number_of_people = int(input("How many people to split the bill?\n"))
tip_percent = 0
while tip_percent not in [10, 12,15]:
    tip_percent = float(input("What percent of tip would you like to give? 10, 12, 15?\n"))
    if tip_percent not in [10, 12, 15]:
        print("Please select 10, 12 or 15")

if tip_percent == 10:
    new_bill = total_bill + total_bill * 0.10
elif tip_percent == 12:
    new_bill = total_bill + total_bill * 0.12
elif tip_percent == 15:
    new_bill = total_bill + total_bill * 0.15


print("Each person should pay: ")

bill_after_split = new_bill / number_of_people
print("$" + str(bill_after_split))
