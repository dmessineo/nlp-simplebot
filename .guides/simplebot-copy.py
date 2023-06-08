import tkinter.scrolledtext as tks #creates a scrollable text window

from datetime import datetime
from tkinter import *


# Generating response
def get_bot_response(user_input):

  bot_response = ""
  if(user_input == "hello"):
    bot_response = "Hi!"
  elif(user_input == "hi" or user_input == "hii" or user_input == "hiiii"):
    bot_response = "Hello there! How are you?"
  elif(user_input == "how are you"):
    bot_response = "Oh, I'm great! How about you?"
  elif(user_input == "fine" or user_input == "i am good" or user_input == "i am doing good"):
    bot_response = "That's excellent! How can I help you today?"
  else:
    bot_response = "I'm sorry, I don't understand..."      
    
  return bot_response


def create_and_insert_user_frame(user_input):
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

  chatWindow.insert('end', '\n ', 'tag-right')
  chatWindow.window_create('end', window=userFrame)


def create_and_insert_bot_frame(bot_response):
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

  chatWindow.insert('end', '\n ', 'tag-left')
  chatWindow.window_create('end', window=botFrame)
  chatWindow.insert(END, "\n\n" + "")


def send(event):
    chatWindow.config(state=NORMAL)

    user_input = userEntryBox.get("1.0",'end-2c')
    user_input_lc = user_input.lower()
    bot_response = get_bot_response(user_input_lc) 

    create_and_insert_user_frame(user_input)
    create_and_insert_bot_frame(bot_response)

    chatWindow.config(state=DISABLED)
    userEntryBox.delete("1.0","end")
    chatWindow.see('end')


baseWindow = Tk()
baseWindow.title("The Simple Bot")
baseWindow.geometry("500x300")

chatWindow = tks.ScrolledText(baseWindow, font="Arial")
chatWindow.tag_configure('tag-left', justify='left')
chatWindow.tag_configure('tag-right', justify='right')
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
baseWindow.bind('<Return>', send)

userEntryBox = Text(baseWindow, bd=1, bg="white", width=38, font="Arial")

chatWindow.place(x=1, y=1, height=270, width=500)
userEntryBox.place(x=3, y=272, height=27)
sendButton.place(x=430, y=270)

baseWindow.mainloop()    