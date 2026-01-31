                                     # 1-ish
sinfdosh={'ism' : 'Ozod', 'familya' : 'Sattorov', 'yosh' : 17, 'bo\'y' : 175}
sinfdosh1={'ism' : 'Bobur','familya' : 'Shapatov','yosh' : 16, 'bo\'y' : 170}
sinfdosh2={'ism' : 'Javohir','familya' : 'Turduqulov','yosh' : 15, 'bo\'y' : 160}
sinfdosh0=sinfdosh2
print(f'{sinfdosh0["ism"]} {sinfdosh0["familya"]} ning yoshi {sinfdosh0["yosh"]} ga teng,'
      f'bo\'yi {sinfdosh0["bo\'y"]} sm ga teng')
                              # Qulayroq varianti
sinfdosh0=[sinfdosh,sinfdosh1,sinfdosh2]
for sinfdo in sinfdosh0:
    print(f'{sinfdo["ism"]} {sinfdo["familya"]} ning yoshi {sinfdo["yosh"]} ga teng,'
          f'bo\'yi {sinfdo["bo\'y"]} sm ga teng')
                                      # 2-ish
zavod=[]
for t in range(10):
    yangi_mashina={
        'nomi' : 'Gentra',
        'yili' : None,
        'rangi' : None,
        'yurgani' : 0,
        'narxi' : None
        }
    zavod.append(yangi_mashina)
for gentracha in zavod[:4]:
    gentracha['rangi']='Oq'
    gentracha['yili']=2020
for gentracha in zavod[4:7]:
    gentracha['yili']=2024
    gentracha['rangi']='qizil'
for gentracha in zavod[7:10]:
    gentracha['rangi']='sariq'
    gentracha['yili']=2025

for gentracha in zavod:
    print(gentracha)
for gentracha in zavod:
    if    gentracha['rangi']=='sariq':
          gentracha ['narxi']=50
    elif  gentracha['rangi']=='Oq':
          gentracha['narxi']=45
    else: gentracha['narxi']=30

for gentracha in zavod:
    print(gentracha)
                                      # 3-ish     
dostlar={
    'Hasan' : ['uy','mashina'],
    'Husan' : ['telefon','planshet'],
    'Tohir' : ['noutbuk','uy']
    }
for ism,buyumlar in dostlar.items():
    print(f'\n{ism} da {buyumlar} bor')    

