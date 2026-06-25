# you must  colculate the leap year

year = int(input("Enter a year:"))

#Gregorian calender controls leap years as follows:

if year < 1582 :
    print("Not within the Gregorian calendar period.")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# Artık yıl kuralları (Gregorian takvimi - 1582'den sonra): | EN: See Turkish explanation

# Yıl 4'e bölünmüyorsa → Common year (normal yıl)
# Yıl 4'e bölünüyor ama 100'e bölünmüyorsa → Leap year (artık yıl)
# Yıl 100'e bölünüyor ama 400'e bölünmüyorsa → Common year (normal yıl)
# Yıl 400'e bölünüyorsa → Leap year (artık yıl)    