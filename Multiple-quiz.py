class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


QuestionsList = ['Which combination creates Purple?\na. Red & Blue\nb. Red & Orange\nc. Green & Yellow\n\n',
                 'Who is the author of The Handmaid\'s tale?\na. Chide Lee\nb. Ailee Cherrot\nc. Margaret Atwood\n\n',
                 'Who was Elizabeth Schuyler\'s husband?\na. Alexander Hamilton\nb. Oliver Stone\nc. Macquire Linn\n\n'
                 ]

questionData = [question(QuestionsList[0], 'a'),
                question(QuestionsList[1], 'c'),
                question(QuestionsList[2], 'a')]


def run_test(questions):
    score = 0
    for question in questions:
        user = input(question.prompt)
        if user == question.answer:
            score += 1

    print('You got ' + str(score) + '/' + str(len(QuestionsList)))


run_test(questionData)
print(input('Press to exit'))

