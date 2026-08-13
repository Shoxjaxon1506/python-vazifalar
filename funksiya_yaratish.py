                           #Funksiya
def malumot_oluvchi():
    """ Foydalanuvchidan  malumot olib ro'yxarga qo'shuvchi funksiya"""
    malumot=[]
    print('Assalomu alaykum biz sizdan malumot olamiz')
    ism=input('ismingizni kiriting:')
    malumot.append(ism.title())
    familya=input('familyangizni kiriting:')
    malumot.append(familya.title())
    yosh=int(input('yoshingizni kiriting:'))
    malumot.append(yosh)
    print('malumotlar muvaffaqiyatli saqlandi!!')
    savol=input('Yana malumot qo\'shishni hohlaysizmi?\n masalan:bo\'y,vazn\n:')
    if savol =='ha':
        boy=int(input('bo\'yingiz necha sm:'))
        malumot.append(boy)
        vazn=int(input('vazningiz qancha:'))
        malumot.append(vazn)
        print(f'{familya.title()} {ism.title()} yoshi {yosh}da, bo\'yi {boy}sm,vazni{vazn}kg')
    else:
        print('Xayr salomat bo\'ling')


def malumot_ol(ism,familya,yosh=18):
    """ foydalanuvchidan o\'zi haqidagi malumotni oladi"""
    print(f'{ism.title()} {familya.title()} ning yoshi {yosh} da ')