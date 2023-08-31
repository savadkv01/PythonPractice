import wikipedia
from tkinter import *

def on_press():
    q = get_q.get()
    try:
        result = wikipedia.summary(q)
        txt.delete("1.0", END)  # Clear previous result
        txt.insert(INSERT, result)
    except wikipedia.exceptions.PageError:
        txt.delete("1.0", END)
        txt.insert(INSERT, "Search result not found. Please try another keyword.")

root = Tk()
root.title("WIKI Search App")

# Configure colors
bg_color = "#E0E0E0"
accent_color = "#336699"
root.configure(bg=bg_color)

qst = Label(root, text='Enter your question:', bg=bg_color)
qst.pack(pady=(10, 0))

get_q = Entry(root, bd=5)
get_q.pack()

submit = Button(root, text='Search Wikipedia', command=on_press, bg=accent_color, fg="white")
submit.pack(pady=10)

txt = Text(root, wrap=WORD, bg=bg_color)
txt.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Scrollbar for the text widget
scrollbar = Scrollbar(txt)
scrollbar.pack(side=RIGHT, fill=Y)
txt.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)

root.mainloop()