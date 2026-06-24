#String operators 

# String concatenation
print("Hello, " + "world!")  # Output: Hello, world!  

# String repetition
print("Hello! " * 3)  # Output: Hello! Hello! Hello!  # bu sekilde stringi 3 kere tekrarlar

# String indexing  => indexini alir
my_string = "Hello, world!"
print(my_string[0])  # Output: H (first character)  

# String slicing
print(my_string[0:5])  # Output: Hello (characters from index 0 to 4)
print(my_string[7:])  # Output: world! (characters from index 7 to the end)
print(my_string[:5])  # Output: Hello (characters from the start to index 4)
print(my_string[-6:])  # Output: world! (last 6 characters)     

# String length 
print(len(my_string))  # Output: 13 (length of the string)      

# String methods
print(my_string.lower())  # Output: hello, world! (convert to lowercase)
print(my_string.upper())  # Output: HELLO, WORLD! (convert to uppercase)
print(my_string.replace("world", "Python"))  # Output: Hello, Python! (replace substring)
print(my_string.split(","))  # Output: ['Hello', ' world!'] (split


#string into a list)
print(my_string.find("world"))  # Output: 7 (find the index of a substring)
print(my_string.count("o"))  # Output: 2 (count occurrences of a character)

# String formatting
name = "Alice"      
age = 30    
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.
print("My name is {} and I am {} years old.".format(name, age)) # Output: My name is Alice and I am 30 years old.   

# String comparison
print("apple" < "banana")  # Output: True (lexicographical comparison)
print("apple" == "Apple")  # Output: False (case-sensitive comparison)
# String membership
print("Hello" in my_string)  # Output: True (check if substring exists)
print("Python" not in my_string)  # Output: True (check if substring does
# not exist)    

# String iteration
for char in my_string:
    print(char, end=" ")  # Output: H e l l o ,   w o r l d !
# String escape characters
print("\nHello\nWorld")  # Output: Hello (newline) World        

# String raw strings
raw_string = r"C:\Users\Alice\Documents"  # Raw string (backslashes are not escaped)
print(raw_string)  # Output: C:\Users\Alice\Documents           

# String Unicode
unicode_string = "Hello, 🌍!"  # Unicode string with an emoji


# Replication and concatenation

# string * number 
# number * string

print("Hello" * 3)  # Output: HelloHelloHello (string replication)
print(3 * "Hello")  # Output: HelloHelloHello (string replication)

# string + string
print("Hello" + " World")  # Output: Hello World (string concatenation)
print("Hello" + " " + "World")  # Output: Hello World (string concatenation with space)

# string + number
# print("Hello" + 5)  # TypeError: can only concatenate str (string) to str (string)
# To concatenate a string and a number, convert the number to a string first

print("Hello" + str(5))  # Output: Hello5 (string concatenation with number converted to string)

# string + boolean
print("Hello" + str(True))  # Output: HelloTrue (string concatenation with boolean converted to string)

# string + list
# print("Hello" + [1, 2, 3])  # TypeError: can only concatenate str (string) to str (string)
# To concatenate a string and a list, convert the list to a string first

print("Hello" + str([1, 2, 3]))  # Output: Hello[1, 2, 3] (string concatenation with list converted to string)

# string + tuple
# print("Hello" + (1, 2, 3))  # TypeError: can only concatenate str (string) to str (string)
# To concatenate a string and a tuple, convert the tuple to a string first

print("Hello" + str((1, 2, 3)))  # Output: Hello(1, 2, 3) (string concatenation with tuple converted to string)


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")






