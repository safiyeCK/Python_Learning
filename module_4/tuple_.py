# What is a tuple? immutable degistrilmez | EN: See Turkish explanation
# Bir tuple, Python'da değiştirilemeyen (immutable) bir veri yapısıdır.
# Tuple'lar, birden fazla değeri tek bir değişken içinde saklamak için kullanılır. | EN: See Turkish explanation
# Tuple'lar, parantez içinde tanımlanır ve virgülle ayrılmış değerlerden oluşur.
def create_tuple():
    my_tuple = (1, 2, 3, 4, 5)
    return my_tuple
# Tuple'lar, listelerden farklı olarak değiştirilemezler. Yani, bir tuple oluşturulduktan sonra elemanları değiştirilemez. | EN: See Turkish explanation
# Tuple'lar, listelerden daha hafif ve hızlıdır, çünkü değiştirilemezler. | EN: See Turkish explanation
# Tuple'lar, farklı veri tiplerini içerebilir. Yani, bir tuple içinde sayılar, metinler ve diğer tuple'lar gibi farklı veri tipleri bulunabilir. | EN: See Turkish explanation
# Tuple'lar, indeksleme ile erişilebilir. İlk elemanın indeksi 0'dır. | EN: See Turkish explanation
# Tuple'lar, listeler gibi dilimlenebilir (slicing) ve birden fazla eleman içerebilir. | EN: See Turkish explanation
# Tuple'lar, genellikle sabit veri kümelerini temsil etmek için kullanılır. Örneğin, bir koordinat noktası (x, y) veya bir RGB renk değeri (kırmızı, yeşil, mavi) gibi. | EN: See Turkish explanation
# Tuple'lar, fonksiyonlara argüman olarak geçirilebilir ve fonksiyonlardan değer döndürülebilir.
# Tuple'lar, Python'da veri yapıları arasında önemli bir yere sahiptir ve birçok yerleşik fonksiyon ve metod ile desteklenir. | EN: See Turkish explanation
# Tuple'lar, genellikle veri bütünlüğünü korumak için kullanılır. Değiştirilemez olmaları, verilerin yanlışlıkla değiştirilmesini önler. | EN: See Turkish explanation

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:  #elem değişkeni, tuple'ın her bir elemanını sırayla alır | EN: See Turkish explanation
    print(elem)


my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000) # Tuple'ları birleştirme 
t2 = my_tuple * 3  # Tuple'ı çoğaltma

print(len(t2))   # Tuple'ın uzunluğu | EN: See Turkish explanation
print(t1)  # Tuple'ların birleştirilmesi
print(t2)  # Tuple'ın çoğaltılması
print(10 in my_tuple)   # Tuple'da eleman arama | EN: See Turkish explanation
print(100 not in my_tuple)  # Tuple'da eleman arama (negatif) | EN: See Turkish explanation
print(-10 not in my_tuple)  # Tuple'da eleman arama (negatif) | EN: See Turkish explanation


my_tuple = (1, 2, 3)

# Bu işlemler HATA verir:
# my_tuple[0] = 10        # TypeError!
# my_tuple.append(4)      # AttributeError!
# my_tuple.remove(2)      # AttributeError!
# del my_tuple[1]         # TypeError!

# 1. Yeni Tuple Oluşturma (Birleştirme):
my_tuple = (1, 2, 3)

# "Ekleme" - yeni tuple oluştur | EN: See Turkish explanation
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # (1, 2, 3, 4, 5)

# Başa ekleme | EN: See Turkish explanation
new_tuple = (0,) + my_tuple
print(new_tuple)  # (0, 1, 2, 3)

my_tuple = (1, 2, 3, 4, 5)

# 2. Slicing ile "Çıkarma":
# İlk elemanı "çıkar" | EN: See Turkish explanation
new_tuple = my_tuple[1:]
print(new_tuple)  # (2, 3, 4, 5)

# Son elemanı "çıkar" | EN: See Turkish explanation
new_tuple = my_tuple[:-1]
print(new_tuple)  # (1, 2, 3, 4)

# Ortadaki elemanı "çıkar" (index 2'yi) | EN: See Turkish explanation
new_tuple = my_tuple[:2] + my_tuple[3:]
print(new_tuple)  # (1, 2, 4, 5)

# 3. Liste'ye Çevirip İşlem Yap: | EN: See Turkish explanation
my_tuple = (1, 2, 3)

# Tuple'ı listeye çevir | EN: See Turkish explanation
temp_list = list(my_tuple)
temp_list.append(4)        # Ekleme | EN: See Turkish explanation
temp_list.remove(2)        # Çıkarma

# Tekrar tuple'a çevir | EN: See Turkish explanation
new_tuple = tuple(temp_list)
print(new_tuple)  # (1, 3, 4)

# Özet Karşılaştırma:
# İşlem	              Liste	                Tuple | EN: See Turkish explanation
# Değiştirme	     ✅ list[0] = 10	    ❌ İmkansız
# Ekleme	         ✅ list.append(4)	❌ Yeni tuple oluştur | EN: See Turkish explanation
# Çıkarma	         ✅ list.remove(2)	❌ Slicing kullan | EN: See Turkish explanation
# Birleştirme	     ✅ list1 + list2	✅ tuple1 + tuple2