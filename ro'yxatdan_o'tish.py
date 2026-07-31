malumot=[]
javob=input('Bu dasturdan foydalanish ro\'yhatdan o\'tishni talab qiladi,ro\'yhatdan o\'tishni hohlaysismi?\n:')
if javob =='ha':
    ism=input('Ismingizni kiriting:')
    familya=input('Familyangizni kiriting:')
    yosh=int(input('Yoshingizni kiriting:'))
    parol=int(input('Parol o\'ylab toping:'))   
    malumot.append(ism)
    malumot.append(familya)
    malumot.append(yosh)
    malumot.append(parol)
    print(f'Sizning ismingiz:{ism} \n Sizning familyangiz:{familya} \n Sizniing yoshingiz:{yosh} \n Sizning parolingiz:{parol}')
else: 
    print('Xayr salomat bo\'ling')