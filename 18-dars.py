                                                                                 While sikliga oid kodlar
print('Sinfdoshlar ro\'yxati:')
sinfdoshlar=[]
n=1
while True:
    savol = f'{n} inchi Sinfdoshingizni kiriting\n:'
    ism= input(savol)
    sinfdoshlar.append(ism)
    takror=input('Yana ism kiritishni xoxlaysizmi (ha\yoq)\n:')
    n+=1
    if takror !='ha':
        break
    
print('ismlar ro\'yxati:')
for sinfdosh in sinfdoshlar:
    sinfdosh=sinfdosh.title()    
    print(sinfdosh)

sinfdoshlar={}
ishora = True
while ishora:
        ism= input('Sinfdoshingizni ismini kiriting\n:')
        yosh=input(f'{ism.title()} ning yoshini kiriting\n:')
        sinfdoshlar[ism]=int(yosh)
        
        qoshimcha = input('Yana ism kiritishni xoxlaysizmi (ha\yoq)\n:')
        if qoshimcha == 'yoq':
            break
        
for ism, yosh in sinfdoshlar.items():
    print(f'{ism.title()} ning yoshi {yosh} yoshda')
kiyimlar=['kurtka','sharf','buruk','kurtka','etik','kurtka']
while 'kurtka' in kiyimlar:
      kiyimlar.remove('kurtka')
print(kiyimlar)
oquvchilar=['Hasan','Ulug\'bek','botir','ozod','javohir']
baholanganlar={}
while oquvchilar:
    oquvchi=oquvchilar.pop()
    oquvchi=oquvchi.title()
    baho=input(f'{oquvchi} ning bahosini kiriting\n:')
    print(f'{oquvchi.title()} baholandi')
    baholanganlar[oquvchi]=int(baho)
