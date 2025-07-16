# Flashcard Quiz App
import random

#mapping Keys (Questions) to (:) Values (Answers)
flashcards =     {"How many times have PSG won the UCL (enter as one word)" : "Once",
                  "Who won the Golden Boy award in 2021?" : "Pedri",
                  "How many PL goals did Erling Haaland score in 22/23?" :  "36",
                  "Who is the youngest goalscorer in the UCL?" : "Ansu Fati",
                  "What is Liverpool's main colour?" : "Red"}

def play_quiz():
    print("------------------------------------------")
    print("WELCOME TO THE FOOTBALL FLASHCARD QUIZ APP")
    print("LETS BEGIN!")
    print("------------------------------------------")

    score = 0 #only increment when user gets a question right
    questions_len = len(flashcards)#gets the number of questions (i.e., K,V pairs) in our questions set, so we can use to display total num of questions once user finishes the quiz
    question_num = 1 #question number counter

    #shuffling the questions
    questions = list(flashcards.items())
    random.shuffle(questions)

    for question, answer in questions:
        print(f"Question {question_num}: {question}")
        question_num += 1
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            print()
            score += 1
        else:
            print("Incorrect!")
            print()

    #summary w/ user's final score (end of quiz)
    print("YOU HAVE COMPLETED THE QUIZ!")
    print(f"You got {score} out of {questions_len} questions.")

# start the game
play_quiz()

# ask user to play again:
def main ():
    while True:
        play_again = str(input("Would you like to play again (y/n)? ")).lower()
        if play_again == "y":
            #shuffle the flashcards again
            questions = list(flashcards.items())
            random.shuffle(questions)
            play_quiz()
        elif play_again == "n":
            print("Thank you for playing!")
            break
        else:
            print("Please enter valid input. ")
            str(input("Would you like to play again (y/n)? "))

# call the function once the quiz is finished
main()