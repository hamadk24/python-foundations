from datetime import datetime


def check_birthdate(year, month, day):
	input_date = datetime(born_year, born_month, born_day)
	if input_date < datetime.today():
		return True
	else:
		return False

def calculate_age(year, month, day):
	input_date = datetime(born_year, born_month, born_day)
	difference = datetime.today()-input_date
	difference_in_days = difference.days
	print(int(difference_in_days/365))

born_year = int(input("Enter year of birth: "))
born_month = int(input("Enter month of birth: "))
born_day = int(input("Enter day of birth: "))

if check_birthdate(born_year, born_month, born_day):
	calculate_age(born_year, born_month, born_day)
else:
	print("Birthdate is invalid")