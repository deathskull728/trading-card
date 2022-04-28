from tkinter import *
import tkinter.messagebox as mb
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "mySQL@ccount123!")

connector = mydb
cur = mydb.cursor()

root = Tk()
root.title("Game Window")
root.geometry("700x500")
root.resizable(0, 0)

gray = "gray70"
gray57 = "gray57"
gray35 = "gray35"

frame_font = ("Garamond", 14)

title_label = Label(root, text = "Game Window", font = ("Arial", 18), bg = "black", fg = "white")
left_frame = Frame(root, bg = gray)
center_frame = Frame(root, bg = gray57)
right_frame = Frame(root, bg = gray35)

title_label.pack(side = TOP, fill = X)
left_frame.place(relx = 0, relheight = 1, y = 30, relwidth = 0.35)
center_frame.place(relx = 0.33, relheight = 1, y = 30, relwidth = 0.4)
right_frame.place(relx = 0.66, relheight = 1, y = 30, relwidth = 0.35)



root.mainloop()
