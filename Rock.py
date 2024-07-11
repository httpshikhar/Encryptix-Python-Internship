import tkinter as tk
import random

user_score = 0
computer_score = 0

def on_button_click(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    
    if "Win" in result:
        user_score += 1
    elif "Lose" in result:
        computer_score += 1
    
    result_label.config(text = f"Computer chose : {computer_choice}\nResult: {result}")
    score_label.config(text = f"User score : {user_score} | Computer Score : {computer_score}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
    (user_choice == "Paper" and computer_choice == "Rock") or \
    (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win"
    else:
        return "You Lose"

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text = f"User score : {user_score} | Computer Score : {computer_score}")

root = tk.Tk()

score_label = tk.Label(root, text = f"User score : {user_score} | Computer Score : {computer_score}")
score_label.pack(pady=10)

result_label = tk.Label(root, text = "")
result_label.pack(pady=10)



root.title("Game")
root.geometry("300x300")


rock_button = tk.Button(root, text = "Rock", command = lambda: on_button_click("Rock"))
paper_button = tk.Button(root, text = "Paper", command = lambda: on_button_click("Paper"))
scissors_button = tk.Button(root, text = "Scissors", command = lambda: on_button_click("Scissors"))

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

reset_button = tk.Button(root, text = "Play Again", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()