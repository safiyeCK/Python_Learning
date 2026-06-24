# The try-except branch
# Python'da hata yönetimi için try-except bloklarını kullanabilirsiniz.
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez.")
# Bu kod, sıfıra bölme hatasını yakalar ve kullanıcıya uygun bir mesaj gösterir.
# try-except blokları, programınızın beklenmeyen hatalarla karşılaştığında çökmesini önler.

# Hata yönetimi, programınızın daha dayanıklı ve kullanıcı dostu olmasını sağlar.
# Ayrıca, hata ayıklama sürecini kolaylaştırır ve kodunuzun daha temiz ve anlaşılır olmasına yardımcı olur.
# Hata yönetimi, programınızın beklenmeyen hatalarla karşılaştığında çökmesini önler.

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
# Bu kod, kullanıcıdan doğal bir sayı girmesini ister ve bu sayının tersini hesaplamaya çalışır.
# Eğer kullanıcı geçersiz bir değer girerse (örneğin, bir harf),    
# ValueError hatası yakalanır ve kullanıcıya uygun bir mesaj gösterilir.
# Eğer kullanıcı sıfır girerse, ZeroDivisionError hatası yakalanır ve kullanıcıya sıfıra bölmenin mümkün olmadığı bildirilir.
# Eğer başka bir hata oluşursa, genel except bloğu devreye girer ve kullanıcıya bilinmeyen bir hata mesajı gösterilir.

# Some useful exceptions
# - FileNotFoundError: Dosya bulunamadığında
# - IndexError: Liste veya dizinin sınırları dışında bir elemana erişilmeye çalışıldığında
# - KeyError: Sözlükte olmayan bir anahtara erişilmeye çalışıldığında   
# - TypeError: Yanlış türde bir işlem yapıldığında (örneğin, bir string ile bir integer'ı toplamak)
# - ValueError: Bir fonksiyona yanlış türde bir değer geçirildiğinde (
#   örneğin, bir string'i integer'a dönüştürmeye çalışmak)
# - ImportError: Modül veya fonksiyon bulunamadığında
# - AttributeError: Bir nesne üzerinde olmayan bir özelliğe erişilmeye çalışıldığında
# - IOError: Giriş/çıkış işlemleri sırasında bir hata oluştuğunda
# - RuntimeError: Çalışma zamanında oluşan genel bir hata
# - OverflowError: Bir sayının sınırlarını aştığında (örneğin, çok büyük bir sayı)
# - MemoryError: Bellek yetersiz olduğunda
# - AssertionError: Bir assert ifadesi başarısız olduğunda
# - KeyboardInterrupt: Kullanıcı tarafından programın durdurulması (Ctrl+C ile)
# - StopIteration: Bir iteratörün sonuna gelindiğinde
# - TimeoutError: Bir işlem zaman aşımına uğradığında
# - ConnectionError: Ağ bağlantısı ile ilgili bir hata oluştuğunda
# - PermissionError: Bir dosyaya erişim izni olmadığında
# - NotImplementedError: Bir fonksiyonun henüz uygulanmadığında
# - RecursionError: Rekürsif bir fonksiyonun maksimum derinliğe ulaştığında
# - UnicodeError: Unicode karakterlerle ilgili bir hata oluştuğunda
# - EnvironmentError: Çevresel bir hata oluştuğunda (örneğin, dosya sistemi hatası)
# - DeprecationWarning: Kullanılan bir özelliğin gelecekteki sürümlerde kaldırılacağına dair uyarı
# - FutureWarning: Gelecekteki sürümlerde değişiklik yapılacağına dair uyarı
# - UserWarning: Kullanıcı tarafından oluşturulan bir uyarı
# - Warning: Genel bir uyarı
# - Exception: Tüm istisnaların temel sınıfı
# - BaseException: Tüm istisnaların en temel sınıfı (genellikle kullanılmaz, Exception kullanılır)
# - ArithmeticError: Aritmetik işlemlerle ilgili genel bir hata
# - FloatingPointError: Ondalık sayı işlemleri sırasında bir hata oluştuğunda
# - BufferError: Bellek tamponu ile ilgili bir hata oluştuğunda
# - SystemExit: Programın normal bir şekilde sonlandırılması gerektiğinde
# - SystemError: Python'un içsel bir hatası oluştuğunda
# - Warning: Genel bir uyarı
# - ImportWarning: Modül veya paket ile ilgili bir uyarı