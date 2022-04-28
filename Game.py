from tkinter import *
import tkinter.messagebox as mb
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "fortnitedire")

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

attack_lbl=Label(center_frame,text='Action',fg='blue',width=15).place(relx=0.13,rely=0.05)
pokemon_btn=Button(center_frame,text='Pokemon',fg='green',width=15).place(relx=0.13,rely=0.25)


attack_btn=Button(center_frame,text='Attack',fg='red',width=15).place(relx=0.13,rely=0.45)
attack_btn=Button(center_frame,text='Special Attack ',fg='darkred',width=15).place(relx=0.13,rely=0.65)
attack_btn=Button(center_frame,text='Heal',fg='yellow',width=15).place(relx=0.13,rely=0.85)

l_hp=Label(left_frame,text=f'HP:*').place(relx=0.33,rely=0.55)
l_ap=Label(left_frame,text=f'AP:*').place(relx=0.33,rely=0.65)
l_type=Label(left_frame,text=f'Type:*').place(relx=0.33,rely=0.75)

r_hp=Label(right_frame,text=f'HP:*').place(relx=0.33,rely=0.55)
r_ap=Label(right_frame,text=f'AP:*').place(relx=0.33,rely=0.65)
r_type=Label(right_frame,text=f'Type:*').place(relx=0.33,rely=0.75)



root.mainloop()
