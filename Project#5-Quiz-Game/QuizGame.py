
from question_model  import question

from data import question_data

## this gets the question data from the question_model file and creates a list of question objects

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)

