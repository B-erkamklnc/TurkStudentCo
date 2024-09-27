while True:
    try:
        boyut = int(input('Kaç elemanlı bir dizi oluşturmak istersiniz?: '))
        break
    except:
        print('Sanırım tam sayı girmek yerine kelime veya kesirli sayı girdin.' +
              '\nHadi tekrar başlayalım.')
        
dizi = []

for i in range(boyut):
    dizi.append(input(f'Dizinin  {i}. elemanını giriniz: '))

# elemanların tekrar etemsi, dizide farklı indislerde aynı iki elemanın bulunması
# olarak yorumlanmıştır. Örneğin Liste = [1,2,3,1] dizisinin elemanları tekrar eder.

if len(dizi) == len(set(dizi)):
    print(dizi, '\nElemenaları benzersiz bir dizidir!')
else:
    print(dizi, '\nElemenalarının bir veya birden fazlası tekrar eden bir dizidir!')
