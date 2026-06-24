# Bubble Sort (Kabarcık Sıralama) Algoritması
# Bu metin bubble sort adlı sıralama algoritmasını açıklıyor.

# Ana Açıklama:
# Bubble Sort nedir?

# Çok basit ama yavaş bir sıralama algoritması
# Anlaması kolay ama verimli değil
# Büyük listeler için kullanılmaz
# Sadece öğrenme amaçlı kullanılır

# Örnek liste
my_list = [8, 10, 6, 2, 4]

# Komşu elemanları karşılaştır ve gerekirse yer değiştir
# İlk geçiş:
# [8, 10, 6, 2, 4] → 8 < 10 ✓ (değişiklik yok)
# [8, 10, 6, 2, 4] → 10 > 6 ✗ (yer değiştir)
# [8, 6, 10, 2, 4] → 10 > 2 ✗ (yer değiştir)
# [8, 6, 2, 10, 4] → 10 > 4 ✗ (yer değiştir)
# [8, 6, 2, 4, 10] → En büyük eleman sona geldi

# Bu işlem tüm liste sıralanana kadar tekrarlanır
def bubble_sort(liste):
    n = len(liste)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Komşu elemanları karşılaştır
            if liste[j] > liste[j + 1]:
                # Yer değiştir (swap)
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    
    return liste

# Test
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Sıralanmamış:", my_list)
bubble_sort(my_list)
print("Sıralanmış:", my_list)


# The inner life of lists
# Listeler, Python'da veri saklamak için kullanılan en temel veri yapılarından biridir.
# Listeler, sıralı ve değiştirilebilir (mutable) bir veri yapısıdır.
# Listeler, farklı veri tiplerini (sayılar, metinler, diğer listeler vb.) içerebilir.
# Listeler, indeksleme ile erişilebilir. İlk elemanın indeksi 0'dır.
# Listeler, dinamik olarak boyutlandırılabilir. Yani, başlangıçta belirli bir boyuta sahip olsalar da, eleman ekleyebilir veya çıkarabilirsiniz.
# Listeler, Python'da çok yaygın olarak kullanılır ve birçok yerleşik fonksiyon ve metod ile desteklenir.

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# Powerful slices 
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]  # yani 1, indexinden 3. indekse kadar olan elemanları alır. Basladigi index alir bitis index almaz.
print(new_list)  # Output: [8, 6]

# Slices - negative indices
my_list = [10, 8, 6, 4, 2] #negatifler -1 den başlar.
new_list = my_list[-4:-2]  # yani -4, indexinden -2. indekse kadar olan elemanları alır.
print(new_list)  # Output: [8, 6]

# Slices: continued
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:]  # 1. indeksten sonrasını alır. o index dahil.
print(new_list)  # Output: [8, 6, 4, 2] 
new_list = my_list[:3]  # 3. indekse kadar olan elemanları alır.
print(new_list)  # Output: [10, 8, 6]

# Slicing with negative indices
my_list = [10, 8, 6, 4, 2]  
new_list = my_list[-3:]  # -3. indeksten sonrasını alır.
print(new_list)  # Output: [6, 4, 2]
new_list = my_list[:-2]  # -2. indekse kadar olan elemanları alır.
print(new_list)  # Output: [10, 8, 6]   

# The in and not in operators
# The in operator checks if an element is present in a list. yani in ile sordugu elaman listede var mi yok mu.
my_list = [10, 8, 6, 4, 2]
print(6 in my_list)  # Output: True
print(5 in my_list)  # Output: False

# Lists - some simple programs yani listelerle basit programlar nasil yazilir 
# Program to find the maximum element in a list
def find_maximum(my_list):
    if not my_list:  # Check if the list is empty
        return None
    maximum = my_list[0]  # Assume the first element is the maximum
    for num in my_list:
        if num > maximum:
            maximum = num  # Update maximum if a larger number is found
    return maximum


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

# Lists in lists yani listeler icinde listeler
# Lists can contain other lists, creating a nested structure.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in a nested list
print(nested_list[0])    # Output: [1, 2, 3]
print(nested_list[1][0]) # Output: 4    
# Lists - indexing and slicing
# Lists can be indexed and sliced like strings.
# Indexing allows access to individual elements.
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Output: 10 (first element)
print(my_list[-1]) # Output: 50 (last element)
# Slicing allows access to a range of elements.
print(my_list[1:4])  # Output: [20, 30,
# 40] (elements from index 1 to 3)
# Lists - concatenation and repetition
# Lists can be concatenated using the + operator and repeated using the * operator.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenation
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
# Repetition
repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]  
# Lists - methods and functions
