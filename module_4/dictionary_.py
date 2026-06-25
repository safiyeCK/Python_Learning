# What is a dictionary? | EN: See Turkish explanation
# yani bir sözlük, Python'da anahtar-değer çiftlerini saklamak için kullanılan bir veri yapısıdır. | EN: See Turkish explanation
# Sözlükler, anahtarların benzersiz olduğu ve her anahtarın bir değere karşılık geldiği bir koleksiyondur. | EN: See Turkish explanation
# Sözlükler, veri yapıları arasında önemli bir yere sahiptir ve birçok yerleşik fonksiyon ve metod ile desteklenir. | EN: See Turkish explanation
# Sözlükler, genellikle verileri hızlı bir şekilde erişmek ve yönetmek için kullanılır. | EN: See Turkish explanation
my_dict = {
    "name": "Ali",
    "age": 30,
    "city": "İstanbul"
}
print(my_dict["name"])  # Ali
print(my_dict["age"])   # 30
print(my_dict["city"])  # İstanbul
# Sözlüklerdeki anahtarlar, string, integer gibi değişik veri tiplerinde olabilir. | EN: See Turkish explanation
# Sözlüklerdeki değerler ise herhangi bir veri tipi olabilir, hatta başka sözlükler veya listeler de içerebilir. | EN: See Turkish explanation
# Sözlüklerdeki anahtarlar benzersizdir, yani aynı anahtar birden fazla kez kullanılamaz. | EN: See Turkish explanation
# Sözlüklerdeki değerler ise değiştirilebilir, yani bir anahtarın değeri sonradan değiştirilebilir. | EN: See Turkish explanation
# Sözlüklerdeki anahtarlar, indeksleme ile erişilemez. Anahtarlar, doğrudan anahtar adı ile erişilir. | EN: See Turkish explanation
# Sözlükler, veri bütünlüğünü korumak için kullanılır. Anahtarların benzersiz olması, verilerin yanlışlıkla üzerine yazılmasını önler. | EN: See Turkish explanation
# Sözlükler, genellikle veri kümelerini temsil etmek için kullanılır. Örneğin, bir kullanıcı bilgisi (isim, yaş, şehir) gibi. | EN: See Turkish explanation
# Sözlükler, fonksiyonlara argüman olarak geçirilebilir ve fonksiyonlardan değer döndürülebilir.
# Sözlükler, Python'da veri yapıları arasında önemli bir yere sahiptir ve birçok yerleşik fonksiyon ve metod ile desteklenir. | EN: See Turkish explanation

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Print the values here.
print(dictionary["cat"])      # chat
print(dictionary["dog"])      # chien
print(dictionary["horse"])    # cheval
print(phone_numbers['boss'])  # 5551234567
print(phone_numbers['Suzy'])  # 22657854310

# How to use a dictionary: the keys()
# Sözlüklerdeki anahtarları almak için keys() metodunu kullanabilirsiniz. | EN: See Turkish explanation
# Bu metod, sözlükteki tüm anahtarları bir liste olarak döndürür. | EN: See Turkish explanation
# Sözlüklerdeki anahtarlar, benzersizdir ve her anahtar bir değere karşılık gelir. | EN: See Turkish explanation
# Anahtarlar, string, integer gibi değişik veri tiplerinde olabilir. | EN: See Turkish explanation
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


#How to use a dictionary: The items() and values() methods
# Sözlüklerdeki anahtar-değer çiftlerini almak için items() metodunu kullanabilirsiniz. | EN: See Turkish explanation
# Bu metod, sözlükteki tüm anahtar-değer çiftlerini bir liste olarak döndürür. | EN: See Turkish explanation
# Sözlüklerdeki değerleri almak için values() metodunu kullanabilirsiniz. | EN: See Turkish explanation
# Bu metod, sözlükteki tüm değerleri bir liste olarak döndürür. | EN: See Turkish explanation
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key, value in dictionary.items():
    print(key, "->", value)

# Sözlüklerdeki değerleri almak için values() metodunu kullanabilirsiniz. | EN: See Turkish explanation
for value in dictionary.values():
    print(value)
# Sözlüklerdeki anahtarları ve değerleri birlikte almak için items() metodunu kullanabilirsiniz. | EN: See Turkish explanation
for item in dictionary.items():
    print(item)  # Anahtar-değer çiftlerini tuple olarak döndürür | EN: See Turkish explanation


# How to use a dictionary: modifying and adding values
# Sözlüklerdeki değerleri değiştirmek için, anahtarın değerini doğrudan atayabilirsiniz. | EN: See Turkish explanation
# Sözlüklerdeki yeni anahtar-değer çiftlerini eklemek için, yeni anahtarın değerini doğrudan atayabilirsiniz. | EN: See Turkish explanation
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# Değerleri değiştirme
dictionary["cat"] = "gato"  # "cat" anahtarının değerini "gato" olarak değiştirir | EN: See Turkish explanation
dictionary["dog"] = "perro"  # "dog" anahtarının değerini "perro" olarak değiştirir | EN: See Turkish explanation
print(dictionary)  # {'cat': 'gato', 'dog': 'perro', 'horse': 'cheval'}
# Yeni anahtar-değer çiftleri ekleme | EN: See Turkish explanation
dictionary["bird"] = "pájaro"  # Yeni "bird" anahtarını ekler ve değerini "pájaro" olarak atar | EN: See Turkish explanation
dictionary["fish"] = "pez"      # Yeni "fish" anahtarını ekler ve değerini "pez" olarak atar | EN: See Turkish explanation
print(dictionary)  # {'cat': 'gato', 'dog': 'perro', 'horse': 'cheval', 'bird': 'pájaro', 'fish': 'pez'}     

# Sözlüklerdeki anahtar-değer çiftlerini silmek için del anahtar kelimesini kullanabilirsiniz. | EN: See Turkish explanation
del dictionary["cat"]  # "cat" anahtarını ve değerini siler | EN: See Turkish explanation
del dictionary["dog"]  # "dog" anahtarını ve değerini siler | EN: See Turkish explanation
print(dictionary)  # {'horse': 'cheval', 'bird': 'pájaro', 'fish': 'pez'} 
# Sözlüklerdeki tüm anahtar-değer çiftlerini silmek için clear() metodunu kullanabilirsiniz. | EN: See Turkish explanation
dictionary.clear()  # Tüm anahtar-değer çiftlerini siler | EN: See Turkish explanation
print(dictionary)  # {}     

# How to use a dictionary: checking for keys
# Sözlüklerdeki anahtarların varlığını kontrol etmek için in anahtar kelimesini kullanabilirsiniz. | EN: See Turkish explanation
# Bu, sözlükteki anahtarın var olup olmadığını kontrol eder ve True veya False döndürür. | EN: See Turkish explanation
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# Anahtarın varlığını kontrol etme | EN: See Turkish explanation
if "cat" in dictionary:
    print("Cat anahtarı var")  # Cat anahtarı var | EN: See Turkish explanation
else:
    print("Cat anahtarı yok")
if "lion" in dictionary:
    print("Lion anahtarı var")
else:
    print("Lion anahtarı yok")
# Sözlüklerdeki anahtarların varlığını kontrol etmek için get() metodunu kullanabilirsiniz. | EN: See Turkish explanation
# Bu metod, sözlükteki anahtarın değerini döndürür. Eğer anahtar yoksa, None döndürür. | EN: See Turkish explanation
value = dictionary.get("cat")
if value is not None:
    print("Cat anahtarının değeri:", value)  # Cat anahtarının değeri: chat | EN: See Turkish explanation
else:
    print("Cat anahtarı yok")       
# Sözlüklerdeki anahtarların varlığını kontrol etmek için get() metodunu kullanabilirsiniz. | EN: See Turkish explanation
# Bu metod, sözlükteki anahtarın değerini döndürür. Eğer anahtar yoksa, varsayılan bir değer döndürebilirsiniz. | EN: See Turkish explanation
