#adding a loop inside another loop
for x in range(4):
    for y in range(3): #innerloop
        print(f'({x},{y})')

#Nested loop challange
#simplest method
numbers=[5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)

print()

#method 2 using nested loop
for x_count in numbers:
    output=''
    for count in range (x_count):
        output+='x'
    print (output)
    print()


#printing an l
for x_count in numbers:
    output=''
    for count in range (x_count):
        output+='l'
    print (output)