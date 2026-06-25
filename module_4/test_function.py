def function_name():
    # function_body
    pass

def message():
    print("Enter a value: ")


def main():
    message()
    value = input()
    print("You entered:", value)    

def message():
    print("Enter a value: ")

message()   # fonksiyonun cagrilmasi
value = input()  # kullanicidan deger alinir | EN: See Turkish explanation
print("You entered:", value)  # kullanicinin girdigi deger ekrana yazdirilir | EN: See Turkish explanation

print("We start here.")
print("We end here.")


def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())


def hello(name):    # defining a function yani fonksiyon tanimlama parametre alir. | EN: See Turkish explanation
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function

def greet(say_something):
    print("Hello," + say_something)

input_value=input("Enter a greeting:")
greet(input_value)

# This is a simple function that adds two numbers
def som(a,b):
    return a+b

print(som(3, 5))


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")