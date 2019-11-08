'''
Also Refer Question.py
We will build a MCQ quiz, keep track of scores, and tell the score at the end to user.
'''
from Question import Question

question_prompts = [
    'What color are Bananas?\n(a) Red\n(b) Yellow\n(c) Black\n',
    'What color are Strawberries?\n(a) Red\n(b) Yellow\n(c) Black\n',
    'What color is night?\n(a) Red\n(b) Yellow\n(c) Black\n'
]

questions = [
    Question(question_prompts[0], 'b'),
    Question(question_prompts[1], 'a'),
    Question(question_prompts[2], 'c')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct.')

run_test(questions)