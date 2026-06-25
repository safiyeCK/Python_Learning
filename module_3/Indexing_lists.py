numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("New list content: ", numbers)  # Current list content.

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.

numbers.append(99)  # Adding a new element to the end of the list. yani numbers[5] = 99 | EN: See Turkish explanation
print("New list content:", numbers)  # Printing the new list content.

# !The len()   elementin uzunlugunu döner. | EN: See Turkish explanation
#len()  yani elementin length i doner | EN: See Turkish explanation
# !The append() elementi listenin sonuna ekler. | EN: See Turkish explanation
#append()  yani listenin sonuna ekler | EN: See Turkish explanation
# !The index of the first element in a list is 0, and the index of the last element is len(list) - 1.
#index()  yani listenin elemaninin indexini döner | EN: See Turkish explanation
# pop() yani listenin sonundaki elemani siler ve o elemani dondurur | EN: See Turkish explanation

liste = ["a", "b", "c", "d"]

# Pozitif indeksler (baştan):
#          0    1    2    3

# Negatif indeksler (sondan): | EN: See Turkish explanation
#         -4   -3   -2   -1

# Index:    0    1    2    3
# Length: len(liste) = 4 | EN: See Turkish explanation

print(liste[0])     # "a" - İlk eleman | EN: See Turkish explanation
print(liste[3])     # "d" - Son eleman | EN: See Turkish explanation
print(liste[len(liste)-1])  # "d" - Son eleman (alternatif yol) | EN: See Turkish explanation

#Negative Indices (Negatif İndeksler)
# Son elemanın indexi = len(liste) - 1 | EN: See Turkish explanation
son_index = len(liste) - 1  # 4

# Negatif indeksler
print(liste[-1])  # "d" - Son eleman | EN: See Turkish explanation
print(liste[-4])  # "a" - İlk eleman | EN: See Turkish explanation
# Uzunluğunu bilmediğiniz bir listede: | EN: See Turkish explanation
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Zor yol:
print(my_list[len(my_list)-1])  # "10" - Son eleman | EN: See Turkish explanation


numbers = [10, 5, 7, 2, 1]

# Bu ikisi aynı sonucu verir: | EN: See Turkish explanation
print(numbers[4])           # 1 (pozitif indeks)
print(numbers[-1])          # 1 (negatif indeks)

# Bu ikisi de aynı:
print(numbers[0])           # 10 (ilk eleman) | EN: See Turkish explanation
print(numbers[-5])          # 10 (sondan 5. eleman = ilk eleman) | EN: See Turkish explanation

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)
hat_list[2] = int(input("Enter a new middle number: "))  # Replace the middle number
hat_list.pop()  # Remove the last element
print("Updated list:", hat_list)  # Print the updated list
print("Length of the updated list:", len(hat_list))  # Print the length of the updated list
print("Length of the updated list:", len(hat_list))  # Print the length of the updated list

# append() yani listenin sonuna ekler | EN: See Turkish explanation
# pop() yani listenin sonundaki elemani siler ve o elemani dondurur | EN: See Turkish explanation
# index() yani listenin elemaninin indexini döner | EN: See Turkish explanation
# insert() yani listenin istedigimiz indexine ekler | EN: See Turkish explanation
# remove() yani listenin istedigimiz elemanini siler | EN: See Turkish explanation
# sort() yani listenin elemanlarini siralar | EN: See Turkish explanation
# reverse() yani listenin elemanlarini ters cevirir | EN: See Turkish explanation
# clear() yani listenin tum elemanlarini siler | EN: See Turkish explanation
# len()   elementin uzunlugunu döner. | EN: See Turkish explanation

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
#####################################
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
###############################33
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)
###########3###################
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]   # toplama islemi yapiyor

print(total)  # Output: 27

############################# SWAP ELEMENTS
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)     #yani burada ne yaptik? 0. ve 4. elemanlari yer degistirdik, 1. ve 3. elemanlari yer degistirdik. | EN: See Turkish explanation
# Output: [5, 3, 8, 1, 10]

#exercises  Beatles Listesi Görevi | EN: See Turkish explanation
# Bu görevde Beatles grubunun üye değişikliklerini gösteren bir program yazacaksınız. | EN: See Turkish explanation
# Step 1: Boş bir beatles listesi oluştur | EN: See Turkish explanation
beatles = []
print("Step 1:", beatles)

# Step 2: append() ile üç üyeyi ekle | EN: See Turkish explanation
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3: for döngüsü ile kullanıcıdan iki üye daha ekle | EN: See Turkish explanation
members = ["Stu Sutcliffe", "Pete Best"]
for member in members:
    beatles.append(member)
print("Step 3:", beatles)

# Step 4: del ile Stu Sutcliffe ve Pete Best'i çıkar
del beatles[4]  # Pete Best (sonuncu) | EN: See Turkish explanation
del beatles[3]  # Stu Sutcliffe (sondan ikinci) | EN: See Turkish explanation
print("Step 4:", beatles)

# Step 5: insert() ile Ringo Starr'ı başa ekle | EN: See Turkish explanation
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Testing list length
print("The Fab", len(beatles))

