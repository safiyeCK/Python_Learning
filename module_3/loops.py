# while conditional_expression:
#     instruction_one
#     instruction_two
#     instruction_three
#     :
#     :
#     instruction_n

# while True:
#     print("I'm stuck inside a loop.")

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number? | EN: See Turkish explanation
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)


# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)


# Guessing game with a while loop

secret_number = 777  # Sihirbazın gizli sayısı

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Kullanıcıdan tahmin al | EN: See Turkish explanation
user_number = int(input("Enter your guess: "))

# While döngüsü - doğru tahmin edilene kadar devam et | EN: See Turkish explanation
while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter your guess: "))

# Doğru tahmin edildiğinde
print(user_number)
print("Well done, muggle! You are free now.")


i = 0
while i < 100:
    # do_something()
    i += 1

for i in range(100):
    # do_something()
    pass

for i in range(10):
    print("The value of i is currently", i)

for i in range(2, 8):
    print("The value of i is currently", i)    