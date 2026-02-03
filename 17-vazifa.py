ishchilar={
    'Temur' : {
        'Familya' : 'Farxodov',
        'yosh' : 35,
        "bo\'yi" : 185,
        'yashash_manzili' : 'Chirchiq'
        },
    'Olim' : {
        'Familya' : 'Jumayev',
        'yosh' : 40,
        'bo\'yi' : 176,
        'yashash_manzili' : 'Oqqovoq'
        }
        }
for ism,malumot in ishchilar.items():
    print(f'\n{ism.title()} {malumot["Familya"].title()},'
          f'Yoshi {malumot["yosh"]} da, bo\'yi {malumot["bo\'yi"]} sm ga teng,'
          f'{malumot["yashash_manzili"]} da yashaydi.')
ism=input('ismingiz nima:')
savol=f'Salom {ism.title()},Yoshingiz nechchida:\n'
yosh=int(input(savol))
print(f'zo\'rku menikiham {yosh} yoshda')
boy=float(input('bo\'yingizni kiriting:'))
#print(f'Ha {ism.title()} san haqingdagi hamma narsani bilib oldim ha ha ha ')
son=1
while son<=10:
    print('salom')
    son +=1
print('sonlarni kvadratini aytib beraman')
savol='istalgan son kiriting'
savol += '(Dastur to\'xtashi uchun "stop" deb yozing):'
qiymat=''
while qiymat !='stop':
    qiymat=input(savol)
    if qiymat !='stop':
        print(float(qiymat)**2)
 print('dastur tugadi!!!')
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat=='stop':
        ishora= False
    else:
        print(float(qiymat)**2)
 print('Dastur tugadi')
while True:
    qiymat=input(savol)
    if qiymat=='stop':
        break
    else:
        print(float(qiymat)**2)
print('Dastur tugadi')
sonlar=list(range(1,15))
for son in sonlar:
    if son==10:
        continue
    else:
        print(f'{son} ning kvadrati {son**2} ga teng')
son=0
while son<=10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)