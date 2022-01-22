#Ask year we were born and calculates age
by = input('Year of birth: ')
#age = 2022 - 'by'
#we have to covert string(year of birth into integer)#
age=2022 - int(by)
print(age)
#using keyword type to show type of integer
print(type(by))
print(type(age))
#Ask user to input their weight, (in pounds),
#convert it into kilograms and print it on the terminal
w=input('Enter your wieght in pounds(lbs): ')
kgs= 0.45 * int (w)
print(kgs)
