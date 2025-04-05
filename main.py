from tkinter import *
from random import choice
import time

# Initialize the window
window = Tk()
window.title("Speed Typing Test")
window.geometry("500x500")
window.configure(bg="skyblue")

# Sample sentences
sentences = [
    "The quick red fox jumps over the lazy dog.",
    "Pack my box with seven dozen liquor jugs.",
    "Six big devils from Greece quickly forgot how to fox-trot."
]


# Reset function
def reset():
    text1.delete("1.0", END)
    global sample, start
    sample = choice(sentences)
    text1.insert(END, sample)
    text2.delete("1.0", END)
    text3.delete("1.0", END)
    start = time.time()


# Calculate function
def calculate():
    text3.delete("1.0", END)
    end = time.time()
    time_taken = end - start
    typed_text = text2.get("1.0", END).strip()

    correct_count = sum(1 for i in range(min(len(sample), len(typed_text))) if sample[i] == typed_text[i])
    total_chars = len(typed_text)

    time_in_min = time_taken / 60
    GWPM = (total_chars / 5) / time_in_min
    NWPM = (correct_count / 5) / time_in_min
    accuracy = (NWPM * 100) / GWPM

    result = f"Total characters: {total_chars}\nCorrect characters: {correct_count}\nIncorrect characters: {total_chars - correct_count}\nTime taken: {round(time_taken, 2)} sec\nAccuracy: {round(accuracy, 2)}%\nTyping speed: {round(NWPM, 2)} WPM"

    text3.insert("1.0", result)


# GUI Elements
Label(window, text="Here is your Sentence:", bg="skyblue", font=("Times", 12, "bold italic")).pack(pady=5)
text1 = Text(window, height=4, width=42)
text1.pack()

Label(window, text="Type the above Sentence:", bg="skyblue", font=("Times", 12, "bold italic")).pack(pady=5)
text2 = Text(window, height=4, width=42)
text2.pack()

Button(window, text="Check Result", bg="lightgreen", font=("Times", 10, "bold italic"), relief="raised",
       command=calculate).pack(pady=10)
Label(window, text="Results:", bg="skyblue", font=("Times", 12, "bold italic")).pack()
text3 = Text(window, height=6, width=42)
text3.pack()

Button(window, text="RESET", width=10, bg="orange", font=("Times", 10, "bold italic"), relief="raised",
       command=reset).pack(pady=10)

# Initialize the game
reset()
window.mainloop()