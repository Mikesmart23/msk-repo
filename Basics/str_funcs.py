# string functions full tutorial ..

myName = "i'm PyQonsole !!"

####################### 1. Modification Methods ######################                      

# Capitalizes the first character of the string
print(myName.capitalize())

# Converts the first character of each word to uppercase and the rest to lowercase
print(myName.title())

# Converts all characters to uppercase
print(myName.upper())

# Converts all characters to lowercase
print(myName.lower())

''' Converts the string to lowercase, more aggressive than lower() for 
    case-insensitivity comparisons'''
print(myName.casefold())

# Swaps the case of all characters in the string
print(myName.swapcase())

''' Centers the string in a field of given width, padded with fillchar
    (default is space)'''
print(myName.center(20, '-'))

# Formats the string using placeholders
print("PyQonsole is {}", 'Awesome !!')

##################################################################
####################### 2. Whitespace Methods ######################

# Removes leading characters (whitespace by default)
print('    PyQonsole'.lstrip())

# Removes trailing characters (whitespace by default)
print("Hello, Python        ".rstrip())

# Removes leading and trailing whitespace
print('    Py    '.strip())
###############################################################################
####################### 3. Searching and Finding Methods ######################

# Returns the lowest index of the substring if found, else returns -1
print(myName.find('!'))

# Returns the highest index of the substring if found, else -1.
print(myName.rfind('o'))

# Similar to find(), but raises a ValueError if the substring is not found.
print(myName.index("Q"))

# Like rfind(), but raises a ValueError if the substring is not found
print(myName.rindex('!'))

# Counts occurrences of a substring in the string
print(myName.count('o'))

###############################################################################
####################### 4. Splitting and Joining Methods ######################

# Splits the string into a list of substrings
print("hello Python".split(" "))

# Splits the string from the right. If maxsplit is specified, it limits the number of splits
print('py-qonsole'.rsplit('-', 1))

# Splits the string at line breaks, returning a list of lines
print('hello\nPython'.splitlines())

'''Joins elements of an iterable into a single string
   using the string as a separator'''
print('*'.join(['PyQonsole', 'is', 'A', 'Programmer']))

##################################################################
####################### 5. Testing Methods ######################

# Returns True if all characters are alphanumeric
print(myName.isalnum())

# Returns True if all characters in the string are alphabetic
print(myName.isalpha())

# Returns True if all characters in the string are ASCII
print(myName.isascii())

# Returns True if all characters in the string are digits
print(myName.isdigit())

# Returns True if all cased characters are lowercase
print(myName.islower())

# Returns True if all cased characters are uppercase
print(myName.isupper())

# Returns True if all characters in the string are whitespace
print(myName.isspace())

# True if the string starts with the specified prefix, otherwise False.
print(myName.startswith('P'))

# Checks if the string ends with the specified suffix
print(myName.endswith('le'))

###################################################################################
####################### 6.  Encoding and Translation Methods ######################

# Encodes the string using the specified encoding
print(myName.encode())

# Creates a translation table
newName = myName.maketrans('tyQs5', 'pyqT6')
print('sython'.translate(newName))
#################################################################################
####################### 7. Replacing and Modifying Methods ######################

# Replaces occurrences of a substring with another substring
print(myName.replace('!!', '??'))

# Expands tabs in the string to spaces
print("Py\tQonsole".expandtabs(4))

# Pads the string on the left with zeros to fill the specified width
print('10'.zfill(10))
##################################################################
###################### 8. Partitioning Methods ######################

# Splits the string at the first occurrence of the separator
print('Py*Qonsole'.partition('*'))

# Splits from the right side similar to partition().
print('Py*Qonsole'.rpartition('*'))

##################################################################




