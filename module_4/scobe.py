def scope_test():
    x = 123


scope_test()
print(x)
# Bu kod çalıştırıldığında hata verecektir çünkü `x` fonksiyonun dışında tanımlanmamıştır.

def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
# Bu kod çalıştırıldığında hata vermeyecektir çünkü `var` global olarak tanımlanmıştır.

def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
# Bu kod çalıştırıldığında `var` değeri 2 olarak değişecektir.