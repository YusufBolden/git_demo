# Review

# primitive data types (integer, float, boolean)
# logical operators (and, or, !, <, >, <=, >=)
# conditional statements (if, elif, else)
# input() - used to take input from the user

# Tonight we will cover the first type of data structure : Lists

# what is a list
our_list = [] # this is an empty list

our_list = [42, 'apples', True]
print(our_list)
print(type(our_list))

# storing data in a list

groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)


# what kind of data can be stored in a list
int_list = [1, 4, -7]
float_list = [12.4, 5.8, 2.9, 55.6]
boolean_list = [True, True, False, True, True, False]
print(int_list)
print(float_list)
print(boolean_list)

mixed_list = [int_list, float_list, boolean_list] # this is called a list of lists
print(mixed_list)
print(type(mixed_list))


# how to add/remove elements from a list
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)

# append() - like an appendix, this will add an element to the end of the list
groceries.append('bread')
groceries.append('milk')
print(groceries)

# remove()
groceries.remove('eggs') # this will remove eggs from the list
print(groceries)

# how to find the number of elements of a list
# len() - used to find the number of elements of the list

print(len(groceries)) # this will return an integer

# list element vs. list index
# list element is an item within a list
# each list element has a location identifier within that list - list index
# the first element of list is index 0

groceries = ['apples', 'eggs', 'pasta', 'carrots'] # indexes 0-3
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[3])
# print(groceries[4]) will return an error because there is no list element at index 4
print(groceries[-1])
print(groceries[-2])
print(groceries[-3])
# print(groceries[-4]) will return an error because there is no list element at index -4

# index() - can display the index of a specific list element
# this will come in handy for the box_office_challenge
# try using print(remaining_50_list.index('Matrix')) before and after removing it

print(groceries.index('eggs')) # this will display the index number where eggs exists
print(groceries,index('carrots')) # this will display the index number where carrots exists
print(groceries,index('grapes')) # this will display an error because grapes is not an element of the groceries list

# slicing 

num_list = [1, 3, 4, 6, 4, 5, 9, 0, 5, 3, 4]
print(len(num_list))

print(num_list[2:len(num_list)]) # this will print from index 2 up to but not including index 7

groceries = ['apples', 'eggs', 'pasta', 'carrots', 'bananas', 'popcorn', 'oranges'] # this is a list of strings
print(groceries[2:4])
print(type(groceries))

# splitting a string with split()

my_string = 'row, row, row, your boat, gently down the stream' # this is a single string
print(my_string)
print(type(my_string))
# split the string by the commas
# 'row', 'row', 'row' , etc

my_split_str = my_string.split(',')
print(my_split_str) # this will convert the single string to a list of strings
print(type(my_split_str))

# join() method
groceries = ['apples', 'eggs', 'pasta', 'carrots', 'bananas', 'popcorn', 'oranges'] # this is a list of strings
print(groceries)

food = ', '.join(groceries) # this takes a list of strings and converts to a single string
print(food)
print(type(food))


