FONT_NAME = "Arial"

from tkinter import *

def FileHandle():
    with open("text.txt", "a") as file:
        file.write(f"Name: {name_input.get()} | Email: {email_input.get()} | Password: {password_input.get()}\n")

def setRandomPassword():
    password_input.delete(0,END)
    password_input.insert(0,"Amlendu786")

window = Tk()

window.minsize(width=500, height=400)
window.title("Password Manager Generator")
window.configure(bg="#F7F9F2")
canvas = Canvas(window, height=150, width=180)
text = canvas.create_text(100, 100, text="🔒", font=(FONT_NAME, 50, "bold"))
canvas.pack()

name_label = Label(window, text="Name:", font=(FONT_NAME, 20, "bold"))
name_label.place(x=10, y=170)

name_input = Entry(window, width=20, font=(FONT_NAME, 12))
name_input.place(x=160, y=180)

email_label = Label(window, text="Email:", font=(FONT_NAME, 20, "bold"))
email_label.place(x=10, y=210)

email_input = Entry(window, width=20, font=(FONT_NAME, 12))
email_input.place(x=160, y=220)

password_label = Label(window, text="Password:", font=(FONT_NAME, 20, "bold"))
password_label.place(x=10, y=250)

password_input = Entry(window, width=20, font=(FONT_NAME, 12))
password_input.place(x=160, y=250)

password_generator = Button(window, text="password generator", command=setRandomPassword, padx=10, pady=3,bg="white",fg="black",font=(FONT_NAME, 8))
password_generator.place(x=350, y=250)

add_button = Button(window, text="Add", command=FileHandle, padx=10, pady=3)
add_button.place(x=250, y=300)

window.mainloop()
