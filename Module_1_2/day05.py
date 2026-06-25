# x = input("Enter a number: ")  #input() fonksiyonu sadece terminalde çalışır.
# x = float(x)
# y = x ** 2
# print("y =", y)

var = 2 
var = 3
print(var)

# my_var
# m
# 101 # incorrect (starts with a digit)
# averylongvariablename
# m101
# m 101 # incorrect (contains a space)
# Del
# del # incorrect (is a keyword)


a= '1'  #string
b ="2"  #string concatination olur
print(a + b)  # Output: 12 (string concatenation)

a = 6
b = 3
a/= 2 * b
print(a)  # Output: 1.0 (6 divided by 2 * 3, which is 6)
 
 #  Tih is a comment line

 # print("String #1")
print("String #2")

print("Tell me anything...")
anything= input()
print("You said:", anything)

#terminlade yazdirmak icin, python dosya yolu  =>>  python Module_1_2\day05.py | EN: See Turkish explanation

# Testing TypeError message.
anything01 = input("Enter a number: ")
something = anything01 ** 2.0  # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
