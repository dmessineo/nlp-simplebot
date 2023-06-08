import nltk
import tkinter.scrolledtext as tks

from datetime import datetime
from tkinter import *
from nltk.chat.util import Chat, reflections

def send(event):
    chatWindow.tag_configure('tag-left', justify='left')
    chatWindow.tag_configure('tag-right', justify='right')
    chatWindow.config(state=NORMAL)

    pairs =[
      ['my name is (.*)', ['Hello ! % 1']],
      ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
      ['(.*) your name ?', ['My name is Geeky']],
      ['(.*) do you do ?', ['We provide a platform for tech enthusiasts, a wide range of options !']],
      ['(.*) created you ?', ['Geeksforgeeks created me using python and NLTK']]
    ]

    chat = Chat(pairs, reflections)

    user_input = userEntryBox.get("1.0",'end-2c')
    bot_response = ""
    while user_input[-1] in "!.":
      user_input = user_input[:-1]
    bot_response = chat.respond(user_input) 

    userFrame = Frame(chatWindow, bg="#d0ffff")
    Label(
        userFrame,
        text=user_input,
        font=("Arial", 11),
        bg="#d0ffff").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    Label(
        userFrame,
        text=datetime.now().strftime("%H:%M"),
        font=("Arial", 7),
        bg="#d0ffff"
    ).grid(row=1, column=0, sticky="w")

    botFrame = Frame(chatWindow, bg="#ffffd0")
    Label(
        botFrame,
        text=bot_response,
        font=("Arial", 11),
        bg="#ffffd0",
        wraplength=400,
        justify='left'
    ).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    Label(
        botFrame,
        text=datetime.now().strftime("%H:%M"),
        font=("Arial", 7),
        bg="#ffffd0"
    ).grid(row=1, column=0, sticky="w")

    chatWindow.insert('end', '\n ', 'tag-right')
    chatWindow.window_create('end', window=userFrame)

    chatWindow.insert('end', '\n ', 'tag-left')
    chatWindow.window_create('end', window=botFrame)
    chatWindow.insert(END, "\n\n" + "")

    chatWindow.config(state=DISABLED)
    userEntryBox.delete("1.0","end")
    chatWindow.see('end')

baseWindow = Tk()
baseWindow.title("SimpleBot")
baseWindow.geometry("500x300")
baseWindow.bind('<Return>', send)

chatWindow = tks.ScrolledText(baseWindow, font="Arial")
chatWindow.config(state=DISABLED)

sendButton = Button(
    baseWindow,
    font=("Verdana", 12, 'bold'),
    text="Send",
    bg="#fd94b4",
    activebackground="#ff467e",
    fg='#ffffff',
    command=send)
sendButton.bind("<Button-1>", send)

userEntryBox = Text(baseWindow, bd=1, bg="white", width=38, font="Arial")

chatWindow.place(x=1, y=1, height=270, width=500)
userEntryBox.place(x=3, y=272, height=27)
sendButton.place(x=430, y=270)

baseWindow.mainloop()