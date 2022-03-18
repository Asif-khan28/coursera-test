# 1) python groups types according to "how you can use them". 
#    Eg Mutable or immutable(you cannot change an object, once created ).
# 2) Collection types: Sequences 
# 3) Some Python data types are callable. That means you can use the type name like a function to produce a new instance of the type.
#    If no value is given, a default value is returned. 

## Numeric, booleam , None types and collection_types
from dataclasses import replace
from locale import format_string
from tkinter import N


def fun1():
    result = 5 + 2
    hex_string = "AB34"
    int_rep = int (hex_string,16)
    print (result, int_rep)

fun1()
###### 2
# bool: and, or, not
print(bool()) # yields False, becasue default
#truth-like values
print(bool(1))
print(int(bool(0.0)))

####### 3
# None type: represents null object
# one and only one None_object in python_Env
# None is default_return_value of python_func
aVaraible = 2 
aVaraible is None
###### 4
# Collection (sequences) types
# strings, bytes, tuples, lists, dictionaries and sets
# operations accepting collection type. ITERABLES
# Iterables are objects that can be used in loop constructs
#https://wiki.python.org/moin/Iterator
# Some common features: 
#  len(), indexing , slicing, sorted 
#    any;The any(collection)returns True if any member of the collection is true.
#    all; The all(collection)  returns True iff if—all the members are true.
#  indexing to access one element, access by indexing [-1]
#  Slicing to access multiple items [start_index:end:step_size]
#  slicing not valid for Dictionaries or sets


def slicing():
    numbers_string = "012345678"
    print(numbers_string)
    print("[:]",numbers_string[:]) #start index is zero 0
    print("[3:]",numbers_string[3:])
    print("[:3]",numbers_string[:3])
    print("[3:7]",numbers_string[3:7])
    print("step_size [3:7:2]",numbers_string[3:7:2]) #step
    print("Even[::]",numbers_string[::2])
    print(" [:]",numbers_string[::3])
    print(any(numbers_string))
    print(all(numbers_string))


slicing()

#### 4 A: 
## strings : Unicode characters: (default encoding is UTF-8)
def string_collection():
    
    print("\n strings are Immutable: a tab \t plus \\ ")
    empty_string = ""
    print(bool(empty_string))#treated as false in boolean Expressio
    #string operations
    string1 = "abcd"
    string2 = "DEFG"
    print("string1: ", string1)
    print("string2: ", string2)

    print("Cancatenation +: ", string1 + string2)
    print("Multiplication *: ", string1 * 3)
    print("upp,low,capitalize : ",string1.upper(),string1.lower(),string1.capitalize() )
    print("center,ljust,rjust: ", string1.center(20,"*")) #length,character
    print("find,rfind,index: ", string1.find("d"),string1.rfind("d")) 
    #string content
    print("isalpha,isdigit: ", string1.isdigit(),string1.isalnum())

    #string join
    print("string.join(iterable) : " ,   " ".join(string2))#SPACE
    print("Join : ", string1.join(string2))

    #string split, splitlines, partiton
    # split:splits a string into a list.
    string3 = " hi! how are you? dear. "
    print("Split,splits a string into a list. : ", string1.split())
    print("Split the text from space : ", string3.split(" "))
    print("Split(separator, max-NumbOF_splits) : ", string3.split(" ", 0))
    print("Split(separator, max-NumbOF_splits) : ", string3.split(" ", 1))
    
    #strip, lstrip,rstrip
    string4 = "hej!  hur mår du?.    "
    print("Sptrip white_SPC :", string4.strip())
    print("Sptrip white_SPC :", string4.strip("hej"))

    #replace :to delete characters
    # replace(oldValue,newValue,count)
    print("replace phrase with another phrase: ", string4.replace("hej", "hello"))

    ############## FORMAT
    ##The basic concept is that pairs of braces embedded in the string
    # form placeholders for data passed as arguments to format():
    # The braces can contain optional style information, such as padding characters
   
    #placeholder: aname indexes{price}, number indexes{0} , empty {}
    #format(value1, value2)

    str1 = "My name is {fname}, I'm {age}".format(fname = "Khan", age = 15)
    str2 = "My name is {0}, I'm {1}".format("Khan",15)
    str3 = "My name is {}, I'm {}".format("Khan",15)

    str4 = "For only {price:.2f} SEK !"
    
    print(str1, "\n",str2, "\n",str3, "\n",str4.format(price = 499))
    
string_collection()
print("\nGEEKS for Geeks Examples and Applications of format() \n ")


#string format(): more exmpales
def format_geekforgeek():
    #gforg

    # Convert base-10 decimal integers to floating point numeric constants
    print("This site is {0:f}% securely {1}!!".
	format(100, "encrypted"))

# To limit the precision
    print("My average of this {0} was {1:.2f}%"
	.format("semester", 78.234876))

# For no decimal places
    print("My average of this {0} was {1:.0f}%"
	.format("semester", 78.234876))

# Convert an integer to its binary or
# with other different converted bases.
    print("The {0} of 100 is {1:b}"
	.format("binary", 100))

    print("The {0} of 100 is {1:o}"
	.format("octal", 100))

# Padding Substitutions or Generating Spaces
# Example 7: Demonstration of spacing when strings are passed as parameters
# By default, strings are left-justified within the field, and numbers are right-justified. 
# We can modify this by placing an alignment code just following the colon.

#   <   :  left-align text in the field
#   ^   :  center text in the field
#   >   :  right-align text in the field
# To demonstrate spacing when
# strings are passed as parameters
    print("{0:4}, is the computer science portal for {1:8}!"
	.format("GeeksforGeeks", "geeks"))

# To demonstrate spacing when numeric
# constants are passed as parameters.
    print("It is {0:5} degrees outside !"
	.format(40))

# To demonstrate both string and numeric
# constants passed as parameters
    print("{0:4} was founded in {1:16}!"
	.format("GeeksforGeeks", 2009))


# To demonstrate aligning of spaces
    print("{0:^16} was founded in {1:<4}!"
	.format("GeeksforGeeks", 2009))

    print("{:*^20s}".format("Geeks"))
    print("  ---------Applications--------- ")
    
# Applications 
#Formatters are generally used to Organize Data. 
# Formatters can be seen in their best light when they are being 
# used to organize a lot of data in a visual way. If we are showing 
# databases to users, using formatters to increase field size and 
# modify alignment can make the output more readable.

#Example 8: To demonstrate the organization of large data using 
# format()
# which prints out i, i ^ 2, i ^ 3,
# i ^ 4 in the given range

# Function prints out values
# in an unorganized manner
def unorganized(a, b):
	for i in range(a, b):
		print(i, i**2, i**3, i**4)

# Function prints the organized set of values
def organized(a, b):
	for i in range(a, b):

		# Using formatters to give 6
		# spaces to each set of values
		print("{:6d} {:6d} {:6d} {:6d}"
			.format(i, i ** 2, i ** 3, i ** 4))

# Driver Code
n1 = int(input("Enter lower range :-\n"))
n2 = int(input("Enter upper range :-\n"))

print("------Before Using Formatters-------")

# Calling function without formatters
unorganized(n1, n2)

print()
print("-------After Using Formatters---------")
print()

# Calling function that contains
# formatters to organize the data
organized(n1, n2)

##################
########Using a dictionary for string formatting 
#Using a dictionary to unpack values into the placeholders in the 
# string that needs to be formatted. We basically use ** to unpack 
# the values. 
#This method can be useful in string substitution while 
# preparing an SQL query.
introduction = 'My name is {first_name} {middle_name} {last_name} AKA the {aka}.'
full_name = {
	'first_name': 'Tony',
	'middle_name': 'Howard',
	'last_name': 'Stark',
	'aka': 'Iron Man',
}

# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))


###########list#####
# Given a list of float values, the task is to truncate 
# all float values to 2-decimal digits. 
# Let’s see 
# # Python code to truncate float values to 2 decimal digits.

# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

# Using format
Output = ['{:.2f}'.format(elem) for elem in Input]

# Print output
print(Output)

format_geekforgeek()
