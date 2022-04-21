from tkinter import *
import mysql.connector
from PIL import ImageTk, Image

#create database variable
#mydb = mysql.connector.connect(host = "localhost", user = "root", password = "mySQL@ccount123!")

root = Tk()
root.geometry("600x400")
main_menu = Frame(root, width = 600, height = 400)
main_menu.config(width = 600)

def Manage_cards():
    main_menu.pack_forget()
    manage_cards.pack()
def Back():
    manage_cards.pack_forget()
    main_menu.pack()

label = Label(main_menu, text="POKEMON - 2 PLAYER GAME", font = ('Arial, 20'), fg = "Yellow")
play_button = Button(main_menu, text = "Play", fg = "blue", padx = 40, pady = 30)
manage_button = Button(main_menu, text = "Manage Cards", command=Manage_cards, fg = "red", padx = 10, pady = 30)

label.pack()
play_button.pack()
manage_button.pack()

manage_cards = Frame(root)
manage_cards_header = Label(manage_cards, text="Manage Cards", font = ('Arial, 20'))
back_button = Button(manage_cards, text="Back", command=Back, fg = "black")

manage_cards_header.pack()
back_button.pack()
main_menu.pack()


root.mainloop()