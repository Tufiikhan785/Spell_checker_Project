from textblob import TextBlob
from tkinter import *


def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, END)
    enter2.insert(0, data)


def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x400")
    win.resizable(False, False)
    win.config(bg="Blue")
    win.title("Spell Checker")
    Label1 = Label(win, text="Incorrect Spelling", font=(
        "Times New Roman", 25, "bold"), bg="blue", fg="white")
    Label1.place(x=100, y=20, height=50, width=300)
    enter1 = Entry(win, font=("Time New Roman", 20))
    enter1.place(x=50, y=80, height=50, width=400)
    Label2 = Label(win, text="Correct Spelling", font=(
        "Times New Roman", 25, "bold"), bg="blue", fg="white")
    Label2.place(x=100, y=140, height=50, width=300)
    enter2 = Entry(win, font=("Time New Roman", 20))
    enter2.place(x=50, y=200, height=50, width=400)

    button = Button(win, text="Done", font=("Time New Roman", 25, "bold"), bg="Green", command=correct_spelling)
    button.place(x=150, y=280, height=50, width=200)
    win.mainloop()

main_window()


# obj=TextBlob("dataa")
# print(obj.correct())
# Spell checker project
# import tkinter as tk
# from tkinter import scrolledtext
# import enchant

# class SpellCheckerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Spell Checker")

#         self.text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD)
#         self.text_widget.pack(fill=tk.BOTH, expand=True)

#         self.check_button = tk.Button(root, text="Check Spelling", command=self.check_spelling)
#         self.check_button.pack()

#         self.result_label = tk.Label(root, text="")
#         self.result_label.pack()

#         self.spell_checker = enchant.Dict("en_US")

#     def check_spelling(self):
#         text = self.text_widget.get("1.0", tk.END)
#         words = text.split()
#         incorrect_words = []

#         for word in words:
#             if not self.spell_checker.check(word):
#                 incorrect_words.append(word)

#         if incorrect_words:
#             self.result_label.config(text=f"Incorrect words: {', '.join(incorrect_words)}")
#         else:
#             self.result_label.config(text="All words are correct!")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SpellCheckerApp(root)
#     root.mainloop()
