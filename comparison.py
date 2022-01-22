#If temprature is greater than 30, 
# it's a hot day otherwise if it's an less than 10,
#  it's a cold day, otherwise it's neither hot or cold

temperature = 35
if temperature >30:#this is an expression-piece of code that produces a value
    print("it's a hot day")
else:
    print("it's not a hot day")

#if name is less than 3 characters long, name must be alteast 3 characters long, 
# otherwise if it's more than 50characters long, 
# name can be  a maximum of 50characters long. otherwise name looks good 
#method 1
name =56
if name <3:
    print('name must be alteast 3 characters long,')
elif name>50:
    print('name can be  a maximum of 50characters lon')
else:
    print('name looks good')

#Hurrey, Omo is a superstar python developer.
#method 2-using len to count charactors
nm="James Ouma"
if len(nm) <3:
    print('name must be alteast 3 characters long,')
elif len (nm)>50:
    print('name can be  a maximum of 50characters lon')
else:
    print('name looks good')

#Program to allow user to enter weight and covert it to 
# other unit lbs or kgs based on user input
weight=int(input('Weight:'))
unit=input('(L)bs or K(gs)')

if unit.upper() =="L":
    converted = weight * 0.45
    print(f"You are {converted} Kilos")
else: 
    converted = weight /0.45
    print(f"You are {converted} pounds")
