from tkinter import *
import tkinter
import mysql.connector
import PIL
from PIL import *
from PIL import ImageTk,Image
import os


#create database variable
#mydb = mysql.connector.connect(host = "localhost", user = "root", password = "mySQL@ccount123!")

absolute_path = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.geometry("600x400")
main_menu = Frame(root, width = 600, height = 400, bg = "skyblue3")
play_frame = Frame(main_menu)
img_1 = ImageTk.PhotoImage(Image.open(absolute_path+"/pash6.png"))

picture_label_1 = Label(play_frame, image = img_1)


def Manage_cards():
    main_menu.pack_forget()
    manage_cards.pack()
def Back():
    manage_cards.pack_forget()
    main_menu.pack()

label = Label(main_menu, text="POKEMON - 2 PLAYER GAME", font = ('Arial, 20'), fg = "Yellow")
play_button = Button(play_frame, text = "Play", fg = "blue", padx = 40, pady = 30)
manage_button = Button(main_menu, text = "Manage Cards", command=Manage_cards, fg = "red", padx = 10, pady = 30)

manage_cards = Frame(root)
manage_cards_header = Label(manage_cards, text="Manage Cards", font = ('Arial, 20'))
back_button = Button(manage_cards, text="Back", command=Back, fg = "black")

manage_cards_header.pack()
back_button.pack()
main_menu.place(relx = 0, relheight = 1, y = 0, relwidth = 1)
play_frame.place(relx = 0, relheight = 1, y = 30, relwidth = 0.5)
picture_label_1.pack()
label.pack()
play_button.place(x = 75, y = 200)
manage_button.pack()


root.mainloop()