# Variables

# I python there are 3 main primitive types :
# -   Booleans : ALWAYS STARTS WITH UPPER CASE
# -   Numbers
# -   Strings


# Boolean

is_muslim = True
is_elligible_to_vote = False

# Numbers

age = 12
weight = 12.22

# String

my_name = "Victoire"
my_Second_name = "Ansima"

# STRINGS


name = "John"
message = """
fasdfas
afjodifa
fads;kfadsf
asdfklas;dfa
sdf
efio;kafasdpf
"""


# print(len(message))  # length
# print(name[0])  # element at a given index
# print(name[0: 2])  # slicing


# Indentation 
# In python indentation is not only for code readability but also for 

if 12 > 23 :
    print("This will never happen")

def what_is_your_name(name):
    print(f"my name is {name}");

#print 
#By default print is a function that takes 2 parameters but the last one is ignored and defaults to new line 

print("I have a new line at the end!")
print("I have space after this " , end = " -=- ")
print("This is after the space")
print(1234, " is a good number , but I prever ", 7)

# Casting : changing from one data type to another one 
print(str(23))

#unpacking : creating variables from lists or tuples

fruits = ['apple', 'banana' , 'cherry']
x, y , z = fruits ;
print(x);


#global variables and scoping 
#When we are we create a variable outside of a function or block , that varaible is globale but when we are trying to 
# create one which is variable within a function we need to use the global key word 

def has_a_global():
    global var;
    var = 'something sweet'
has_a_global();
print(var)

