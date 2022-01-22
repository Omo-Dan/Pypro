names=['Daniel', 'Flavia', 'Irene','Rael','Agomba']
print(names)
print(names [0])
print(names [-1])
print(names [4])
print(names [2])
print(names [2: ])
print(names [2:4])
print(names [0:2])

#LARGEST NUMBER IN A LIST
num=[3,6,2,8,4,10,80, 400,67]
max = num[0]
for n in num:
    if n>max:
        max=n
print(max)