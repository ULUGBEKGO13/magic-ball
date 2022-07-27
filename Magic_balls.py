import random
choice = 'yes'
def is_valid(choice):
    while not(choice.isalpha()):
        print('Хотите ли вы задать еще один вопрос? "YES" или "NO"')
        choise = input()
    else:
        while choice.lower() != 'yes' and choice.lower() != 'no':
            print('Хотите ли вы задать еще один вопрос? "YES" или "NO"')
            choice = input()
        else:
            return choice.lower()
def is_valid_question(question):
    while not(question.isalnum()):
        print('Может быть вы зададите нормальный вопрос вместо непонятных символов #$/*№!')
        question = input()
    else:
        return question
answer = ['беспорно', 'предрешено', 'никаких сомнений', 'определённо да', 'можешь быть уверен в этом', 'мне кажется - да', 'вероятнее всего', 'хорошие преспективы', 'знаки говорят - да', 'да', 'пока неясно, попробуй снова', 'спроси позже', 'лучше не рассказывать', 'сейчас нельзя предсказать', 'сконцентрируйся и спроси опять', 'даже не думай', 'мой ответ - нет', 'по моим дванным - нет', 'преспективы не очень хорошие', 'весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как к вам обращаться?')
print('Привет ' + name)
while choice == 'yes':
    print('Ожидаю вашего вопроса!')
    question = ''.join(input().split())
    question = is_valid_question(question)
    print(random.choice(answer))
    print('Хотите ли вы задать еще один вопрос? "YES" или "NO"')
    choice = input()
    choice = is_valid(choice)
else:
    print('Возвращайся если возникнут вопросы!')
