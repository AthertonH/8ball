import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

import responses

root = tk.Tk(className="Magic 8 Ball")

canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open("image.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Please type in your question. Then 'Shake' to see your fate.")
instructions.grid(columnspan=3, column=0, rowspan=5, row=1)


# won't print command on GUI*************
def shake():
	text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
	text_box.insert(0, responses.EightBall())
	text_box.tag_configure("center", justify="center")
	text_box.tag_add("center", 0, "end")
	text_box.grid(column=1, row=3)

# shake button
shake_text = tk.StringVar()
shake_button = tk.Button(root, textvariable=shake_text, command=lambda: shake())

shake_text.set("Shake")
shake_button.grid(column=1, row=2)

root.mainloop()