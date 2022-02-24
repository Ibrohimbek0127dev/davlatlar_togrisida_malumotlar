# MUSTAQIL - AMALIYOT

print("! Davlatlar to'g'risida ma'lumot beruvchi dasturga xush kelibsiz !")
davlatlar = {
    "o'zbekiston": {
        'poytaxti': 'toshkent',
        'hududi': 4.489_78,
        'aholisi': 33.000_000,
        'pul birligi': "so'm"

    },
    "rossiya": {
        'poytaxti': 'moskva',
        'hududi': 170.98_236,
        'aholisi': 144.000_000,
        'pul birligi': "rubl"

    },
    "aqsh": {
        'poytaxti': 'vashington',
        'hududi': 9.631418,
        'aholisi': 327.000_000,
        'pul birligi': "dollar"

    },
    "malaziya": {
        'poytaxti': 'kuala-lumpur',
        'hududi': 329.750,
        'aholisi': 25.000_000,
        'pul birligi': "rinngit"

    },
    "koreya": {
        'poytaxti': 'seul',
        'hududi': 100.363,
        'aholisi': 51.709098,
        'pul birligi': "won"

    },
    "skoreya": {
        'poytaxti': 'pyongyang',
        'hududi': 120.540,
        'aholisi': 25.549_604,
        'pul birligi': "won"

    },
    "saudiya": {
        'poytaxti': 'ar-riyod',
        'hududi': 2.149_690,
        'aholisi': 34.218_169,
        'pul birligi': "saudiya riyali"

    },

    "turkiya": {
        'poytaxti': 'anqara',
        'hududi': 783.356,
        'aholisi': 84.680_273,
        'pul birligi': "turk lirasi"

    }

}

try:
    mavjud_davlatlar_royxati = ["o'zbekiston", "rassiya", "aqsh", "malaziya", "koreya", "saudiya", "turkiya"]
    user1 = True
    while user1:
        users = input("\nIltimos, dasturdan foydalanish uchun ismingizni kiriting: ")
        if users.strip().isdigit():
            print("Iltimos, faqat harflardan iborat so'z kiriting :)")
        elif len(users) < 3:
            print("Iltimos, Ismingiz 3 ta harfdan ko'p bo'lsin :)")
        elif len(users) >= 3:
            print("\n'Y' (ha) | 'X' (yo'q) tanlang")
            n = input(f"Sizni Janob \"{users.upper()}\" deb chaqirishimga qarshi emasmisiz?: ").lower()
            if n == 'y':
                break
            elif n == 'x':
                print(f"\nAgar men sizni \"{users.upper()}\" deb chaqishimga qarshi bo'lsangiz unda boshqa ism tanlang :(")

    print("\nUshbu dastur o'zbek tilida !!! Faqat lotin harflaridan foydalaning :)")
    user = True
    while user:
        print("\nMavjud davlatlar ro'yxatini ko'rish uchun \"h\" ni bosing")
        print("Dasturni to'xtatish uchun 'x' ni bosing :)")
        user = input("\nIstalgan davlat nomini kiriting: ").lower()

        if user.lower() == 'aqsh':
            info = davlatlar[user]
            print(f"\n{user.upper()} davtati to'g'risida qisqagina ma'lumot: ")
            print(f"{user.upper()} davlatining poytaxti: {info['poytaxti'].title()}\n"
                  f"Hududi: {info['hududi']} kv.km\n"
                  f"Aholisi: {info['aholisi']}\n"
                  f"Pul birligi: {info['pul birligi']}\n")

        elif user.lower() == 'koreya':
            a = input("\"(a)Janubiy\" yoki \"(b)Shimoliy\"?: ")
            if a.lower() == 'a':
                info = davlatlar[user]
                print(f"\nJanubiy {user.title()} davlati to'g'risida qisqagina ma'lumot: ")
                print(f"Janubiy {user.capitalize()} davlatining poytaxti: {info['poytaxti'].title()}\n"
                      f"Hududi: {info['hududi']} kv.km\n"
                      f"Aholisi: {info['aholisi']}\n"
                      f"Pul birligi: {info['pul birligi']}\n")

            elif a.lower() == 'b':
                info = davlatlar['skoreya']
                print(f"\nShimoliy {user.title()} davlati to'g'risida qisqagina ma'lumot: ")
                print(f"Shimoliy {user.capitalize()} davlatining poytaxti: {info['poytaxti'].title()}\n"
                      f"Hududi: {info['hududi']} kv.km\n"
                      f"Aholisi: {info['aholisi']}\n"
                      f"Pul birligi: {info['pul birligi']}\n")
        elif user == 'h':
            print(f"\nXozirda ma'lumot olishingiz mumkin bo'lgan davlatlar ro'yxati:")
            print(mavjud_davlatlar_royxati, '\n')

        elif user.lower() == 'x':
            break

        elif user.strip().isdigit():
            print("\nIltimos, faqat harflardan iborat so'z kiriting :)")

        elif user in davlatlar:
            info = davlatlar[user]
            print(f"\n{user.capitalize()} davtati to'g'risida qisqagina ma'lumot: ")
            print(f"{user.capitalize()} davlatining poytaxti: {info['poytaxti'].title()}\n"
                  f"Hududi: {info['hududi']} kv.km\n"
                  f"Aholisi: {info['aholisi']}\n"
                  f"Pul birligi: {info['pul birligi']}\n")
        else:
            print(f"\nUzr, bizda hali \"{user.title()}\" davlati to'g'risida ma'lumot yo'q :(")

    print(f"\nDastur to'xatildi. Foydalanganingiz uchun tashakkur Janob {users.title()} :)")
except:
    print("Uzr, dastur ishdan chiqdi :(")
