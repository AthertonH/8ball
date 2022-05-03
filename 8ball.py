import tkinter as tk
from PIL import Image, ImageTk
from random import choice

def eightball(box):
	box.delete('1.0', tk.END)
	responses = ["It is certain.",
	             "It is decidedly so.",
	             "Without a doubt",
	             "Yes - definitely",
	             "You may rely on it.",
	             "As I see it, yes.",
	             "Most likely.",
	             "Outlook good.",
	             "Yes.",
	             "Signs point to yes.",
	             "Reply hazy, try again.",
	             "Ask again later.",
	             "Better not tell you now.",
	             "Cannot predict now.",
	             "Concentrate and ask again.",
	             "Don't count on it.",
	             "My reply is no.",
	             "My sources say no.",
	             "Outlook not so good.",
	             "Very doubtful."]
	box.insert(tk.END, choice(responses))

root = tk.Tk()
root.title("Magic 8 Ball")
root['padx'] = 0
root['pady'] = 0

canvas=tk.Canvas(root, width=1280, height=720, bg="black")
canvas.grid(columnspan=11, rowspan=11)


logo = Image.open("image.bmp")
logo = ImageTk.PhotoImage(logo)
canvas.create_image(640,300,image=logo)


label = tk.Label(root, text='Type a question then, shake', bg="black", fg="purple")
label.grid(columnspan=1, rowspan=1)
label.grid(column=5, row=9, sticky='new')

string = tk.StringVar()
box = tk.Text(root, width=3, height=1)
box.grid(columnspan=1, rowspan=1)
box.grid(column=5, row=8, sticky='new')


btn = tk.Button(root, text='SHAKE', bg="black", fg="purple")
btn['command'] = lambda: eightball(box)
btn.grid(column=5, row=10, sticky='new')
root.mainloop()