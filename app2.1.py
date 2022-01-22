from dataclasses import replace
from email import message


course='Python for superstars'
print(course[0])
print(course[1-3])
print(course[0:6])
print(course[0:])
print(course[6:])
print(course[:7])
another=course[:]
print(another)
name='Jannifer'
print(name[1:-1])

#Formatted Strings
first='John'
last='Smith'
#print john [smith] is a coder.
message=first+'['+last +'] is a coder'
print(message)
#Example of formated string f
msg=f'{first} [{last}] is a coder'
print(msg)

#String methods #len
print(len(course)) #len is a general term 

#other methods
print(course.upper()) #string method for uppercase
print(course.lower()) #string method for lowercase
print (course)
#find method
print(course.find('P'))
print(course.find('B'))
print(course.find('s'))
print(course.find('superstars'))

#replace method
print(course.replace('superstars', 'experts'))
print(course.replace('P', 'J'))

#in operator-which is a boolean
print('Python' in course)
print('superstars' in course)
print('Hello' in course)
print('Superstars' in course)

#Strings recap
#len() count number of characters in a string
#methods(.upper(), .lower() .title(), .find(), .replace(), .... in )

