x = 0, y = 1,  z = 0

# ==	returns True if operands' values are equal, and False otherwise	
#-  !=	returns True if operands' values are not equal, and False otherwise	
x != y  # True
x != z  # False

# >	True if the left operand's value is greater than the right operand's value, and False otherwise	
x > y  # False
y > z  # True

# <	True if the left operand's value is less than the right operand's value, and False otherwise	
x < y  # True
y < z  # False

# ≥	True if the left operand's value is greater than or equal to the right operand's value, and False otherwise	
x >= y  # False
x >= z  # True
y >= z  # True

# ≤	True if the left operand's value is less than or equal to the right operand's value, and False otherwise	
x <= y  # True
x <= z  # True
y <= z  # False

#########################
# conditional statement:
x = 10

if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.

x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.   


##########################################
x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.

##################################
x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")

#################################
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")

###############################
x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")   