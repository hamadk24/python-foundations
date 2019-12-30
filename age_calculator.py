from datetime import date

born_year = input("Enter year of birth: ")
born_month = input("Enter month of birth: ")
born_day = input("Enter day of birth: ")

def check_birthdate(year, month, day):
	if check_birthdate < date.today():
		return True
	else:
		return False

def calculate_age(year, month, day):
	print ("You are {date.today() - (year + month + day)} years old.").format(year)


if check_birthdate(born_year, born_month, born_day):
	calculate_age(born_year, born_month, born_day)
else:
	print("Birthdate is invalid")