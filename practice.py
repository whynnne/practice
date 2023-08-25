import math

def triangle_area(a, b, c):
    s = (a + b + c)/ 2
    area = math.sqrt(s * (s - a) * (s -b ) * (s - c))
    return area


a = 5
b= 6
c= 7
area = triangle_area(a, b, c)
print("The area of the triangle is:", area)


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
