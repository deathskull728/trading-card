from tkinter import *
import tkinter.messagebox as mb
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "mySQL@ccount123!")

connector = mydb
cur = mydb.cursor()

def search():
    pass

def submit_record():
    global name_strvar, phone_strvar, email_strvar, address_entry, cur
    name, email, phone, address = name_strvar.get(), email_strvar.get(), phone_strvar.get(), address_strvar.get()
    if name == '' or address == '' or phone == "" or email == "":
        mb.showerror("Error", "Please fill out all the fields")
    else:
        cur.execute("insert into db.Pokemon_Data(name, attack, health, type) values (%s, %s, %s, %s)", (name, email, phone, address))
        connector.commit()
        mb.showinfo("Success!", "Field was added succesfully")
        listbox.delete(0, END)
        list_contacts()
        clear_fields()

def view_record():
    pass

def clear_fields():
    global name_strvar, phone_strvar, email_strvar, address_strvar, listbox
    listbox.selection_clear(0, END)
    name_strvar.set("")
    phone_strvar.set("")
    email_strvar.set("")
    address_strvar.set("")

def delete_record():
    global listbox, connector, cur
    if not listbox.get(ACTIVE):
        mb.showerror("Error", "Contact not selected")
    else:
        cur.execute("delete from db.Pokemon_Data where name = %s", (listbox.get(ACTIVE)))
        connector.commit()
        mb.showinfo("Success!", "Contact was deleted succesfully")
        listbox.delete(0, END)
        list_contacts()

def delete_all_records():
    pass

def list_contacts():
    global cur
    cur.execute("select name from db.Pokemon_Data")
    fetch = cur.fetchall()
    for data in fetch:
        listbox.insert(END, data)

root = Tk()
root.title("Manage Cards")
root.geometry("700x500")
root.resizable(0, 0)

gray = "gray70"
gray57 = "gray57"
gray35 = "gray35"

frame_font = ("Garamond", 14)

title_label = Label(root, text = "Manage Cards", font = ("Arial", 18), bg = "black", fg = "white")
left_frame = Frame(root, bg = gray)
center_frame = Frame(root, bg = gray57)
right_frame = Frame(root, bg = gray35)

title_label.pack(side = TOP, fill = X)
left_frame.place(relx = 0, relheight = 1, y = 30, relwidth = 0.3)
center_frame.place(relx = 0.3, relheight = 1, y = 30, relwidth = 0.3)
right_frame.place(relx = 0.6, relheight = 1, y = 30, relwidth = 0.4)

#### Frame 1 Populating ####
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()
address_strvar = StringVar()
search_strvar = StringVar()

pokemon_header = Label(left_frame, text = "Pokemon Details", bg = gray57, font = ("Arial", 20)).place(relx = 0.10, rely = 0.05)

name_label = Label(left_frame, text = "Name", bg = gray, font = frame_font).place(relx = 0.3, rely = 0.13)
name_entry = Entry(left_frame, width = 15, font = ("Verdana", 11), textvariable = name_strvar)
name_entry.place(relx = 0.1, rely = 0.18)

phone_label = Label(left_frame, text = "Attack", bg = gray, font = frame_font).place(relx = 0.28, rely = 0.33)
phone_entry = Entry(left_frame, width = 15, font = ("Verdana", 11), textvariable = phone_strvar)
phone_entry.place(relx = 0.1, rely = 0.38)

email_label = Label(left_frame, text = "Health", bg = gray, font = frame_font).place(relx = 0.3, rely = 0.53)
email_entry = Entry(left_frame, width = 15, font = ("Verdana", 11), textvariable = email_strvar)
email_entry.place(relx = 0.1, rely = 0.58)

address_label = Label(left_frame, text = "Type", bg = gray, font = frame_font).place(relx = 0.28, rely = 0.73)
address_entry = Entry(left_frame, width = 15, font = ("Verdana", 11), textvariable = address_strvar)
address_entry.place(relx = 0.1, rely = 0.78)

#### Frame 2 Populating ####
search_entry = Entry(center_frame, width = 18, font = ("Verdana", 12), textvariable = search_strvar)
search_entry.place(relx = 0.13, rely = 0.04)
search_button = Button(center_frame, text = "Search", font = frame_font, width = 15, command = search).place(relx = 0.13, rely = 0.1)

add_record_button = Button(center_frame, text = "Add Pokemon", font = frame_font, width = 15, command = submit_record).place(relx = 0.13, rely = 0.2)
view_records_button = Button(center_frame, text = "View Pokemon", font = frame_font, width = 15, command = view_record).place(relx = 0.13, rely = 0.3)
clear_fields_button = Button(center_frame, text = "Clear Fields", font = frame_font, width = 15, command = clear_fields).place(relx = 0.13, rely = 0.4)
delete_record_button = Button(center_frame, text = "Delete Pokemon", font = frame_font, width = 15, command = delete_record).place(relx = 0.13, rely = 0.5)
delete_all_records_button = Button(center_frame, text = "Delete All Pokemon", font = frame_font, width = 15, command = delete_all_records).place(relx = 0.13, rely = 0.6)

saved_contacts_label = Label(right_frame, text = "Saved Pokemon", bg = gray57, font = frame_font).place(relx = 0.25, rely = 0.05)
listbox = Listbox(right_frame, selectbackground = "SkyBlue", bg = 'Gainsboro', font = ('Helvetica', 12), height = 20, width = 25)
scrollbar = Scrollbar(listbox, orient = VERTICAL, command = listbox.yview)
scrollbar.place(relx = 3.93, rely = 0, relheight = 1)
listbox.config(yscrollcommand = scrollbar.set)
listbox.place(relx = 0.1, rely = 0.15)

root.mainloop()
