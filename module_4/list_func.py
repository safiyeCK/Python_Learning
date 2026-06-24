def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
# yani bu fonksiyon bir liste içindeki sayıların toplamını döndürür.
def list_average(lst):
    if len(lst) == 0:
        return None  # Boş liste için None döndür
    
    total = list_sum(lst)
    average = total / len(lst)
    
    return average
# yani bu fonksiyon bir liste içindeki sayıların ortalamasını döndürür.

def list_max(lst):
    if len(lst) == 0:
        return None  # Boş liste için None döndür
    
    max_value = lst[0]
    
    for elem in lst:
        if elem > max_value:
            max_value = elem
    
    return max_value
# yani bu fonksiyon bir liste içindeki en büyük sayıyı döndürür.
def list_min(lst):
    if len(lst) == 0:
        return None  # Boş liste için None döndür
    
    min_value = lst[0]
    
    for elem in lst:
        if elem < min_value:
            min_value = elem
    
    return min_value
# yani bu fonksiyon bir liste içindeki en küçük sayıyı döndürür.
def list_reverse(lst):
    reversed_list = []
    
    for elem in lst:
        reversed_list.insert(0, elem)  # Her elemanı başa ekle
    
    return reversed_list
# yani bu fonksiyon bir listeyi tersine çevirir.

# Effects and results: lists and functions - continued
def list_contains(lst, value):
    for elem in lst:
        if elem == value:
            return True  # Değer bulundu
    return False  # Değer bulunamadı
# yani bu fonksiyon bir listenin belirli bir değeri içerip içermediğini kontrol eder.
def list_count(lst, value):
    count = 0
    
    for elem in lst:
        if elem == value:
            count += 1  # Değer bulunduğunda sayacı artır
    
    return count
# yani bu fonksiyon bir listenin belirli bir değerden kaç kez içerdiğini sayar.

#
def is_year_leap(year):
    # Artık yıl kontrolü
    if year % 4 != 0:
        return False        # 4'e bölünmüyorsa normal yıl
    elif year % 100 != 0:
        return True         # 4'e bölünür ama 100'e bölünmezse artık yıl
    elif year % 400 != 0:
        return False        # 100'e bölünür ama 400'e bölünmezse normal yıl
    else:
        return True         # 400'e bölünürse artık yıl

# Test kodu leap year fonksiyonunu kontrol etmek için
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


#
# Your code from LAB 4.3.1.6.
#

def days_in_month(year, month):
    # Ayların gün sayısı (Şubat için 28, artık yıl kontrolü aşağıda)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None  # Geçersiz ay
    if month == 2 and is_year_leap(year):
        return 29
    return month_days[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
# yani bu fonksiyon bir yıl ve ay için o ayın kaç gün olduğunu döndürür.

def is_year_leap(year):
    # Artık yıl kontrolü
    if year % 4 != 0:
        return False        
    elif year % 100 != 0:
        return True         
    elif year % 400 != 0:
        return False        
    else:
        return True         

def days_in_month(year, month):
    # Ayların gün sayısı
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month < 1 or month > 12:
        return None  # Geçersiz ay
    
    if month == 2 and is_year_leap(year):
        return 29
    
    return month_days[month - 1]

def day_of_year(year, month, day):
    # Geçersiz ay kontrolü
    if month < 1 or month > 12:
        return None
    
    # O ay için maksimum gün sayısını al
    max_days = days_in_month(year, month)
    
    # Geçersiz gün kontrolü
    if day < 1 or day > max_days:
        return None
    
    # Yılın başından itibaren günleri hesapla
    total_days = 0
    
    # Önceki ayların günlerini topla
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    # Bu ayın günlerini ekle
    total_days += day
    
    return total_days

# Test vakaları
print(day_of_year(2000, 12, 31))  # 366 (artık yıl)
print(day_of_year(1999, 12, 31))  # 365 (normal yıl)
print(day_of_year(2000, 1, 1))    # 1 (yılın ilk günü)
print(day_of_year(2000, 2, 29))   # 60 (artık yılda şubat ayının 29'u)
print(day_of_year(1999, 2, 29))   # None (normal yılda şubat 29 yok)
print(day_of_year(2000, 13, 1))   # None (geçersiz ay)
print(day_of_year(2000, 4, 31))   # None (nisan ayında 31 gün yok)

