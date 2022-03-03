'''
Today we'll learn about nested data in python. By the end of the lesson, you'll be able to:

    Work with lists inside dictionaries
    Work with dictionaries inside dictionaries
    Work with dictionaries inside lists
    Work with lists inside lists


Nesting, revisited...

Last time we talked about nesting with loops and logic -- now we'll be dealing with situations where the data are nested! We'll be going through examples of this with both lists and dictionaries.

'''

# Lists inside dictionaries

'''
You've actually seen this one before in the restaurants challenge, although we didn't talk about it too much!

Lists can be stored as values inside dictionaries, and referenced using keys just as with ever piece of data in a dictionary.

'''

# For example, we could have a shopping cart with lists for different categories of foods:

cart = {'fruits': ['mangos', 'apples', 'oranges'],
        'vegetables': ['kale', 'okra'],
        'grains': ['wild rice', 'quinoa'],
        'other': ['olive oil', 'black pepper'],
        'total': 24.76}

# '''
# So in this example, every value in this dictionary is a list, except for total, which is a float. Lists that are inside the dictionary are still formatted as lists.
# '''

# # Accessing lists within dictionaries:

veggies = cart['vegetables']
print(veggies)
print(type(veggies))


# # Adding to the list

cart['vegetables'].append('bell pepper')
print(veggies)


# # Specific list indices from a list nested in a dictionary

# # So, if we wanted to get the first item in fruits inside our cart
# # Bracket indexing

print(cart['fruits'][0])

# # This second set of hard brackets might be confusing, but let's break it down:

# cart['fruits'] is a list
print(type('fruits'))

# # Since cart['fruits'] is a list, we can then do cart['fruits'][0] to get the first element of said list

cart['fruits'][0] = 'papayas'
print(cart['fruits'])


# # Looping through lists inside dictionaries

for food in cart['vegetables']:
    print(food)


# # Dictionaries inside dictionaries

# # Let's see an example of some restaurants as a nested dictionary:

restaurants = {'El Basurero': {'address': '32-17 Steinway St, Queens, NY 11103',
                              'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'},
              'SriPraPhai': {'address': '64-13 39th Ave, Woodside, NY 11377',
                             'menu_url': 'https://sripraphai.com/menu.html'}
}

# # So, if we wanted to add one more restaurant to this dictionary of restaurants, we could do something like this:



restaurants['Joes Pizza'] = {'address': '7 Carmine St, New York, NY 10014',
                             'phone': '212-366-1182'}
print(restaurants)


# # Adding key-value pairs to an inner dictionary

# # dict = {key: value}
#         # {key: {key:value}}

restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com'
print(restaurants['Joes Pizza'])

# # Why 2 sets of hard brackets here?


# # Updating / removing inner dictionary key-value pairs


# # Update the menu_url

# # dict = {key: value}
#         # {key: {key:value}}


restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com/menu.php'
print(restaurants['Joes Pizza'])

# Remove phone number
restaurants['Joes Pizza'].pop('phone')
print(restaurants['Joes Pizza'])


print(restaurants)


# Dictionaries inside lists

this_dict = [{}, {}, {}]
print(this_dict)


# Let's see this in action when we make a list of dictionaries containing user accounts for a website:

users = [{'username': 'lillie', 'password': 'ilovepython', 'last_login': '2/28/2022'},
         {'username': 'ash', 'password': 'ilovedictionaries'},
         {'username': 'yusuf', 'password': 'ilovedjango', 'last_login': '3/1/2022'},
         {'username': 'paul', 'password': 'ilovegit'}]

print(users)
print(type(users))

# Acccesing items in dictionaries inside a list
# Getting a whole dictionary

# to print out the dictionary where `username` is 'yusuf'
print(users[2])


# We can add more dictionaries to this list using the append() command -- we can put the whole dictionary inside the append command

users.append({'username': 'aeshna', 'password': 'ilovesublimetxt'})
print(users)


# Accessing key-value pairs from a dictionary inside a list

# If we want a specific key-value pair from a dictionary inside a list, however, we can reference the key inside that dictionary:

# So, if we want the 'username' associated with the second item in users, we can do:

# list[dict_name[i][key]] 
print(users[1]['password'])


# We can also add, update, and remove these key-value pairs from the dictionary within the list:

#add a new key-value pair
users[2]['verified_account'] = True
print(users[2])

# update a key-value pair
users[2]['password'] = 'iloveprogramming'
print(users[2])


# remove a key-value pair
users[2].pop('password')
print(users[2])

# print users[2] to check the changes
print(users[2])


# Because we have a list full of users, we can loop through each user:

for user in users:
    print(user)


# Accessing data within each dictionary in a loop

# Let's say we wanted to loop through our users list and pull out just the usernames:

for user in users:
    print(user['password'])

# Manipulating string output to make all uppercase 

# name = 'Lillie'
# print(name.upper())

for user in users:
    user['username'] = user['username'].upper()
    print(user)


# What happens when all dictionaries don't have the same keys

# Let's way we were trying to access the last_login of each user. It turns out only the first user (ASH) has this information now, so let's see what happens if we try to print this out for everyone:

for user in users:
    print(user['last_login'])


# Lists inside lists

# Let's redo our shopping cart using this data structure:

shopping_list = [['mangos', 'apples', 'oranges'], ['carrots', 'broccoli', 'lettuce'], ['corn flakes', 'oatmeal']]

# list --> list_index --> list_element

# So, we have hard brackets within hard brackets to indicate that each list is inside another list.


# Accessing inner lists & sublists

# For example:

print(shopping_list[0][1])


# add an item to the first inside list
shopping_list[0].append('grapes')
print(shopping_list[0])

# add an item to the last inside list
shopping_list[-1].append('eggs')
print(shopping_list[-1])

# update an item in the 2nd inside list
print(shopping_list[1])
shopping_list[1][0] = 'baby carrots'
print(shopping_list[1])
print(shopping_list[0][2])

# remove an item from the 2nd inside list
shopping_list[1].remove('broccoli')
print(shopping_list)


# Nested loops with nested lists

# Since we can loop through any list, we can set up nested loops to iterate through each item in each inner list

for food_group in shopping_list:
    for food in food_group:
        print(f'I plan to buy some {food}')


# Adding a counter

# So we can see all of the foods across all the nested lists. Now, maybe we want to add a counter to see how many different items we are buying total, or to number our items. Here's one way to do this:

counter = 1
for food_group in shopping_list:
    for food in food_group:
        print(f'Item #{counter}: {food}')
        # this line means to add 1 to the counter variable
        counter+=1


# Looping through nested lists + logic

# We can add logical statements in here too. Let's say we only want to add the foods to our list if they contain the letter 'o'.

counter = 1
for food_group in shopping_list:
    for food in food_group:
        # Only print and advance the counter if food contains an o
        if 'p' in food:
            print(f'Item #{counter}: {food}')
            # this line means to add 1 to the counter variable
            counter+=1


nest_a_lot = [[[1,2,3], ['a', 'b', 'c']], [[True, False, True], [{'name':'paul'}, 2.7, 'apples']]]

# loop through the 3 levels of nested lists and print out each individual item!

for i in nest_a_lot:
    for j in i:
        for k in j:
            print(k)


# Overview of what we learned today

# We've gone over some very complex data structures with nested data today. Lots of stuff, but this will allow for a ton of useful applications moving forward. We're really putting pieces together now -- we will be taking plenty of time to review this stuff, and apply it in many settings.

# We learned about:

#     Dictionaries with nested lists inside
#     Dictionaries with nested dictionaries inside
#     Lists with nested dictionaries inside
#     Lists with nested lists inside
