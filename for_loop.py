#for loop Used to iterate over all items in a collection
for item in 'Python':
    print(item)
    print()

for fruits in ['Apple', 'Mango', 'Orange', 'Pome']:
      print(fruits)

for n in [1,2,3,4,5,6,7]:
      print(n)
      print()

#range
for nm in range(10):
    print(nm)
    print()

for num in range(5,10):
    print(num)
    print()

for r in range(5,10,2 ):
    print(r)

#write a loop program to calculate the price below
prices = [10, 20, 30]

total=0
for price in prices:
    total +=price
print(f"Total: {total}")
     
