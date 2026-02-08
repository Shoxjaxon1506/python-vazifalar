                        #Funfsiya yaratishga oid kodlar
def salom_ber():
    """salom beruvchi funksiya"""
    print('assalomu alaykum')

def salom_de(ism,familya):
    """ Foydalanivchidan ism va familya qabul qilib olib,
    unga salom beruvchi funksiya"""
    print(f'assalomu alaykum {familya.title()} {ism.title()} nima gaplar?')

def foydalanuvchi_malumoti(ism,familya,tugulgan_yil,boy,manzil):
    """Fpydalanuvchidan o'zi haqidagi malumotni oluvchi funksiya"""
    print(f'{ism.title()} {familya.title()} {tugulgan_yil} da tug\'ilgan,\n bo\'yi {boy} sm,{manzil.title()} da yashaydi.')

def yosh_hisoblash(ism,t_yil):
    """Fpydalanuvchi yoshini hisoblab beruvchi funksiya"""
    print(f'{ism.title()} ning yoshi {2026-t_yil} yoshda.')

def yosh_hisobla(t_yil,h_yil=2026):
    """Yoshni hisoblovchi funksiya"""
    print(f'siz {h_yil - t_yil} yoshdasiz.')