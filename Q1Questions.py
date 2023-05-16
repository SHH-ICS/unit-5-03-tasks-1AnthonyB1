# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
import json

Question = input("\nWhat is your multiple choice question?\n(Example Question: What is 1 + 1)\nType your own question here: ")

print('')
A = []
for i in range(4):
    A.append(input(f"Answer {i + 1}: "))

Correct = int(input("\nCorrect Index: "))

myJson = {"Question":Question, "Answers":A, "Correct":Correct}

with open("Question.json", "w") as f:
    f.write(json.dumps(myJson))