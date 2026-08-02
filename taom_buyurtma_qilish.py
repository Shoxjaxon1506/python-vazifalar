                       #Taom  buyurtma qilish
menu=['osh','manti','shashlik','kavob','sho\'rva','choy','non','salat','pepsi']
buyurtmalar=[]
while True:
    buyurtma=input('Nima buyurtma qilasiz:')
    if buyurtma=='yoq':
        break
    buyurtmalar.append(buyurtma)
if not buyurtmalar:
    print('Sinzning savatingiz bo\'sh')
else:
    for taom in buyurtmalar:
        if taom in menu:
            print(f'Sizning {taom} buyurtmangiz qabul qilindi')
        else:
            print(f' Bizda {taom} yoq')