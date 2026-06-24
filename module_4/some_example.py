# #Some simple functions: evaluating the BMI
# Let's get started on a function to evaluate the Body Mass Index (BMI).

# BMI equals weight in kilograms divided by height in meters squared
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
calculate_bmi(70, 1.75)  # Example usage: 70 kg and 1.75 m height


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))
# Bu kod çalıştırıldığında, BMI hesaplaması için verilen ağırlık ve yükseklik değerleri geçersiz olduğu için None dönecektir.

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
# Bu kod çalıştırıldığında, ilk fonksiyon çağrısı bir üçgen olduğunu doğrularken, ikinci çağrı bir üçgen olmadığını belirtecektir.

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
# Bu kod, kullanıcıdan üç kenarın uzunluklarını alır ve bu kenarların bir üçgen oluşturup oluşturamayacağını kontrol eder. Eğer üçgen oluşturabiliyorsa "Yes, it can be a triangle." mesajını, oluşturamıyorsa "No, it can't be a triangle." mesajını yazdırır.

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
# Bu kod, kullanıcıdan üç kenarın uzunluklarını alır ve bu kenarların bir üçgen oluşturup oluşturamayacağını kontrol eder. Eğer üçgen oluşturabiliyorsa "Yes, it can be a triangle." mesajını, oluşturamıyorsa "No, it can't be a triangle." mesajını yazdırır.
# 
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))
# Bu kod, 1'den 5'e kadar olan sayılar için faktöriyel hesaplaması yapar ve her bir sayının faktöriyelini yazdırır. Örneğin, 1! = 1, 2! = 2, 3! = 6, 4! = 24 ve 5! = 120 olarak hesaplanır.

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):  # testing
    print(n, "->", fib(n))    
# Bu kod, Fibonacci dizisinin ilk 9 terimini hesaplar ve her bir terimi yazdırır. Fibonacci dizisi, her terimin kendisinden önceki iki terimin toplamı olduğu bir dizidir. Örneğin, 1, 1, 2, 3, 5, 8, 13, 21 ve 34 olarak hesaplanır.    