is_hot = False
is_cold=False
if is_hot:
    print("It's a hot day ")
    print('drink plenty of water')
elif is_cold:
    print("It's a cold day ")
    print("Wear warm clothes ")
else:
    print("It's a lovely day")


#Price of a house is $1M. If buyer has good credit, they need to put down 
#Otherwise they need to put down 20%. Write down a program.

price = 1000000
has_good_credit=False

if has_good_credit:
    down_payment=0.1 *price
else:
    down_payment=0.2 * price
print (f"Down Payment: {down_payment}")

