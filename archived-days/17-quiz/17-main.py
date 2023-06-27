# Part 1 - Class Intro
# class User:
#     def __init__(self, user_id, name):
#         self.id = user_id
#         self.name = name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User('001', 'jack')
# user_2 = User('002', 'fran')
# user_1.follow(user_2)
#
# print(user_1.following)
# print(user_1.followers)
# print(user_2.following)
# print(user_2.followers)

# Project - Quiz Game
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

