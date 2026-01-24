menu=['non','chuchvara','osh','shashlik','lavash','sho\'rva','choy']
#ovqat= input('Ovqat turini kiriting:')
#if ovqat.lower() in menu:   
 #   print('Buyurtmangiz qabul qilindi')
#else:
#    print('Afsuski bizda bunday turdagi ovqat yoq!!')
buyurtmalar=['osh','manti','norin','lavash','choy','grel']
for ovqat in buyurtmalar:
    if ovqat in menu:
        print(f'Bizning menuda {ovqat} bor')
    else:
        print(f'Bizning menuda bunday turdagi {ovqat} ovqati yoq')