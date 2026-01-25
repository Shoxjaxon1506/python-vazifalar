                               #1-mashiq
sinfdosh={
    'ism':'Bobur',
    'familya':'Shapatov',
    'yosh':17,
    'bo\'y':172,
    'vazn':60   }
print(f'sinfdoshim {sinfdosh["ism"]} {sinfdosh["familya"]} ning yoshi {sinfdosh["yosh"]} ga teng.\n Bo\'yi {sinfdosh["bo\'y"]} ga teng.\n Vazni {sinfdosh["vazn"]} kg ga teng')
                                #2-mashiq
for Kalit,Qiymat in sinfdosh.items():
    print(f'Kalit : {Kalit}')
    print(f'Qiymat : {Qiymat}\n')
                                #3-mashq
kiyimlar={
    'Bobur' : 'koylak',
    'Ozod' : 'buruk',
    'Javohir' : 'fudbolka'
    }
for k,q in kiyimlar.items():
    print(f'{k}da {q} bor\n')
                               #4-mashq
kiyimlar={'buruk': 60000,'oq ko\'ylak': 75000,'kastyum': 120000,'burukcha': 60000}
xaridlar=['galistyuk','buruk','jensi','kastyum','ko\'ylak']
for kiyim in kiyimlar:
    if kiyim in xaridlar:
        print(f'{kiyim} {kiyimlar[kiyim]} so\'m')
for narsa in xaridlar:
    if narsa not in kiyimlar:
        print(f'iltimos do\'koningizga {narsa} ham olib keling')
                               #5-mashq
print('do\'kondagi kiyimlar:')
for kiyim in sorted(kiyimlar):
    print(kiyim.title())
                # Ro'yxatdagi faqat qiymatni chiqarish uchun
      #print(kiyimlar.values())
print('bozordagi kiyimlar narxi:')
for kiy in kiyimlar.values():
    print(kiy)
#bir nechta bir xil kalitlarni ortiqchasini olib tashlash uchun
print( set(kiyimlar.values()))