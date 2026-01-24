                                  #1-mashq
sinfdosh={'ism':'javohir','yosh':'17','bo\'y':170}
print(f'mening sinfdoshim {sinfdosh["ism"].title()} ning yoshi {sinfdosh["yosh"]} yosh,\
 # bo\'yi {sinfdosh["bo\'y" ]} sm')
print(sinfdosh['ism'])
                                  # 2-mashq
dost={}
dost['ism']='ozod'.title()
dost['ism2']='bobur'.title()
print(f'kecha {dost["ism"]} bilan {dost["ism2"]} bir birini go\'shini yedi')
                     # Lug'atdan ba'zi bir ma'lumotni o'chirish uchun
del sinfdosh['ism']
                     #Lug'atda yo'q so'z yozilgan taqdirda
maktab=sinfdosh.get('familya','bunday ism mavjut emas')
print(maktab)

                