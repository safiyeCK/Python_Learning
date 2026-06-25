def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
# Bu kod çalıştırıldığında `var` değeri 1 olarak kalacaktır çünkü `my_function` içinde `n` değişkeni yerel olarak tanımlanmıştır.

def message():
    alt = 1
    print("Hello, World!")


#print(alt)
# Bu kod çalıştırıldığında hata verecektir çünkü `alt` değişkeni `message` fonksiyonunun içinde tanımlanmıştır ve dışarıdan erişilemez.

a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)
# Bu kod çalıştırıldığında `fun` fonksiyonu içinde `a` değişkeni 2 olarak yazdırılacak, ancak dışarıdaki `a` değişkeni 1 olarak kalacaktır.

a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)
# Bu kod çalıştırıldığında `fun` fonksiyonu içinde `a` değişkeni 2 olarak değiştirilecek, ancak dışarıdaki `a` değişkeni 3 olarak kalacaktır.

a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)
# Bu kod çalıştırıldığında `fun` fonksiyonu içinde `a` değişkeni 2 olarak değiştirilecek, ancak dışarıdaki `a` değişkeni 3 olarak kalacaktır.
a = 1          # Global 'a' değişkeni 1 olarak tanımlanır

def fun():
    global a   # Fonksiyon içinde global 'a' değişkenini kullanacağımızı belirtiriz | EN: See Turkish explanation
    a = 2      # Global 'a' değişkenini 2 olarak değiştiririz
    print(a)   # 2 yazdırır

a = 3          # Global 'a' değişkenini 3 olarak değiştiririz
fun()          # Fonksiyonu çağırırız
print(a)       # Son durumu yazdırırız | EN: See Turkish explanation