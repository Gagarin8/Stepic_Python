import random

answers =   ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
             "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
             "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
            "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", 
            "Перспективы не очень хорошие", "Весьма сомнительно"
            ]

def welcome():            
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Напишите,как Вас зовут:')
    name = input()
    print('Привет,', name.title(), '!')
    start_game()


#Начало игры
def start_game():        
    print('Задайте вопрос Магическому шару:')
    input()
    print(random.choice(answers))
    game_again()
        

#Играть заново
def game_again():
    print('Есть еще вопросы?')
    print('Нажмите "д", если нет - нажмите "н":', end=' ')
    answer = input().lower()
    if answer == 'д':
        start_game()
    elif answer == 'н':
        finish_game()
    else:
        print('Что за кракозябру Вы ввели?')
        game_again()


#Конец игры
def finish_game():
    print('Возвращайся если возникнут вопросы!')


welcome()