# None Değeri Açıklaması
# None, Python'da çok özel bir değerdir ve "hiçlik" anlamına gelir.

# None Nedir?
# None = "Hiçbir şey yok" demektir
# Gerçek bir değer değildir, değersizliği temsil eder
# Diğer dillerdeki null, nil veya undefined kavramına benzer

# None tek başına kullanılabilir
result = None
print(result)  # None

# Ama matematiksel işlemlerde KULLANILMAZ
# print(None + 5)      # TypeError! 
# print(None * 2)      # TypeError!
# print(None > 10)     # TypeError!

value = None
if value is None:
    print("Sorry, you don't carry any value")


#A few words about None: continued
# None, Python'da bir değişkenin henüz bir değer almadığını veya bilinçli olarak "değer yok" anlamına geldiğini belirtmek için kullanılır.
# None, bir fonksiyonun değer döndürmediğini belirtmek için de kullanılabilir.
# Örneğin, bir fonksiyon sadece bir işlem yapıp değer döndürmüyorsa, None döndürebilir.
# None, boolean bir değer olarak False ile eşdeğerdir, yani if koşullarında False olarak değerlendirilir.   
# 

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(4))  # True
print(strange_function(5))  # None (değer döndürmediği için None döner)


