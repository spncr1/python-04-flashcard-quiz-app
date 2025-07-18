# using the questions for GUI integration
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.ttk import Style
from flashcards import flashcards

# Function to display the current question and choices
def show_question():
    # Get the current question from the flashcards list
    question = flashcards[current_question]
    question_label.config(text=question["Question"])

    #  Display the choices on the buttons
    options = question["Options"]
    for i in range(4):
        choice_buttons[i].config(text=options[i], state="normal") # Reset button state

    # Clear the feedback label and disable the 'next' button
    feedback_label.config(text="")
    next_button.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(answer):
    # Get the current question from the flashcards list
    question = flashcards[current_question]
    selected_choice = choice_buttons[answer].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["Answer"]:
        # Update the socre and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(flashcards)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")

    # Disable all choice buttons and enable the next button
    for button in choice_buttons:
        button.config(state="disabled")
    next_button.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    if current_question == len(flashcards) - 1:
        # If all questions have been answered, display the final score
        messagebox.showinfo(
                        "No more questions!",
                            "Quiz Completed! Final score: {}/{}".format(score, len(flashcards))
                            )
        window.destroy()
    else:
        # If there are more questions, show the next question
        current_question += 1
        show_question()

# Create the main window
window = tk.Tk()
window.title("Football Flashcard Quiz App")
window.geometry("800x640")
style = Style()
#window.config(background = "black")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))


# Create the question label
question_label = ttk.Label(
    window,
    anchor="center",
    text="Question",
    wraplength=500,
    padding=10
)
question_label.pack(pady=10)

# Create the choice buttons
choice_buttons = [] #list to store all the buttons (i.e., 4 choices where user can click on 4 buttons for an answer)
for i in range(4):
    button = ttk.Button(
        window,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_buttons.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    window,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialise score (counter)
score = 0

# Create the score label
score_label = ttk.Label(
    window,
    text="Score: 0/{}".format(len(flashcards)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_button = ttk.Button(
    window,
    text="Next",
    command=next_question,
    state="disabled"
)
next_button.pack(pady=10)

# Initialise current question index
current_question = 0

# Show the first question
show_question()

window.mainloop()