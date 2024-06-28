# Declaring a primitive variable
x_int = 5
x_float = 3.14
x_string = 'this is still a string'
x_bool = True

# Variable operations
x = 5
y = 7
z = x + y # z = 12 due to numeral addition

x = 'abcde'
y = 'fghij'
z = x + y # z = 'abcdefghij' due to string concatenation

# Bool operations treat 'True' as 1 and 'False' as 0

# Sequences (to obtain an item in each of these, use the variable[0] and onward from zero to find it (zero-based indexing))
# Strings may also be considered sequences (can index to find characters). They are immutable  (items can't be changed)
x_list = [True, 'two', 3, 4.0, ['five', 6]] # lists may contain other sequence containers as well
x_tuple = (True, 'two', 3, 4.0, ('five', 6)) # tuples are almost the same as lists, but immutable
x_set = {True, 'two', 3, 4.0, 4} # sets do not contain duplicate values; every value is unique. This set will only return True, 'two', 3, 4.0
x_dictionary = {'key' : 5, 'key2' : 10, 'key3' : "value"} # dictionaries are represented as key-value pairs. Rather than a numerical index, one would use variable['key']

# Sequence operations
# For any of the above sequences, adding like containers (list-list, tuple-tuple) will just concatenate the two
# Any other operations, such as subtraction, multiplication or division can not be done natively with these containers

# Conditional statements
if x == 'condition':
    print('executable')
else:
    print('other executable')   # for the if statement, the == operand compares the two conditions. If True, the following code executes (print used as example). If False, the else code executes
                                # other conditional operands exist as well. !(not equal to), <(less than), <=(less than or equal), >(greater than), >=(greater than or equal)