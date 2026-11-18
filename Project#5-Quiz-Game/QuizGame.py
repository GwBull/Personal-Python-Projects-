
from question_model  import question

from data import question_data

## this gets the question data from the question_model file and creates a list of question objects

question_bank = []

for question in question_data:
    ## this gets the question text and answer from the question_data list and creates a new question object
    ## this loop goes through the whole dictionary in the question_data list and creates a new question object for each question
    question_text = question["question"]
    ## this gets the correct answer from the question_data list and creates a new question object
    ## from the other file question_model.py
    ## the dictionary in that file is called question data and it contains the question text and the correct answer
    question_answer = question["correct_answer"]
    ## this creates a new question object using the question text and correct answer
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)

