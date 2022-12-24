from tkinter import *
import requests
import MED


def send(code,command):
    code=code+"@1secmail.com"
    command="Command "+command+"."
    MED.send2(code.split(),command)


def speak(code,command):
    code=code+"@1secmail.com"
    command="speak "+command+"."
    MED.send2(code.split(),command)
 
window = Tk()

window.geometry("1198x741")
window.title('')
window.iconbitmap('BLANK_ICON.ico')

window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 741,
    width = 1198,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    783.5, 485.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    695.5, 469.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 391.0, y = 450,
    width = 609.0,
    height = 36)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    279.5, 469.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fbfbfb",
    highlightthickness = 0)

entry1.place(
    x = 222.0, y = 450,
    width = 115.0,
    height = 36)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :send((entry1.get()),("shutdown/l")),
    relief = "flat")

b0.place(
    x = 842, y = 140,
    width = 62,
    height = 61)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :send((entry1.get()),("shutdown/s")),
    relief = "flat")

b1.place(
    x = 316, y = 139,
    width = 67,
    height = 61)



img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :send((entry1.get()),(entry0.get())),
    relief = "flat")

b2.place(
    x = 656, y = 571,
    width = 367,
    height = 58)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :speak((entry1.get()),(entry0.get())),
    relief = "flat")

b3.place(
    x = 196, y = 571,
    width = 410,
    height = 58)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda :send((entry1.get()),("shutdown/s")),
    relief = "flat")

b4.place(
    x = 561, y = 134,
    width = 76,
    height = 71)



window.resizable(False, False)
window.mainloop()
