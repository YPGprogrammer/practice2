import random


def better_victory():
    while True:
        # Used dict to easy access for names and b-days
        victory_names_list = {'Илон Маск': '28.06.1971', 'Джефф Безос': '12.01.1964', 'Билл Гейтс': '28.10.1955',
                        'Марк Цукерберг': '14.05.1984', 'Сэм Альтмэн': '22.04.1985' , 'Виталий Бутерин': '31.01.1994',
                        'Чанпэн Чжао': '10.09.1977', 'Гвидо Ван Россум': '31.01.1956', 'Алан Тьюринг': '23.06.1912',
                        'Стивен Хокинг': '8.01.1942'}

        # Created a set to exclude repeating
        random_names = set()

        # Created a loop where randomed chosen names will be added to a set until it has five elements
        while len(random_names) < 5:
            random_names.add(random.choice(list(victory_names_list.keys())))

        # Turned a set to a list for easy acces to it
        random_names = list(random_names)
        print("Выбранные имена:", random_names)

        # score metrics
        correct = 0
        incorrect = 0

        # loop for  main work. it's starting to watch over a list of random names in it's length range
        # firstly it's printing a message to write down b-day of a chosen name
        # then user must write it down in a correct format. This is why input type is str
        # is user writes down incorrect answer the programm will print a correct one using a function .get
        # and random_names[i] as a value for dict
        # after user entering an answer one of the metrics gets 1 point
        for i in range(len(random_names)):
            print('Введите дату рождения в формате "dd.mm.year" для', random_names[i], ':')
            user_input = str(input())
            if user_input in victory_names_list.values():
                print('Ответ правильный!')
                correct += 1
            else:
                print("Ответ неправильный! Правильный ответ:", victory_names_list.get(random_names[i]))
                incorrect += 1

        print('Количество правильных ответов:', correct)
        print('Количество неправильных ответов:', incorrect)
        user_answer = str(input('Хотите попробовать еще раз? Да/Нет '))
        if user_answer == 'Да' or 'да':
            continue
        else:
            break


better_victory()