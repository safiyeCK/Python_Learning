#Write a income tax calculator
# the roles are:
# Gelir ≤ 85,528 thaler: Vergi = (Gelir × 18%) - 556.02
# Gelir > 85,528 thaler: Vergi = 14,839.02 + ((Gelir - 85,528) × 32%)
# Vergi negatifse, vergi = 0

income = float(input("Gelirinizi girin: "))
if income <= 85528:
    tax = (income * 0.18) - 556.02
else:
    tax = 14839.02 + ((income - 85528) * 0.32)
#if tax < 0
if tax < 0:
    tax = 0
tax = round(tax, 2)  # Round the tax to 2 decimal places
print("The tax is :", tax)