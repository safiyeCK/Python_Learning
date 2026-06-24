#Variables - data-shaped boxes
# Variables are used to store data in a program
# Variables can be created by assigning a value to a name
# Variable names can contain letters, numbers, and underscores, but cannot start with a number
# Variable names are case-sensitive
# Variable names should be descriptive and meaningful
# Variable names should not be a reserved keyword in Python
# Variable names should not contain spaces or special characters
# Variable names should be written in lowercase, with words separated by underscores (snake_case)
# Variable names should not start with a number
# Variable names should not be too long or too short
# Variable names should not be too generic or too specific
# Variable names should not be too similar to other variable names
# Variable names should not be too similar to built-in functions or modules
# Variable names should not be too similar to reserved keywords
# Variable names should not be too similar to other variable names
# Variable names should not be too similar to built-in functions or modules
# Variable names should not be too similar to reserved keywords
      
# Değişkenler, programda veri saklamak için kullanılır.
# Bir değişken oluşturmak için bir isme değer atamanız yeterlidir.
# Değişken isimlerinde harf, rakam ve alt çizgi (_) kullanılabilir; ancak isim rakamla başlayamaz.
# Değişken isimleri büyük/küçük harfe duyarlıdır (örneğin, sayi ve Sayi farklı değişkenlerdir).
# İsimler açıklayıcı ve anlamlı olmalıdır.
# Python’daki özel anahtar kelimeler (if, for, class gibi) değişken ismi olarak kullanılmamalıdır.
# Değişken isimlerinde boşluk veya özel karakterler bulunmamalıdır.
# Python’da yaygın olarak kullanılan isimlendirme biçimi snake_case’dir: tüm harfler küçük ve kelimeler alt çizgiyle ayrılır (örneğin, kullanici_adi).
# Değişken isimleri çok uzun veya çok kısa olmamalı, çok genel ya da çok özel olmamalıdır.
# Yerleşik fonksiyon veya modül isimlerine (list, str gibi) benzer isimler kullanılmamalıdır.
# Birbirine çok benzeyen değişken isimlerinden kaçınılmalıdır.

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = 2
account_balance = 2000.0
client_name = 'Jane Smith'
print(var, account_balance, client_name)
print(var)


#Assigning a new value to an already existing variable
var = 3
var = var +1
print(var)  # Output: 4
###############################################
#Solving simple mathematical problems
# Example 1: Calculate the area of a rectangle
length = 5  # Length of the rectangle
width = 3   # Width of the rectangle
area = length * width  # Area calculation
print("Area of the rectangle:", area)  # Output: Area of the rectangle: 15

# Example 2: Calculate the total cost of items      
item_price = 20.0  # Price of a single item
quantity = 4       # Number of items purchased
total_cost = item_price * quantity  # Total cost calculation
print("Total cost of items:", total_cost)  # Output: Total cost of items: 80.0  

# Example 3: Calculate the average of three numbers
num1 = 10  # First number       
num2 = 15  # Second number
num3 = 20  # Third number
average = (num1 + num2 + num3) / 3  # Average calculation
print("Average of the numbers:", average)  # Output: Average of the numbers: 15.0  
 
 ###################################################
john = 3
marry = 5
adam = 6

print(john , marry , adam)  # Output: 14

total_apples = john + marry + adam  # Total apples calculation
print("Total apples:", total_apples)  # Output: Total apples: 14    

####################################################

#Shortcut operators
# Example 1: Incrementing a variable
counter = 0  # Initial value of the counter 
counter += 1  # Incrementing the counter by 1
print("Counter after incrementing:", counter)  # Output: Counter after incrementing: 1

# Example 2: Decrementing a variable
counter -= 1  # Decrementing the counter by 1

print("Counter after decrementing:", counter)  # Output: Counter after decrementing: 0
# Example 3: Multiplying a variable

multiplier = 2  # Initial value of the multiplier
multiplier *= 3  # Multiplying the multiplier by 3
print("Multiplier after multiplication:", multiplier)  # Output: Multiplier after multiplication: 6

# Example 4: Dividing a variable
divisor = 10  # Initial value of the divisor
divisor /= 2  # Dividing the divisor by 2
print("Divisor after division:", divisor)  # Output: Divisor after division: 5.0    

# Example 5: Modulus operation
modulus_value = 10  # Initial value for modulus operation
modulus_value %= 3  # Calculating the modulus of modulus_value by 3
print("Modulus value after operation:", modulus_value)  # Output: Modulus value after operation: 1

# Example 6: Exponentiation
exponent = 2  # Initial value for exponentiation
exponent **= 3  # Raising the exponent to the power of 3
print("Exponent after exponentiation:", exponent)  # Output: Exponent after exponentiation: 8

# Example 7: Floor division
floor_division_value = 10  # Initial value for floor division
floor_division_value //= 3  # Performing floor division by 3
print("Floor division value after operation:", floor_division_value)  # Output: Floor division
# value after operation: 3

# Example 8: Combining multiple operations
combined_value = 5  # Initial value for combined operations
combined_value += 2  # Adding 2
combined_value *= 3  # Multiplying by 3
combined_value -= 4  # Subtracting 4
print("Combined value after operations:", combined_value)  # Output: Combined value after operations: 13    

# Example 9: Using multiple shortcut operators
value = 10  # Initial value
value += 5  # Adding 5
value *= 2  # Multiplying by 2
value -= 3  # Subtracting 3
value /= 2  # Dividing by 2
print("Value after multiple operations:", value)  # Output: Value after multiple operations: 11.0   


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.60934
kilometers_to_miles = kilometers / 1.60934

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
