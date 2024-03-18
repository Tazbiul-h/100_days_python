# two_digit_number = input("Type a two digit number: ")
# digit_one = int(two_digit_number[0])
# digit_two = int(two_digit_number[1])
# total = digit_one+digit_two
# print(total)

# # challange 2
#
# height = float(input("Enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = weight/height**2
# bmi = int(bmi)
# print("Your BMI is: " + str(bmi))

# challange 3
age = input("What is your current age? ")
age_in_int = int(age)
age_in_months = age_in_int * 12
age_in_weeks = age_in_int * 52
age_in_days = age_in_int * 365

remaining_years = int(90-age_in_int)
remaining_months = int(90*12-age_in_months)
remaining_weeks = int(90*52 - age_in_weeks)
remaining_days = int(90*365 - age_in_days)

print(f'You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left')


