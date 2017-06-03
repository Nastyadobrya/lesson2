def  get_answer(ans):
    while True:
        if ans == 'Хорошо':
            print('Ну и славненько')
            break
        else:
            ans = str(input('Как дела?  '))
def  user_ask(q):
    while True:
        if q == 'Пока!':
            print('До скорой встречи!')
            break
        else:
            q = str(input('Сам разберешься с этим! Еще вопросы?'))
answer = str(input('Привет! Как жизнь?   '))
get_answer(answer)
question = str(input('Спрашивай о че хотел:)   '))
user_ask(question)
