number_1=int(input("Enter the first number:"))
number_2=int(input("Enter the second number:"))

if number_1 > number_2:
    larger_number= number_1
else:
    larger_number= number_2

print("The larger number is:", larger_number)


#python module_3\Ifstatement.py ==>write terminal

number01= int(input('Enter the first number:'))
number02= int(input('Enter the second number:'))

if number01 > number02: larger_number= number01    
else:larger_number= number02
    
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

#################################################

#Pseudocode and introduction to loops = en buyuk sayiyi bulma | EN: See Turkish explanation

# Read three numbers

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number

###############################################
# Read three numbers. Kullanicidan 3 sayi al ve en buyuk olanini bul.Burada max() ve min() fonksiyonlarini kullanacagiz. | EN: See Turkish explanation
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3) 
smallest_number = min(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)
print("The smallest number is:", smallest_number)
