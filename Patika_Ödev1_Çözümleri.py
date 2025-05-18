####girilen sayının pozitif negatif veya sıfır olduğunu yazan koşul
def tek_cift():
    sayı = int(input('Bir sayı giriniz: '))
    if sayı<0:
        return 'negatif'
    elif sayı==0:
        return 'sıfır'
    else:
        return 'pozitif'

#####girilen sayının tek mi çift mi olduğunu yazan koşul
def tek_cift():
    while True:
        sayı = input('Bir sayı giriniz: ')

        if sayı.lstrip('-').isdigit():
            sayı = int(sayı)
            break

        print("Geçersiz bir değer girdiniz")

    return "çift" if sayı % 2 == 0 else "tek"

#####Girilen nota göre harf aralığı nı yazan koşul
sayı = int(input('Bir sayı giriniz: '))

if sayı>80 and sayı<=100:
    print('A')
elif sayı>60:
    print('B')
elif sayı>40:
    print('C')
else:
    print('F')

###Girilen ismin karakter sayısı 5'ten büyük ise uzun bir isminiz var değilse ismimi yazsın
isim=input("İsminizi giriniz:")

if len(isim)>5:
    print("uzun bir isminiz var")
else:
    print(isim)

###Girilen sayının asal olup olmadığını bulan kod dizisi (for and while ile)
###For döngüsü ile asal sayı bulma
####1.yol
def asal_mı():
   sayı=int(input("bana bir sayı ver:"))
   if sayı<2:
       return 'asal değil'
   for i in range(2, sayı):
        if sayı % i == 0:
            return 'asal değil'
   return "asal"

###2.yol
while True:
    asal_mı = True
    sayı = int(input("bana bir sayı ver:"))
    if sayı < 2:
        print("2'den küçük sayılar asal değildir.")
        continue
    for i in range(2, sayı):
        if sayı % i == 0:
            print("asal değil")
            asal_mı = False
            break
    if asal_mı:
        print("asaldır")

#while ile asal sayı bulma
sayı = int(input("bana bir sayı ver:"))
flag=True
i=2
while i<sayı:
    if sayı%i==0:
        print("sayı asal değildir")
        flag=False
        break
    i+=1
if flag:
    print("sayı asaldır")

###notlar=[45,85,75,50] içinde 75 değerinin indisini yazdıran döngü
notlar=[45,85,75,50]
for index,eleman in enumerate(notlar):
    if eleman==75:
        print(index)

###girilen sayının faktöriyelini alalım
###for ile
carpım=1
sayı = int(input("bana bir sayı ver:"))
for i in range(sayı,0,-1):
    carpım*=i
print(sayı)

#while ile
if sayı < 0:
    print("Negatif sayıların faktöriyeli tanımsızdır.")
else:
    sayı = int(input("bana bir sayı ver:"))
    i=1
    carpım=1
    while i<=sayı:
        carpım*=i
        i+=1
    print(carpım)

#####Kullanıcıdan pozitif bir sayı bekleyen,pozitifi de gördüğü an bastıran,negatif sayı girildikçe bir daha soran yapıyı kuralım(for döngüsü ile)
for i in range(100000):
    sayı = int(input("bana bir sayı ver:"))
    if sayı>0:
        print(sayı)
        break
    else:
        print("Negatif girdiniz, tekrar deneyin.")

#fonksiyon ile girilen sayının asal olup olmadığını (for) ile bulan kod dizisi
def asal_mı(sayı):
    if sayı < 2:
        return 'asal değil'
    for i in range(2, sayı):
        if sayı % i == 0:
            return 'asal değil'
    return "asal"

##fonksiyon ile girilen sayının asal olup olmadığını (while) ile bulan kod dizisi
def asal_mı(sayı):
    if sayı < 2:
        return "asal değildir"
    i = 2
    while i<sayı:
        if sayı%i==0:
            return "asal değildir"
        i+=1
    return "asaldır"

###fonksiyon ile sayının faktöriyelini alalım (for ile)
def faktoriyel_bul(sayı):
    if sayı < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır"
    carpım=1
    for i in range(sayı, 0, -1):
        carpım *= i
    return carpım

###fonksiyon ile sayının faktöriyelini alalım (while ile)
def faktoriyel(sayı):
    if sayı < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır."
    i=1
    carpım=1
    while i<=sayı:
        carpım*=i
        i+=1
    return carpım











