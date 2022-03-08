
print('Part 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['steak', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
for i in range(len(meats)):
    meats[i] = meats[i].capitalize()

for i in range(len(cheeses)):
    cheeses[i] = cheeses[i].capitalize()

print(meats)
print(cheeses)

print('Part 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []

for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}')

print(sandwiches)

print()

print('Part 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'

for sandwich in sandwiches:
    order = input('What is your order?: ')
    if order.capitalize() == sandwich:
        print(f'Great choice! 1 {order} coming right up!')
    else:
        print("Sorry, that's not on the menu!")
        
