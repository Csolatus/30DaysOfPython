#Day 2: 30 Days of Python programming
import math
first_name = 'lucas'
last_name = 'lanoue'
full_name = 'lucas' + 'lanoue'
country = 'France'
city = 'Paris'
age = 20
year = 2025
is_married = False
is_true = True
is_light_on = True
first_name, last_name, country, city, age = 'Lucas', 'Lanoue', 'France', 'Paris', 20

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = num_one ** num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

radius = 30
area_of_circle = math.pi*radius**2
print(area_of_circle)

circum_of_circle = area_of_circle / math.pi
print(circum_of_circle)

input('Donnez votre nom : ')
input('Donnez votre prénom : ')
input('Donnez votre pays : ')
input('Donnez votre age : ')


