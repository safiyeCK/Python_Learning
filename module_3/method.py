def greeting(name):
    print(f"Hallo, {name}. Nice to meet you")

name =input("Enter your name:")

greeting(name)
    
#################################
def age(age):
    print(f"You are {age} years old.")

age_input = int(input("Enter your age:"))

age(age_input)

#################################
def calculate_sum(num1,num2):
    return num1 + num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = calculate_sum(num1, num2)
print(f"The sum of {num1} and {num2} is {result}.")

###########################


