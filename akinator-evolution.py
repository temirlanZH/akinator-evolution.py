import random
import numpy as np

color = ["красный", "розовый", "фиолетовый", "черный", "белый", "серый",
         "зеленый", "синий", "коричневый", "желтый", "голубой", "оранжевый",
         "лаймовый", "бирюзовый", "темно-зеленый", "пурпурный", "светло-серый"]

# Вопросы
questions = [
    ["Яблоко может быть вашего цвета?", 35, False, 0],
    ["Небо может быть вашего цвета?", 20, False, 0],
    ["Лес может быть вашего цвета?", 50, False, 0],
    ["Ваш цвет это цвет снега?", 40, False, 0],
    ["В вашем цвете 7 букв?", 50, True, 0],
    ["Ваш цвет светлый?", 30, False, 0],
    ["Панда может быть вашего цвета?", 60, True, 0],
    ["Ваш цвет популярен у фруктов?", 40, False, 0],
    ["Ваш цвет похож на воду?", 40, True, 0],
    ["Ваш цвет женский?", 40, False, 0],
    ["Ваш цвет как у бетона?", 50, True, 0],
    ["Ваш цвет редкий?", 60, False, 0],
    ["Листья могут быть вашего цвета?", 40, False, 0],
    ["Ваш цвет состоит из двух слов?", 80, True, 0],
    ["Ваш цвет градация основных цветов?", 50, False, 0],
    ["Ваш цвет часто встречается в жизни?", 40, False, 0],
    ["Ваш цвет есть в логотипе Билайна?", 60, True, 0],
    ["Ваш цвет лаймовый или оранжевый?", 100, True, 0],
    ["Ваш цвет состоит из 9+ букв?", 70, True, 0],
]

full_answers_if_true = []

good_answers = ["Да", "Д", "Y", "Yes", 1, "1", "11"]


def auto_balls():
    for i in range(len(questions)):
        solo_answers = []
        answer = ""
        while answer != "с":
            answer = input(questions[i][0])
            solo_answers.append(answer)
        full_answers_if_true.append(solo_answers)

    return full_answers_if_true


# print(auto_balls())

full_answers_if_true = [['красный', 'зеленый', 'желтый', 'коричневый', 'с'],
                        ['голубой', 'синий', 'бирюзовый', 'фиолетовый',
                         'розовый', 'красный', 'пурпурный', 'черный', 'с'],
                        ['зеленый', 'темно-зеленый', 'коричневый', 'с'],
                        ['белый', 'серый', 'черный', 'желтый', 'с'],
                        ['красный', 'розовый', 'зеленый', 'голубой', 'с'],
                        ['красный', 'розовый', 'белый', 'желтый', 'голубой', 'оранжевый',
                         'лаймовый', 'бирюзовый', 'пурпурный', 'светло-серый', 'с'],
                        ['черный', 'белый', 'с'],
                        ['красный', 'зеленый', 'желтый',
                         'оранжевый', 'лаймовый', 'с'],
                        ['синий', 'голубой', 'бирюзовый', 'с'],
                        ['розовый', 'голубой', 'пурпурный', 'бирюзовый', 'с'],
                        ['серый', 'светло-серый', 'с'],
                        ['пурпурный', 'лаймовый', 'бирюзовый', 'с'],
                        ['красный', 'желтый', 'зеленый', 'с'],
                        ['темно-зеленый', 'светло-серый', 'с'],
                        ['розовый', 'оранжевый', 'серый',
                         'светло-серый', 'бирюзовый', 'с'],
                        ['красный', 'черный', 'белый',
                         'зеленый', 'синий', 'серый', 'с'],
                        ['черный', 'желтый', 'с'],
                        ['лаймовый', 'оранжевый', 'с'],
                        ['фиолетовый', 'коричневый', 'темно-зеленый', 'пурпурный', 'светло-серый', 'с']]


def questions_rebrend(full_answers_if_true):
    for i in range(len(full_answers_if_true)):
        for j in range(len(full_answers_if_true[i])):
            full_answers_if_true[i][-1] = questions[i][1]
    return full_answers_if_true


def akinator():
    count = [0] * len(color)
    not_end = False

    def quenstions_choose(answer_index):
        answer = input(questions[answer_index][0])

        for j in range(len(full_answers_if_true[answer_index])):
            for k in range(len(color)):
                if answer in good_answers:
                    if full_answers_if_true[answer_index][j] == color[k]:
                        count[k] += full_answers_if_true[answer_index][-1]

                        # добавим приоретет некоторым вопросам
                        questions[k][3] += 1
                        # print(questions[k])
                else:
                    # if full_answers_if_true[answer_index][j] == color[k]:
                    count[k] += full_answers_if_true[answer_index][-1] * 0.1
                    if questions[k][2] == True:
                        count[k] = count[k] * 0.5
        return count

    def questions_action():
        global question_past
        question_past = []

        answer_index = 0
        for number_of_quenstions in range(len(questions)):
            if max(count) <= 135:
                # акинатор первые 5 вопросов выставляет приорететы
                if number_of_quenstions <= 3:
                    # print("Акинатор зашел в обучение, попытка ", number_of_quenstions)
                    # убираем дубликаты вопросов
                    answer_index = random.randint(0, len(questions) - 1)
                    # print(answer_index)
                    # print(questions[answer_index])
                    if questions[answer_index][0] not in question_past:
                        # print(question_past)
                        question_past.append(questions[answer_index][0])
                        quenstions_choose(answer_index)

                # дальше, он ориентируется на ответы 5 вопросов
                else:
                    prioretets = []
                    for i in range(len(questions)):
                        prioretets.append(questions[i][3])

                    prioretets = np.array(prioretets)
                    index_of_best = prioretets.argsort()[-8:][::-1]
                    index_of_best = list(index_of_best)
                    for i in range(len(index_of_best)):
                        if questions[index_of_best[i]][0] not in question_past:
                            # print(count)
                            # print(questions[index_of_best[i]])
                            question_past.append(
                                questions[index_of_best[i]][0])
                            quenstions_choose(index_of_best[i])

        # print(str(color[count.index(max(count))]))

        return count

    def final():
        for i in range(len(count)):
            if count[i] == max(count):
                ask = input("Ваш цвет - " +
                            str(color[i]) + "?")
                count[i] = - count[i]
                if ask in good_answers:
                    print("Я угадал твой цвет :)")
                    return count
            else:
                print(count)
                print(color)
                print("Игра продолжается")
                # продолжаем игру и нулируем шанс выпадения того же цвета
                questions_action()
                not_end = True

    questions_action()
    final()
    if not_end:
        print("Я думаю твой цвет")
        print(color.index(max(count)))
    return count


if __name__ == "__main__":
    while input("Сыграем?") in good_answers:
        full_answers_if_true = questions_rebrend(full_answers_if_true)
        count = akinator()
        print(count)
        print(color)