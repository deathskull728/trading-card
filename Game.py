from tkinter import *
import tkinter.messagebox as mb
import mysql.connector
from PIL import Image, ImageTk
import time

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "mySQL@ccount123!")

connector = mydb
cur = mydb.cursor()

active_pokemon = "dfhgdfhdfghdgfhhdgfd"

img = ""
label = ""
myImage = ""
turn = "p1"
l_hp = ""
l_ap = ""
l_type = ""
r_hp = ""
r_ap = ""
r_type = ""
l_points = 0
r_points = 0

def display_img():
    global turn
    
    if turn == "p1":
        global active_pokemon1
        active_pokemon1 = listbox.get(ACTIVE)

        cur.execute("select image from db.Pokimon where name = %s", listbox.get(ACTIVE))
        fetch = cur.fetchall()
        path = fetch[0][0]

        global myImage, img1, label
        myImage = Image.open(path)
        myImage = myImage.resize((100, 100), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(myImage)

        label = Label(left_frame, image = img1)
        label.place(relx = 0.3, rely = 0.2)
        listbox.destroy()

        global healthl, attackl, tyl, l_hp, l_ap, l_type
        cur.execute("select health from db.Pokimon where name = %s", active_pokemon1)
        fetch = cur.fetchall()
        healthl = fetch[0][0]
        l_hp=Label(left_frame,text=f'HP:{healthl}').place(relx=0.33,rely=0.55)

        cur.execute("select attack from db.Pokimon where name = %s", active_pokemon1)
        fetch = cur.fetchall()
        attackl = fetch[0][0]
        l_ap=Label(left_frame,text=f'AP:{attackl}').place(relx=0.33,rely=0.65)

        cur.execute("select type from db.Pokimon where name = %s", active_pokemon1)
        fetch = cur.fetchall()
        tyl = fetch[0][0]
        l_type=Label(left_frame,text=f'Type:{tyl}').place(relx=0.33,rely=0.75)

    if turn == "p2":
        global active_pokemon2
        active_pokemon2 = listbox.get(ACTIVE)

        cur.execute("select image from db.Pokimon where name = %s", listbox.get(ACTIVE))
        fetch = cur.fetchall()
        path = fetch[0][0]

        global img2
        myImage = Image.open(path)
        myImage = myImage.resize((100, 100), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(myImage)

        label = Label(right_frame, image = img2)
        label.place(relx = 0.3, rely = 0.2)
        listbox.destroy()

        global healthr, attackr, tyr, r_hp, r_ap, r_type
        cur.execute("select health from db.Pokimon where name = %s", active_pokemon2)
        fetch = cur.fetchall()
        healthr = fetch[0][0]
        r_hp=Label(right_frame,text=f'HP:{healthr}').place(relx=0.33,rely=0.55)

        cur.execute("select attack from db.Pokimon where name = %s", active_pokemon2)
        fetch = cur.fetchall()
        attackr = fetch[0][0]
        r_ap=Label(right_frame,text=f'AP:{attackr}').place(relx=0.33,rely=0.65)

        cur.execute("select type from db.Pokimon where name = %s", active_pokemon2)
        fetch = cur.fetchall()
        tyr = fetch[0][0]
        r_type=Label(right_frame,text=f'Type:{tyr}').place(relx=0.33,rely=0.75)

def change_turn():
    global turn
    for i in ['p1','p2']:
        if not(i==turn):
            turn=i
            break

def list_contacts():
    global cur
    cur.execute("select name from db.Pokimon")
    fetch = cur.fetchall()
    for data in fetch:
        listbox.insert(END, data)

def Attack():
    global turn, healthl, healthr, attackl, attackr, tyl, tyr, l_hp, l_ap, l_type, r_hp, r_ap, r_type, active_pokemon1, active_pokemon_2, l_points, r_points

    if turn == "p1":
        healthr -= attackl
        if healthr <= 0:
            healthr = 0

    if turn == "p2":
        healthl -= attackr
        if healthl <= 0:
            healthl = 0

    l_hp=Label(left_frame,text=f'HP:{healthl}').place(relx=0.33,rely=0.55)
    l_ap=Label(left_frame,text=f'AP:{attackl}').place(relx=0.33,rely=0.65)
    l_type=Label(left_frame,text=f'Type:{tyl}').place(relx=0.33,rely=0.75)

    r_hp=Label(right_frame,text=f'HP:{healthr}').place(relx=0.33,rely=0.55)
    r_ap=Label(right_frame,text=f'AP:{attackr}').place(relx=0.33,rely=0.65)
    r_type=Label(right_frame,text=f'Type:{tyr}').place(relx=0.33,rely=0.75)

    if healthl == 0:
        r_points += 1
        if r_points == 10:
            pointsr_lbl=Label(root,text="PLAYER 2 WINS!!!",fg='white', bg = "darkred",padx = 100, pady = 50).place(x =200, y = 250)
        else:
            pointsr_lbl=Label(right_frame,text=f'Points: {r_points}',fg='blue', bg = "skyblue3",width=5).place(relx=0.07,rely=0.05)

    if healthr == 0:
        l_points += 1
        if l_points == 10:
            pointsl_lbl=Label(root,text="PLAYER 1 WINS!!!",fg='white', bg = "darkred",padx = 100, pady = 50).place(x =200, y = 250)
        else:
            pointsl_lbl=Label(left_frame,text=f'Points: {l_points}',fg='blue', bg = "skyblue3",width=5).place(relx=0.07,rely=0.05)

def create_listbox():
    global listbox, turn
    if turn == "p1":
        listbox = Listbox(left_frame, selectbackground = "SkyBlue", bg = 'Gainsboro', font = ('Helvetica', 12), fg ="black", height = 20, width = 25)
    if turn == "p2":
        listbox = Listbox(right_frame, selectbackground = "SkyBlue", bg = 'Gainsboro', font = ('Helvetica', 12), fg = "black", height = 20, width = 25)
    listbox.place(relx = 0.1, rely = 0.15)
    list_contacts()

def heal():
    global healthl, healthr, turn
    if turn == "p1":
        healthl += 20
        l_hp=Label(left_frame,text=f'HP:{healthl}').place(relx=0.33,rely=0.55)
    if turn == "p2":
        healthr += 20
        r_hp=Label(right_frame,text=f'HP:{healthr}').place(relx=0.33,rely=0.55)

def attack_spcl():
    global turn, healthl, healthr, attackl, attackr, tyl, tyr, l_hp, l_ap, l_type, r_hp, r_ap, r_type, active_pokemon1, active_pokemon_2, l_points, r_points

    if turn == "p1":
        healthr -= 200
        if healthr <= 0:
            healthr = 0

    if turn == "p2":
        healthl -= 200
        if healthl <= 0:
            healthl = 0

    if healthl == 0:
        r_points += 1
        if r_points == 10:
            pointsr_lbl=Label(root,text="PLAYER 2 WINS!!!",fg='white', bg = "darkred",padx = 100, pady = 50).place(x =200, y = 250)
        else:
            pointsr_lbl=Label(right_frame,text=f'Points: {r_points}',fg='blue', bg = "skyblue3",width=5).place(relx=0.07,rely=0.05)

    if healthr == 0:
        l_points += 1
        if l_points == 10:
            pointsl_lbl=Label(root,text="PLAYER 1 WINS!!!",fg='white', bg = "darkred",padx = 100, pady = 50).place(x =200, y = 250)
        else:
            pointsl_lbl=Label(left_frame,text=f'Points: {l_points}',fg='blue', bg = "skyblue3",width=5).place(relx=0.07,rely=0.05)

    l_hp=Label(left_frame,text=f'HP:{healthl}').place(relx=0.33,rely=0.55)
    l_ap=Label(left_frame,text=f'AP:{attackl}').place(relx=0.33,rely=0.65)
    l_type=Label(left_frame,text=f'Type:{tyl}').place(relx=0.33,rely=0.75)

    r_hp=Label(right_frame,text=f'HP:{healthr}').place(relx=0.33,rely=0.55)
    r_ap=Label(right_frame,text=f'AP:{attackr}').place(relx=0.33,rely=0.65)
    r_type=Label(right_frame,text=f'Type:{tyr}').place(relx=0.33,rely=0.75)

root = Tk()
root.title("Game Window")
root.geometry("700x500")
root.resizable(0, 0)

gray = "dark orange"
gray57 = "orange"
gray35 = "dark orange"

frame_font = ("Garamond", 14)

title_label = Label(root, text = "Game Window", font = ("Arial", 18), bg = "black", fg = "white")
left_frame = Frame(root, bg = gray)
center_frame = Frame(root, bg = gray57)
right_frame = Frame(root, bg = gray35)
player1 = Label(left_frame, text = "Player 1", font = ("Arial", 18), bg = "black", fg = "white").place(relx = 0.3, rely = 0.05)
player2 = Label(right_frame, text = "Player 2", font = ("Arial", 18), bg = "black", fg = "white").place(relx = 0.3, rely = 0.05)

title_label.pack(side = TOP, fill = X)
left_frame.place(relx = 0, relheight = 1, y = 30, relwidth = 0.35)
center_frame.place(relx = 0.33, relheight = 1, y = 30, relwidth = 0.4)
right_frame.place(relx = 0.66, relheight = 1, y = 30, relwidth = 0.35)

attack_lbl=Label(center_frame,text='Action',fg='blue', bg = "skyblue3",width=15).place(relx=0.13,rely=0.05)
pokemon_btn=Button(center_frame,text='Pokemon',fg='green',width=15, command = create_listbox).place(relx=0.13,rely=0.25)
select_btn = Button(center_frame, text = "Select Pokemon", fg = 'green', width = 15, command = display_img).place(relx = 0.13, rely = 0.30)
change_turn = Button(center_frame, text = "Change Turn", fg = "purple", width = 10, command = change_turn).place(relx = 0.2, rely = 0.15)

pointsl_lbl=Label(left_frame,text=f'Points: {l_points}',fg='blue', bg = "skyblue3",width=5).place(relx=0.07,rely=0.05)
pointsr_lbl=Label(right_frame,text=f'Points: {l_points}',fg='blue', bg = "skyblue3",width=5).place(relx=0.07,rely=0.05)

attack_btn=Button(center_frame,text='Attack',fg='red',width=15, command = Attack).place(relx=0.13,rely=0.45)
sattack_btn=Button(center_frame,text='Special Attack ',fg='darkred',width=15, command = attack_spcl).place(relx=0.13,rely=0.65)
heal_button=Button(center_frame,text='Heal',fg='skyblue3',width=15, command = heal).place(relx=0.13,rely=0.85)


create_listbox()

root.mainloop()
