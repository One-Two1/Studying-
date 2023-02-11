def reg_team():
    teameits,team_number = reg()
    Log_in(teameits,team_number)

def reg():
        team_name=input("Введите название комманды ")

        team_number=int(input("Введи количество участников.Количество участников должно быть не менее 2 и не более 8 "))
        while team_number <2 or team_number>8:
            print("Ошибка!")
            team_number = int(input("Введи количество участников.Количество участников должно быть не менее 2 и не более 8 "))
        teameits=""

        for item in range(team_number):
            teameits+=input("Напишите имя участника ")
        return teameits,  team_number

def Log_in(teameits,team_number):
        login=""
        for i in teameits:
            if i.isupper()==True:
                login+=i.lower()
        print("Ващ логин —",login)

        while True:
            password=input("Придумай безопасный пароль ")
            if len(password)<8:
                print("Ошибка! Пароль должен состоять минимум из 8 символов")
            forbidden_symbol="#%?@/"
            for i in password:
                for  j in forbidden_symbol:
                    if i==j:
                        print('Найден запрещенный симвод-',i)
            points=team_number*200
            print("Вам начислено",points,"баллов")

            break

reg_team()


