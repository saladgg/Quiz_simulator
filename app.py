from Questions import Questions

question_prompts = [
    "Sun rises from? \n(a) East \n (b) South \n (c) West \n (d) North\n\n",
    "What is the name of kenya\'s capital city? \n (a) Addis\n (b) Nairobi\n (c) Daresalaam\n (d) Kigali\n\n",
    "Which is the biggest tech  \n (a) Intel\n (b) Microsoft\n (c) Apple\n (d) IBM\n\n",
    "Who is the founder of facebook?\n (a) Alibaba\n (b) Elon Musk\n (c) Bill Gates\n (d) Zuckerberg\n\n"
]

questions = [
    Questions(question_prompts[0],"a"),
    Questions(question_prompts[1],"b"),
    Questions(question_prompts[2],"c"),
    Questions(question_prompts[3],"d")
]


def run_test(test_questions):
    score = 0
    answers = ["a","b","c","d"]
    for question in test_questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
        elif answer == "":
            print("Please enter your answer")
            input(question.prompt)
        elif answer != range(1,len(answers)):
            print("Your answer must be in form of a,b,c or d")
        else:
            print("Interesting!")

    print("You got "+str(score)+ "/" + str(len(test_questions))+ " Correct")
    print("Your score is "+str(score/len(test_questions)*100)+" %")

run_test(questions)