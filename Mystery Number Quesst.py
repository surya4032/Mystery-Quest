import tkinter as tk
from tkinter import messagebox
import random

class MysteryQuest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mystery Quest")
        self.geometry("800x600")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 7
        self.state('zoomed')
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill='both')
        self.sub_frame = tk.Frame(self.main_frame)
        self.sub_frame.pack(expand=True, anchor="center")
        self.label = tk.Label(self.sub_frame, text="Guess a number between 1 and 100:",width=40,font=("Arial",15))
        self.label.pack(pady=(20,5) )
        self.entry = tk.Entry(self.sub_frame)
        self.entry.pack( pady=(20,5))
        self.button = tk.Button(self.sub_frame, text="Guess", command=self.check_guess,bg="blue",fg="white",width=10)
        self.button.pack(pady=(20,5))
        self.info_label = tk.Label(self.sub_frame, text=f"You have {self.max_attempts} attempts remaining.")
        
        self.info_label.pack(pady=(20,5))
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            remaining_attempts = self.max_attempts - self.attempts

            if guess < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.secret_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number} in {self.attempts} attempts!")
                self.reset_game()
                return

            if remaining_attempts > 0:
                self.info_label.config(text=f"You have {remaining_attempts} attempts remaining.")
            else:
                messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The number was {self.secret_number}.")
                self.reset_game()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            

    def reset_game(self):
        self.attempts = 0
        self.secret_number = random.randint(1, 100)
        
        self.info_label.config(text=f"You have {self.max_attempts} attempts remaining.")
        
        self.entry.delete(0, tk.END)
 
if __name__ == "__main__":
    app = MysteryQuest()
    app.mainloop()
