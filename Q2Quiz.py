# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
import json
with open("Question.json", "r") as f:
    Data = json.loads(f.read())

while True:

    print("")
    print(Data["Question"])
    print("\nAnswer 1:",(Data["Answers"][0]))
    print("Answer 2:",(Data["Answers"][1]))
    print("Answer 3:",(Data["Answers"][2]))
    print("Answer 4:",(Data["Answers"][3]))

    b = int(input("\nWhat is the correct answer \n(example: if the correct answer is (Answer 3) type 3)\nType your answer here: "))

    if b == (Data["Correct"]):
        print("\nWell done, your answer was correct! \n\n(Run the python file again if you would like to do the quiz again)\n")
        break
    elif b != (Data["Correct"]):
        print("\nIncorrect! Please try again!")
