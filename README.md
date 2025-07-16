# Flashcard Quiz App

A simple command-line Football Flashcard Quiz game built in Python!  
Test your football knowledge with randomized questions and keep track of your score.

---

## Features

- **Multiple choice questions** about football.
- **Randomized question order** for each playthrough.
- **Score tracking**: See how many you got right.
- **Play again** option for endless fun.
- **Immediate feedback** after each answer.

---

## How to Run

1. **Save** the code to a file named `flashcard_quiz.py`.
2. **Run** the file with:
   ```sh
   python flashcard_quiz.py
   ```

---

## How to Play

- The app will present you with a series of football flashcard questions, one at a time.
- Enter your answer and press **Enter**.
- The app will tell you if you are **Correct!** or **Incorrect!** after each question.
- At the end, you'll see your **final score**.
- You will be asked if you want to play again (`y` or `n`).

---

## Example

```
------------------------------------------
WELCOME TO THE FOOTBALL FLASHCARD QUIZ APP
LETS BEGIN!
------------------------------------------
Question 1: Who won the Golden Boy award in 2021?
Your answer: Pedri
Correct!

Question 2: How many times have PSG won the UCL (enter as one word)
Your answer: Once
Correct!

...

YOU HAVE COMPLETED THE QUIZ!
You got 4 out of 5 questions.
Would you like to play again (y/n)? n
Thank you for playing!
```

---

## Code Highlights

- **Flashcards** are stored as a Python dictionary (`flashcards`), mapping questions to answers.
- **Randomization** uses `random.shuffle()` to ensure questions appear in a new order each playthrough.
- **Case-insensitive** answer checking (`user_answer.lower() == answer.lower()`).
- **Replay loop** allows the user to play as many times as they want.

---

## Customization

- **Add your questions:**  
  Add or edit questions and answers in the `flashcards` dictionary at the top of the file.

- **Expand the app:**  
  You can add features like hints, scoreboards, or categories for more advanced use.

---

## License

This project is open source and free to use.

---