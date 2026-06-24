for i in range(1, 1):
    print("The value of i is currently", i)

for i in range(2, 1):
    print("The value of i is currently", i)


power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


import time

# 1'den 5'e kadar Mississippi sayma döngüsü
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i, "Mississippi")
    time.sleep(1)  # 1 saniye bekle

# Final mesaj
print("Ready or not, here I come!")


# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

#The break variant

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


#The continue variant
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")



while True:
    word = input("Enter a word: ")
    
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
    
 # Girilen kelimeyi yazdırmıyoruz, sadece döngü devam ediyor   


# Sesli harf yiyici program

# Kullanıcıdan kelime al
user_word = input("Enter a word: ")

# Kelimeyi büyük harfe çevir
user_word = user_word.upper()

# Her harf için döngü
for letter in user_word:
    # Sesli harfleri kontrol et ve atla
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    
    # Sesli harf değilse yazdır
    print(letter)


# ...existing code...

# Geliştirilmiş sesli harf yiyici program

# Kullanıcıdan kelime al
user_word = input("Enter a word: ")

# Kelimeyi büyük harfe çevir
user_word = user_word.upper()

# Boş string oluştur
word_without_vowels = ""

# Her harf için döngü
for letter in user_word:
    # Sesli harfleri kontrol et ve atla
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    
    # Sesli harf değilse string'e ekle
    word_without_vowels = word_without_vowels + letter

# Sonucu yazdır
print(word_without_vowels)

#The for loop and the else branch

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)    

###################################################


blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

# While döngüsü ile katman katman kontrol et
while blocks >= layer:
    blocks -= layer  # Mevcut katman için blokları kullan
    height += 1      # Yüksekliği artır
    layer += 1       # Bir sonraki katman daha fazla blok gerektirir

print("The height of the pyramid:", height)   

# Görev Açıklaması
# Bu görevde Collatz Hipotezi (3n+1 problemi) adını taşıyan ünlü matematik problemini kodlayacaksınız.

# Collatz Hipotezi Kuralları:

# Pozitif bir sayı c0 ile başlayın
# Eğer sayı çift ise: c0 = c0 ÷ 2
# Eğer sayı tek ise: c0 = 3 × c0 + 1
# c0 ≠ 1 olduğu sürece adım 2'ye dön
# Hipotez: Her sayı sonunda 1'e ulaşır
# Programın yapması gerekenler:

# Kullanıcıdan bir doğal sayı alın
# Collatz kurallarını uygulayın
# Tüm ara değerleri yazdırın
# Kaç adım gerektiğini sayın

# Collatz Hipotezi (3n+1 problemi)

c0 = int(input("Enter a natural number: "))
steps = 0

# c0 1'e eşit olmadığı sürece devam et
while c0 != 1:
    # Eğer çift ise 2'ye böl
    if c0 % 2 == 0:
        c0 = c0 // 2
    # Eğer tek ise 3 ile çarp ve 1 ekle
    else:
        c0 = 3 * c0 + 1
    
    # Ara değeri yazdır
    print(c0)
    # Adım sayısını artır
    steps += 1

# Toplam adım sayısını yazdır
print("steps =", steps)

# c0 % 2 == 0: Sayının çift olup olmadığını kontrol eder
# c0 // 2: Tam sayı bölme işlemi
# 3 * c0 + 1: Tek sayılar için Collatz kuralı
# steps: Kaç adımda 1'e ulaşıldığını sayar
# Döngü c0 = 1 olduğunda durur


#Key takeaways: continued

for i in range(1, 11):
    # Line of code.
    print(i, end=" ")


# x = 1
# while x < 11:
    # Line of code.
        # Line of code.
    # Line of code.


# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         # Line of code.
#         print("Found @ symbol")
#     # Line of code.
#     pass


# for digit in "0165031806510":
#     if digit == "0":
#         # Line of code.
#         # Line of code.
#     # Line of code.


n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)


n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)


for i in range(0, 6, 3):
    print(i)
