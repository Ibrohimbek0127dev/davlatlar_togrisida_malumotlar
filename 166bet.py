# AMALIYOT - 166 -BET

#-------------------------------------------------------------------------------#

#1.1) Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashhur shaxslar haqidagi
#ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang
#va har bir shaxs haqidagi ma'lumotni konsolga chiqaring:
print("! Tarixda yashab o'tgan 4 buyuk alloma !")
al_buxoriy = {
    'ism':'abu abdulloh muhammad ibn ismoil',
    't_yil':810,
    't_shaxar':'buxoro',
    'yashagan':60
}

abdulla_qodiriy = {
    'ism':'abdulla qodiriy',
    't_yil':1894,
    't_shaxar':'toshkent',
    'yashagan':44
}

erkin_vohidov = {
    'ism':'erkin vohidov',
    't_yil':1936,
    't_shaxar':'farg\'ona',
    'yashagan':80
}

alisher_navoiy = {
    'ism':'alisher navoiy',
    't_yil':1441,
    't_shaxar':'xirot',
    'yashagan':60
}
buyuk_alloma = [al_buxoriy, abdulla_qodiriy, erkin_vohidov, alisher_navoiy]
for alloma in buyuk_alloma:
    print(f"{alloma['ism'].title()}, {alloma['t_yil']} - yilda "
          f"{alloma['t_shaxar'].capitalize()}da tavallud topgan. "
          f"{alloma['yashagan']} yil umr ko'rgan")

#---------------------------------------------------------------------------------#

#1.2) Yuqoridagi lug'atlarga xar bir shaxsning mashhur asarlari ro'yxatini ham
#qo'shing. FOR sikli yordamida muallifning ismi va uning asarlarini
#konsolga chiqaring:
print("\n! Tarixda yashab o'tgan 4 buyuk allomalarning asarlari !")
buyuk_alloma_asarlari = {
    'abu abdulloh muhammad ibn ismoil': ["al-jome' as-sahih", "al-adab al-mufrad", "at-tarix al-kabir", "at-tairx as-sag'ir"],
    'abdulla qodiriy':["o'tkan kunlar", "mehrobdan chayon", "obid ketmon"],
    'erkin vohidov':["tong nafasi", "qo'shiqlarim sizga", "o'zbegim", "qiziquvchan matmusa"],
    'alisher navoiy':["xamsa", "lison ut-tayir", "mahbub al-qulub", "munojot"]
}

for ism, asarlar in buyuk_alloma_asarlari.items():
    print(f"{ism.title()}ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar.title())
    print('\n', end='')


#--------------------------------------------------------------------------------------------#

#1.3) Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali
#haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolari esa
#ro'yxat ko'rinishida lug'atga saqlang. Natijani konsolga chiqaring:
print("! Do'stlarimning 3 ta sevimli kinolari !")
kinolar= {
    'ali':['terminator', 'rambo', 'titanic'],
    'vali':['tenet', 'inception', 'interstellar'],
    'hasan':['abdullajon', 'bomba', 'shaytanat'],
    'husan':['mahallada duv-duv gap', 'john wick']
}
for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolai: ")
    for kino in kinolar:
        print(f"{kino.title()}")


#1.4) Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar
#haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni
#konsolga chiqaring:
print("\n! Davlatlar haqida ma'lumotlar !")
davlatlar = {
    "o'zbekiston": {
        'poytaxti':'toshkent',
        'hududi':4_489_78,
        'aholisi':33_000_000,
        'pul birligi':"so'm"

},
    "rossiya": {
        'poytaxti': 'moskva',
        'hududi': 170_98_236,
        'aholisi':144_000_000,
        'pul birligi': "rubl"

    },
    "aqsh": {
        'poytaxti': 'vashington',
        'hududi': 9_631_418,
        'aholisi':327_000_000,
        'pul birligi': "dollar"

    },
    "malaziya": {
        'poytaxti': 'kuala-lumpur',
        'hududi':329_750,
        'aholisi':25_000_000,
        'pul birligi': "rinngit"

    }
}
for davlat, info in davlatlar.items():
    if davlat.lower() == 'aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxti'].title()}"
          f"\nHududi: {info['hududi']} kv.km"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul birligi']}")


#--------------------------------------------------------------------------------#

#1.5) Yuqoridagi dasturga o'gartirish kiriting: konsolga barcha davlatlar emas,
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa,
#"Bizda bu davlat haqida ma'umot yo'q" degan xabarni chiqaring:
print("\n! Davlatlar to'g'risida ma'lumot beruvchi dasturga xush kelibsiz !")
davlatlar = {
    "o'zbekiston": {
        'poytaxti':'toshkent',
        'hududi':4_489_78,
        'aholisi':33_000_000,
        'pul birligi':"so'm"

},
    "rossiya": {
        'poytaxti': 'moskva',
        'hududi': 170_98_236,
        'aholisi':144_000_000,
        'pul birligi': "rubl"

    },
    "aqsh": {
        'poytaxti': 'vashington',
        'hududi': 9_631_418,
        'aholisi':327_000_000,
        'pul birligi': "dollar"

    },
    "malaziya": {
        'poytaxti': 'kuala-lumpur',
        'hududi':329_750,
        'aholisi':25_000_000,
        'pul birligi': "rinngit"

    }
}

user = input("Istalgan davlat nomini kiriting: ").lower()
if user.lower() == 'aqsh':
    info = davlatlar[user]
    print(f"\n{user.upper()}ning poytaxti {info['poytaxti'].title()}\n"
          f"Hududi: {info['hududi']} kv.km\n"
          f"Aholisi: {info['aholisi']}\n"
          f"Pul birligi: {info['pul birligi']}")
elif user in davlatlar:
    info = davlatlar[user]
    print(f"\n{user.capitalize()}ning poytaxti {info['poytaxti'].title()}\n"
              f"Hududi: {info['hududi']} kv.km\n"
              f"Aholisi: {info['aholisi']}\n"
              f"Pul birligi: {info['pul birligi']}")
else:
    print(f"Uzr, bizda hali \"{user}\" davlati to'g'risida ma'lumot yo'q :(")
