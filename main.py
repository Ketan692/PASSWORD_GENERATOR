from tkinter import *
import random
import string
import pyperclip
import datetime

tim = Tk()
tim.minsize(width=500, height=500)
tim.title("PASSWORD GENERATOR")
tim.config(pady=50, padx=50, bg="#76BA99")


def generate_password():
    res_input.delete(0, END)

    my_alpha = list(string.ascii_lowercase)
    my_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_sym = ['~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_',
              '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    a = let_input.get()
    b = num_input.get()
    c = ch_input.get()
    final = ""
    try:
        for i in range(int(a)):
            final += random.choice(my_alpha)
    except ValueError:
        pass
    try:
        for i in range(int(b)):
            final += str(random.choice(my_num))
    except ValueError:
        pass
    try:
        for i in range(int(c)):
            final += random.choice(my_sym)
    except ValueError:
        pass

    first = list(final)
    second = random.sample(first, len(first))
    last_result = "".join(second)

    res_input.insert(0, f"{last_result}")


def save_data():
    pyperclip.copy(res_input.get())
    if len(app_input.get()) == 0:
        message = "NAME NOT MENTIONED"
    else:
        message = app_input.get()

    with open("my_pass.txt", mode='a') as data:
        data.write(f"\n\n{message} = {res_input.get()} ~~ Created on {datetime.datetime.now()}")


heading = Label(text="PASSWORD GENERATOR", font=("Courier", "40", "bold"), bg="#76BA99", fg="#100F0F")
heading.grid(row=0, column=0, columnspan=3)

app_name = Label(text="App:", font=("Courier", "12", "bold"), pady=20, fg="#100F0F", bg="#76BA99")
app_name.grid(row=1, column=0)

app_input = Entry(width=50)
app_input.grid(row=1, column=1, columnspan=2)

ch_sel = Label(text="Characters selection", font=("Courier", "15", "bold"), pady=20, fg="#100F0F", bg="#76BA99")
ch_sel.grid(row=2, column=1)

letters = Label(text="letters:", font=("Courier", "12", "bold"), fg="#100F0F", bg="#76BA99")
letters.grid(row=3, column=0)

let_input = Entry(width=50)
let_input.grid(row=3, column=1, columnspan=2)

symbols = Label(text="symbols:", font=("Courier", "12", "bold"), pady=20, fg="#100F0F", bg="#76BA99")
symbols.grid(row=4, column=0)

ch_input = Entry(width=50)
ch_input.grid(row=4, column=1, columnspan=2)

num = Label(text="Numbers:", font=("Courier", "12", "bold"), fg="#100F0F", bg="#76BA99")
num.grid(row=5, column=0)

num_input = Entry(width=50)
num_input.grid(row=5, column=1, columnspan=2)

submit = Button(text="GENERATE", width=10, command=generate_password, bg="#EAE509", font=("Courier", 12, "bold"))
submit.grid(row=6, column=1, pady=12)

result = Label(text="Generated password", font=("Courier", "12", "bold"), pady=10, fg="#100F0F", bg="#76BA99")
result.grid(row=7, column=0, columnspan=3)

res_input = Entry(width=50)
res_input.grid(row=8, column=0, columnspan=3)

copy_btn = Button(text="Save & Copy", command=save_data, bg="#EAE509", font=("Courier", 12, "bold"), width=12)
copy_btn.grid(row=9, column=0, columnspan=3, pady=15)

last_lable = Label(text="Created by - Ketan Sawant", bg="#76BA99")
last_lable.grid(row=10, column=2)


tim.mainloop()
