import tkinter as tk
import random

# List of words for the game
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.word_to_guess = ""
        self.display_word = ""
        self.incorrect_guesses = []
        self.attempts = 6
        
        self.choose_word()
        self.initialize_display()
        
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()
        
        self.draw_hangman(0)
        
        self.label = tk.Label(master, text="Word: " + self.display_word)
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

    def choose_word(self):
        self.word_to_guess = random.choice(words).lower()

    def initialize_display(self):
        self.display_word = "_" * len(self.word_to_guess)
        self.incorrect_guesses = []
        self.attempts = 6

    def draw_hangman(self, incorrect_attempts):
        self.canvas.delete("all")
        if incorrect_attempts >= 1:
            self.canvas.create_line(10, 190, 100, 190)
        if incorrect_attempts >= 2:
            self.canvas.create_line(55, 190, 55, 30)
        if incorrect_attempts >= 3:
            self.canvas.create_line(55, 30, 125, 30)
        if incorrect_attempts >= 4:
            self.canvas.create_line(125, 30, 125, 50)
        if incorrect_attempts >= 5:
            self.canvas.create_oval(115, 50, 135, 70)
        if incorrect_attempts >= 6:
            self.canvas.create_line(125, 70, 125, 120)
        if incorrect_attempts >= 7:
            self.canvas.create_line(125, 80, 110, 100)
        if incorrect_attempts >= 8:
            self.canvas.create_line(125, 80, 140, 100)

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if guess in self.word_to_guess:
            # Update the display_word with correct guesses
            new_display_word = ""
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    new_display_word += guess
                else:
                    new_display_word += self.display_word[i]
            self.display_word = new_display_word
        else:
            if guess not in self.incorrect_guesses:
                # Add incorrect guesses to the list and draw the hangman
                self.incorrect_guesses.append(guess)
                self.attempts -= 1
                self.draw_hangman(6 - self.attempts)
        
        self.label.config(text="Word: " + self.display_word)
        
        if self.display_word == self.word_to_guess:
            self.label.config(text="Congratulations! You've guessed the word: " + self.word_to_guess)
        elif self.attempts == 0:
            self.label.config(text="You've run out of attempts. The word was: " + self.word_to_guess)
        
        if self.attempts == 0 or self.display_word == self.word_to_guess:
            self.button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()