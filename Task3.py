import tkinter as tk
from tkinter import messagebox
import random

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""

    
    if user_choice == computer_choice:
        result = "It's a tie!"
        result_color = "blue"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
        result_color = "green"
    else:
        result = "You lose!"
        computer_score += 1
        result_color = "red"

    
    label_user_choice.config(text=f"Your choice: {user_choice}", fg="darkblue")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}", fg="purple")
    label_result.config(text=result, fg=result_color)
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def play_again():
    label_user_choice.config(text="Your choice: ", fg="black")
    label_computer_choice.config(text="Computer's choice: ", fg="black")
    label_result.config(text="")
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        pass  
    else:
        root.quit()  

# GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x500")
root.config(bg="#f7e6ff")  

title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#f7e6ff", fg="#6a0dad")
title_label.pack(pady=10)


btn_rock = tk.Button(root, text="Rock", command=lambda: play_game("Rock"), font=("Helvetica", 12), bg="#ff6666", fg="white", width=15)
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", command=lambda: play_game("Paper"), font=("Helvetica", 12), bg="#66b3ff", fg="white", width=15)
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"), font=("Helvetica", 12), bg="#85e085", fg="white", width=15)
btn_scissors.pack(pady=5)

label_user_choice = tk.Label(root, text="Your choice: ", font=("Helvetica", 12), bg="#f7e6ff")
label_user_choice.pack(pady=10)

label_computer_choice = tk.Label(root, text="Computer's choice: ", font=("Helvetica", 12), bg="#f7e6ff")
label_computer_choice.pack(pady=10)

label_result = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f7e6ff")
label_result.pack(pady=10)

label_score = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#f7e6ff", fg="black")
label_score.pack(pady=10)

btn_play_again = tk.Button(root, text="Play Again", command=play_again, font=("Helvetica", 12), bg="#ffcc66", fg="black", width=15)
btn_play_again.pack(pady=20)

root.mainloop()

