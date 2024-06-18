FONT_NAME = "Arial"
bgcolor="#F7F9F2"
from tkinter import *
import json
from tkinter import messagebox
import random
def PasswordGenerator():
    nr_letters=random.randint(8,10)
    nr_numbers=random.randint(2,4)
    nr_symbols=random.randint(2,4)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list=[]
    for i in range(0,nr_letters):
        password_list.append(random.choice(letters))
    for i in range(0,nr_numbers):
        password_list.append(random.choice(numbers))
    for i in range(0,nr_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)
    password=""
    for s in password_list:
        password+=s
    return password

def FileHandle():
    name=name_input.get()
    email=email_input.get()
    password=password_input.get()
    data={
        name:{
            "email":email,
            "password":password
        }
    }
    try:
        with open("text.json", "r") as file:
            d=json.load(file)
            d.update(data)
    except FileNotFoundError:
        d=data
    finally:
        with open("text.json","w") as file:
            json.dump(d,file,indent=4)
        messagebox.askquestion("Message","Successfully Generated!!")


def setRandomPassword():
    password_input.delete(0,END)
    password_=PasswordGenerator()
    password_input.insert(0,password_)

def find_password():
    name=name_input.get()
    try:
        with open("text.json","r") as file:
            d=json.load(file)
            output=d[name]
            messagebox.askquestion(f"{name}",f"Email : {output['email']}\nPassword:{output['password']}")


    except FileNotFoundError:
        messagebox.askquestion("Message","FileNotFound")
    except KeyError:
        messagebox.askquestion("Message","No details for website")


window = Tk()

window.minsize(width=550, height=450)
window.title("Password Generator Mangager")
window.configure(bg="#F7F9F2",padx=50,pady=50)

canvas = Canvas(window, height=150, width=180,bg=bgcolor,highlightthickness=0)
text = canvas.create_text(100, 100, text="🔒", font=(FONT_NAME, 70, "bold"),fill="#A73121")
canvas.pack()

name_label = Label(window, text="Name:", font=(FONT_NAME, 20, "bold"))
name_label.config(bg=bgcolor)
name_label.place(x=10, y=180)

name_input = Entry(window, width=20, font=(FONT_NAME, 12))
name_input.place(x=160, y=180)

search_button = Button(window, text="Search", command=find_password, padx=10, pady=3,font=("times new roman", 10,"bold"),relief="groove",width=5)
search_button.place(x=350, y=180)

email_label = Label(window, text="Email:", font=(FONT_NAME, 20, "bold"))
email_label.config(bg=bgcolor)
email_label.place(x=10, y=220)

email_input = Entry(window, width=20, font=(FONT_NAME, 12))
email_input.place(x=160, y=220)

password_label = Label(window, text="Password:", font=(FONT_NAME, 20, "bold"))
password_label.place(x=10, y=250)
password_label.config(bg=bgcolor)
password_input = Entry(window, width=20, font=(FONT_NAME, 12))
password_input.place(x=160, y=250)

password_generator = Button(window, text="Password Generator", command=setRandomPassword, padx=10, pady=3,bg="white",fg="black",font=("times new roman", 8,"bold"))
password_generator.place(x=350, y=250)

add_button = Button(window, text="Add", command=FileHandle, padx=10, pady=3,font=("times new roman", 10,"bold"),relief="groove",width=30)
add_button.place(x=150, y=300)

window.mainloop()
