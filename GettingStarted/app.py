# import random
# # Variables
import time
# # I python there are 3 main primitive types :
# # -   Booleans : ALWAYS STARTS WITH UPPER CASE
# # -   Numbers
# # -   Strings


# # Boolean

# is_muslim = True
# is_elligible_to_vote = False

# # Numbers

# age = 12
# weight = 12.22

# # String

# my_name = "Victoire"
# my_Second_name = "Ansima"

# # STRINGS


# name = "John"
# message = """
# fasdfas
# afjodifa
# fads;kfadsf
# asdfklas;dfa
# sdf
# efio;kafasdpf
# """


# # print(len(message))  # length
# # print(name[0])  # element at a given index
# # print(name[0: 2])  # slicing


# # Indentation
# # In python indentation is not only for code readability but also for

# if 12 > 23:
#     print("This will never happen")


# def what_is_your_name(name):
#     print(f"my name is {name}")

# # print
# # By default print is a function that takes 2 parameters but the last one is ignored and defaults to new line


# print("I have a new line at the end!")
# print("I have space after this ", end=" -=- ")
# print("This is after the space")
# print(1234, " is a good number , but I prever ", 7)

# # Casting : changing from one data type to another one
# print(str(23))

# # unpacking : creating variables from lists or tuples

# fruits = ['apple', 'banana', 'cherry']


# # global variables and scoping
# # When we are we create a variable outside of a function or block , that varaible is globale but when we are trying to
# # create one which is variable within a function we need to use the global key word

# def has_a_global():
#     global var
#     var = 'something sweet'


# has_a_global()
# print(var)


# # DataTypes
# # In pytnon these are the existing data types :
# # - Text types (str)
# # - Numeric Types (int , float , complex)
# # - Sequence types (list , tuple , range)
# # - Mapping type (dict)
# # - Set tupes (set  , frozenset)
# # - Booleans Type (bool)
# # - Binary Types (bytes, butearray , memoryview)
# # - None Type (NoneType)


# # U get the the data type of any object by using the type function type(value)

# # NUMBERS :
# # There are three numeric types in python where : int , float and complex
# x = 1
# y = 2.8
# z = "1j"

# print(type(x))
# print(type(y))
# print(type(z))

# # you can convert from one number type to another one

# print(complex(x))
# print(random.randint(1, 5))

# # STRINGS :

# field = "computer science"

# # checking the length of a string

# print(len(field))

# # Strings are array so we can iterate through them using the for loop

# for letter in field:
#     print(letter)


# # Checking for a given character in a string

# if "computer" in field:
#     print("YES COMPUTER")

# if "mavi" not in field:
#     print("NO MAVI")

# # accessing a character at a given position

# print(field[2])


# # Slicing a string
# # U do this by specifying a range using a semicolon between start and end index

# # welcome = "Welcome to amaliTech"
# # print(welcome[0:3])
# # print(welcome[-2: -1])

# # stings have a lot of methods to look into the documentation

# # string formating

# # F-string was introduced in python 3.6 and is now the default way of formating strings in python
# price = 59
# text = f"The price is {price:.2f} dollars"
# print(text)

# # BOOLEAN
# # Most values are t in ruthy python exept , zero and empty containers

# # Operators in python
# # Python devides operators into the following types :
# # Arithmetic , Assignment , Comparison , Logical , Identity , Membership , Bitwise

# # Assignment operator :
# x = 21


# print(x // 2)
# print(2 & 2)


# print(~12)


# # walrus operator


# # def count_odds(data):
# #     time.sleep(1)
# #     odds = [o for o in data if o % 2 == 1]
# #     return (len(odds))


# # # data = [45, 65, 22, 12, 54, 1, 0, 17]

# # # t1 = time.time()  # present time

# # # if (n := count_odds(data)) > 1:
# # #     print(f'{n} odds')

# # # t2 = time.time()
# # # print(f'Took {t2-t1} seconds.')


# # # num = 6

# # # x = 'WEEKEND' if num > 5 else 'Workday'

# # # print(x)

# # # parentheses has the highest precendence
# # # multiplication
# # #

# # # LISTS IN PYTHON

# # days = list(('apple', 'banana', 'cherry'))
# # print(days)
# # days[0:1] = ['victor']
# # print(days)


# # days.insert(1, 'butamu')
# # print(days)

# # days.append("volvo")
# # print(days)

# # family_x = [1, 2, 34, 5, 6, 7, 8, 9]
# # family_y = [10, 20, 30, 40]


# # family_x.extend(family_y)
# # print(family_x)

# # family_x.remove(34)
# # print(family_x)

# # family_x.pop(3)
# # print(family_x)

# # family_y.clear()
# # del(family_y)

# # # print(family_y)


# # # Looping through lists in python 

# # for x in family_x : 
# #     x -= x
# #     print(x)


# # for i in range(len(family_x)):
# #     print(i)

# # i = 0
# # while i < len(family_x):
# #     print(family_x[i])
# #     i = i + 1

# # # list comprehension 

# # [print(f"listComprehension chapter {x}") for x in family_x]

# # # List comprehension can also make you create lists based on other existing lists

# # days = ['monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday']

# # odd_positioned = [x for x in days if len(x) == 6]

# # print(odd_positioned)


# # LISTS in python 

# this_list = ['apples' , 'hembe' , 'mango' ,'butamu']

# another_list = this_list.copy()

# another_other_list = list(another_list)

# yet_another_list = another_other_list[:]

# # Joining two list

# # method one  : 

# l1 = [1,2,3,4,5,6] 
# l2 = ['1', 'a']

# l3 = l1 + l2

# # method two

# for item in l1 :
#     l2.append(item)

# print(l2)


# # method 3

# l5 = l1.extend([23, 2300])
# print(l5)

# # TUPLES

# names = 'ansima' , 'ikuliyo' , 'victoire'

# print(names[2])


# fruits = 'apples' , 'banana' , 'cherry' , 'strawberry' , 'raspberry'

# (green , *yellow , red) = fruits

# print(yellow);

# my_tuple = fruits * 2;
# print(my_tuple)


# SETS in python 

this_set = {1, 2, 3}
this_set.update({12})
print(this_set)

# Frozenset

my_names = frozenset({'Ansima' , 'Ikuliyo' , 'Victoire'})

my_flex_names = my_names.copy()
union = my_flex_names.union({"Tupac man"});

print(my_flex_names)
print(union)



