import requests
# py -m pip install pip
# python -m pip install pip
# python3 -m pip install pip
# pip install requests
# pip3 install requests

import tkinter as tk
from tkinter import END, Text
from tkinter import Button

#API = https://api.quotable.io/random

root = tk.Tk()
root.title('Quotes')

def get_quote():
    r = requests.get('https://api.quotable.io/random')
    data = r.json()
    quote = data['content']

    text_box.delete('1.0', END)
    text_box.insert(END, quote)

text_box = Text(root, height=10, width=50)
get_button = Button(root, text='Get Quote', command=get_quote)

text_box.pack()
get_button.pack()
root.mainloop()