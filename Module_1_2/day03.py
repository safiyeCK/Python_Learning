#Operators and their priorities
print(2 + 3 * 4)  # Output: 14
print(2 + 3 * 4 - 5)  # Output: 9
print(2 + 3 * 4 - 5 + 6)  # Output: 15
print(2 + 3 * 4 - 5 + 6 - 7) # Output: 8

#Operators and their bindings
print(9 % 6 % 2)
print(9 % 4 % 2)  # Output: 1
print(10% 4 % 2)  # Output: 0
# Modülüs (modulus, %) işlemi, bir sayının başka bir sayıya bölümünden kalanı bulur. Yani a % b ifadesi, a sayısı b sayısına bölündüğünde kalan değeri verir.

# Örneğin:

# 9 % 6 işlemi: 9’u 6’ya böldüğümüzde bölüm 1, kalan 3’tür. Sonuç 3 olur.
# Sonra bu kalan tekrar % 2 işlemine girer: 3 % 2 işlemi, 3’ü 2’ye böldüğümüzde kalan 1’dir


#Operators and their bindings: exponentiation

print(2 ** 3 ** 2)  # Output: 512 (3^2 = 9, then 2^9 = 512)
print(2 ** 3 ** 2 + 1)  # Output: 513 (adding 1 to the previous result) => islemler sagdan sola dogru, yani 3**2 once yapilir, sonra 2**9 yapilir
print(2 ** 3 ** 2 - 1)  # Output: 511

#List of priorities
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary plus and minus +, -
# 4. Multiplication, division, floor division, and modulus *, /, //, %
print(2 * 3 % 5) # Output: 1 (2 * 3 = 6, then 6 % 5 = 1)
print(2* 3 // 5) # Output: 0 (2 * 3 = 6, then 6 // 5 = 1) // 6 // 5 işlemi, 6’yı 5’e böler. Normalde 6 / 5 = 1.2 olur.
# taban bolme operatörü ondalık kısmı atar ve sadece tam kısmı alır.
# Yani 6 // 5 sonucu 1 olur.

#Both operators (* and %) have the same priority,

#Operators and parentheses
print(2 * (3 % 5))  # Output: 6  (3 % 5 = 3, then 2 * 3 = 6)
print(2 * 3 % 5)  # Output: 1   (2 * 3 = 6, then 6 % 5 = 1)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # Output: 10  # Explanation:
# 1. Calculate 25 % 13 = 12     
# 2. Add 100 to it: 12 + 100 = 112
# 3. Multiply by 5: 5 * 112 = 560
# 4. Calculate 2 * 13 = 26
# 5. Divide: 560 / 26 = 21.53846153846154
# 6. Floor divide by 2: 21.53846153846154 // 2 = 10.0

#Key takeaways
# 1. Python follows operator precedence rules, where parentheses have the highest priority.
# 2. Exponentiation is right associative, meaning it evaluates from right to left.
# 3. Multiplication, division, floor division, and modulus have the same priority and are evaluated left to right.
# 4. Unary operators (+, -) have lower priority than multiplication and division.
# 5. The order of operations can be changed using parentheses to ensure specific calculations are performed first.
# 6. Understanding operator precedence is crucial for writing correct and efficient Python code.

#Temel çıkarımlar
# 1. Python, en yüksek önceliğe parantezlerin sahip olduğu operatör önceliği kurallarına uyar.
# 2. Üs alma (exponentiation) işlemi sağdan sola doğru değerlendirilir (sağdan bağlanır).
# 3. Çarpma, bölme, taban bölme ve modülüs işlemleri aynı önceliğe sahiptir ve soldan sağa doğru değerlendirilir.
# 4. Tekli (unary) operatörler (+, -), çarpma ve bölmeden daha düşük önceliğe sahiptir.
# 5. Parantezler kullanılarak işlemlerin sırası değiştirilebilir ve belirli hesaplamaların önce yapılması sağlanabilir.
# 6. Operatör önceliğini anlamak, doğru ve verimli Python kodu yazmak için çok önemlidir.

print((2 ** 4), (2 * 4.), (2 * 4)) # Output: 16 8.0 8

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) # Output: -0.5  0.5  0  -1

print((2 % -4), (2 % 4), (2 ** 3 ** 2)) # Output: -2 2 512 explanation:
# 1. 2 % -4 = 2 (2 is less than -4, so the result is 2)
# 2. 2 % 4 = 2 (2 is less than 4, so the result is 2)
# 3. 2 ** 3 ** 2 = 512 (3 ** 2 = 9, then 2 ** 9 = 512)  




