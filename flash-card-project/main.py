import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn = {}
try:
    data = pandas.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
    original_file = pandas.read_csv('data/french_words.csv')
    to_learn = original_file.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French",fill='white')
    canvas.itemconfig(word, text=current_card["French"], fill='white')
    canvas.itemconfig(canvas_card, image=back)
    flip_timer = window.after(3000,func=flip_canvas)


def flip_canvas():
    canvas.itemconfig(language,text="English",fill='black')
    canvas.itemconfig(word, text=current_card["English"], fill='black')
    canvas.itemconfig(canvas_card,image=front)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/to_learn.csv',index=False)
    next_card()

#--------------------------------SETTING UP UI-----------------------------------

LANGUAGE_FONT = ('Arial',40,'italic')
WORD_FONT = ('Arial',60,'bold')

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,func=flip_canvas)

#Canvas creation
canvas = Canvas()
back = PhotoImage(file='images/card_back.png')
front = PhotoImage(file='images/card_front.png')

canvas_card = canvas.create_image(400,263,image=back)
canvas.config(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
language = canvas.create_text(400,150,text='',font=LANGUAGE_FONT)
word = canvas.create_text(400,263,text='',font=WORD_FONT)

#Buttons
tick = PhotoImage(file='images/right.png')
correct = Button(image=tick,highlightthickness=0,borderwidth=0,command=is_known)
correct.grid(row=1,column=1)

cross = PhotoImage(file='images/wrong.png')
wrong = Button(image=cross,highlightthickness=0,borderwidth=0,command=next_card)
wrong.grid(row=1,column=0)

next_card()

window.mainloop()
