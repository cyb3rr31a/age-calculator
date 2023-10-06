from datetime import date

def calculate_age(birth_year):
    today = date.today()
    age = today.year - birth_year
    months = today.month - birth_month
    days = today.day - birth_day
    
    if months < 0 or (months == 0 and days < 0):
        age -= 1
    if today.month < birth_month:
        months = 12 - birth_month + today.month
    else:
        months = today.month - birth_month
    if today.day < birth_day:
        days = 31 - birth_day + today.day
    else:
        days = today.day - birth_day
    return age, months, days

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

age, months, days = calculate_age(birth_year)

print("Your age is:", age, "years,", months, "months and", days, "days.")
