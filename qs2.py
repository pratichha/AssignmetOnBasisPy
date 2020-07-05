#if statement to determine whether a variable holding a year is a leap year.
def is_prime(year):
    if year % 4 == 0 and  year % 100 != 0:
        print("leap2 year")
    elif year % 100 == 0:
        print("Not leap year")     
    elif year % 400 == 0:
        print("leap year")     
    else:
        print("Not leap year")
year = int(input("Enter a year:"))
is_prime(year)  