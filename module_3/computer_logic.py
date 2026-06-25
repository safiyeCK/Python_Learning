# OR operation
# Argument A	Argument B	A OR B  veay dedigi icin bir true, false de olsa true return eder | EN: See Turkish explanation
# False     	False	   False
# False     	True	   True          
# True      	False	   True
# True      	True	   True


#AND operation
# Argument A	Argument B	   A and B
# False         False         	False
# False	        True	        False
# True	        False	        False
# True	        True	        True


def or_operation(a, b):
    """
    Returns the result of the OR operation on two boolean values.
    
    Parameters:
    a (bool): First boolean value.
    b (bool): Second boolean value.
    
    Returns:
    bool: Result of the OR operation.
    """
    return a or b   

def and_operation(a, b):
    """
    Returns the result of the AND operation on two boolean values.
    
    Parameters:
    a (bool): First boolean value.
    b (bool): Second boolean value.
    
    Returns:
    bool: Result of the AND operation.
    """
    return a and b

# Example 1:
a = 1
print(a > 0)
print(not (a <= 0))


# Example 2:
print(a != 0)
print(not (a == 0))

# Example 3:
p = True
q = False
not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

i = 1
j = not not i

# & (ampersand) - bitwise conjunction;
# | (bar) - bitwise disjunction;
# ~ (tilde) - bitwise negation;
# ^ (caret) - bitwise exclusive or (xor).

# Bitwise operations (      &,        |,         ^)
# Argument A	Argument B	A & B	 A | B	    A ^ B
# 0	              0	        0	        0	       0
# 0	              1	        0	        1	       1
# 1	              0	        0	        1	       1
# 1	              1	        1	        1	       0

# Bitwise operations in Python can also be performed using the following operators:
# x = x & y  	x &= y
# x = x | y	    x |= y
# x = x ^ y	    x ^= y

# Binary left shift and binary right shift
# << (double less than) - left shift
# >> (double greater than) - right shift
12 << 2  # This shifts the bits of 12 (1100 in binary) to the left by 2 positions, resulting in 48 (110000 in binary).
12 >> 2  # This shifts the bits of 12 (1100 in binary) to the right by 2 positions, resulting in 3 (0011 in binary).    

# Hızlı çarpma işlemi
x = 5
print(x << 1)  # 5 * 2 = 10
print(x << 3)  # 5 * 8 = 40

# Hızlı bölme işlemi  
y = 20
print(y >> 1)  # 20 / 2 = 10
print(y >> 2)  # 20 / 4 = 5     Özetle: Shift işlemleri, 2'nin kuvvetleri ile çarpma/bölme yapmak için çok hızlı bir yöntemdir!

# Sola kaydırma her zaman ÇARPMA yapar
x << n  # x * (2^n) anlamına gelir

# Örnekler: | EN: See Turkish explanation
5 << 1  # 5 * 2¹ = 5 * 2 = 10
5 << 2  # 5 * 2² = 5 * 4 = 20  
5 << 3  # 5 * 2³ = 5 * 8 = 40

# Sağa kaydırma her zaman BÖLME yapar

x >> n  # x ÷ (2^n) anlamına gelir (tam sayı bölme)

# Örnekler: | EN: See Turkish explanation
20 >> 1  # 20 ÷ 2¹ = 20 ÷ 2 = 10
20 >> 2  # 20 ÷ 2² = 20 ÷ 4 = 5
20 >> 3  # 20 ÷ 2³ = 20 ÷ 8 = 2


# Priority	Operator	
# 1	        ~, +, -	         unary
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	          binary
# 5	        <<, >>	
# 6	        <, <=, >, >=	
# 7	        ==, !=	
# 8	        &	
# 9	        |	
# 10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

var = 17
var_right = var >> 1  #iki buyktur isareti bol | EN: See Turkish explanation
var_left = var << 2   #iki kucuktur isareti carp | EN: See Turkish explanation
print(var, var_left, var_right)

#exercise
# Bitwise İşlemler Açıklaması
# Bu kodda x = 4 ve y = 1 değerleri üzerinde çeşitli bitwise (bit düzeyinde) işlemler yapılıyor.
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))   # output: false

#exercise  
x = 4
y = 1

a = x & y     # Bitwise AND
# 100  (4)
# & 001  (1)
# ------
#   000  = 0

b = x | y
# 100  (4)
# | 001  (1)    
# ------
#   101  = 5
# Bitwise OR

c = ~x
# 100  (4)
# ~ 001  (1)
# ------
#   011  = 3

d = x ^ 5
# 100  (4)
# ^ 101  (5)
# ------
#   001  = 1

e = x >> 2
# 100 (4) >> 2 = 1
# 100 ÷ 2² = 4 ÷ 4 = 1

f = x << 2
# 100 (4) << 2 = 16
# 100 * 2² = 4 * 4 = 16



print(a, b, c, d, e, f)   #0 5 -5 1 1 16
# Özet:
# a = 0 (AND işlemi)
# b = 5 (OR işlemi)
# c = -5 (NOT işlemi - dikkatli ol!)
# d = 1 (XOR işlemi)
# e = 1 (Sağa kaydırma)
# f = 16 (Sola kaydırma)











