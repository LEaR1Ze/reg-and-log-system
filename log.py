from logging import root
import mysql.connector
import tkinter as tk
from tkinter import *
import time

connection = mysql.connector.connect(host="________",user="______",password="____",database="_____") 

print("#" * 20)
print ("connect successful!!")
ttr=connection.cursor()

def log():
    global user1
    global passw1
    global root2
    root2 = Toplevel(root1)
    root2.title("Поле Входа")
    root2.geometry("275x175")
    user1 = StringVar()
    passw1 = StringVar()

    Label(root2,text="Логин").pack()
    Entry(root2,textvariable=user1).pack()
    Label(root2,text="Пароль").pack()
    Entry(root2,textvariable=passw1,show="*").pack()

    Label(root2,text="").pack()
    Button(
            root2,
            text="Войти",
            fg ="white",
            bg ="black",
            width=25,
            height=2,
            command=log_succ
    ).pack()   
 
def log_succ():
    user = user1.get()
    passw = passw1.get()
    sql = "select * from clients where username = %s and password = %s"
    ttr.execute(sql,[(user),(passw)])
    results = ttr.fetchall()
    if results:
        for i in results:
            print("#" * 20)
            print ("Вы вошли в систему")
            break
        time.sleep(1)
        exit()
    else:
        print("#" * 20)
        print ("Пароль или логын не верный")

def reg_succ():
    inf1 = username.get()
    inf2 = password.get()
    inf3 = password23.get()
    if inf3 != inf2:
        print("#" * 20)
        print("Пароли должны быть одинаковыми!!")
    else: 
        True 
        terp = "INSERT INTO clients (username, password) VALUES (%s,%s)"
        prop = (inf1, inf2)
        ttr.execute(terp,prop)
        connection.commit()
        time.sleep(0.50)
        print("#" * 20)
        print("Вы зарегистрировались!")
        time.sleep(0.5)


def reg():
    global root1
    root1 = Toplevel(root)
    root1.title("Регестрация")
    root1.geometry("275x200")
    global username
    global password
    global password23
    password23 = StringVar()
    username = StringVar()
    password = StringVar()
    Label(root1,text="Логин").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1,text="Пароль").pack()
    Entry(root1,textvariable=password,show="*").pack()
    Label(root1,text="Повторите пароль").pack()
    Entry(root1,textvariable=password23,show="*").pack()
    Label(root1,text="").pack()
    Button(
    root1,
    text="Зарегестрироваться",
    fg ="white",
    bg ="black",
    width=20,
    height=2,
    command=reg_succ
    ).pack()
    Label(root1,text="").pack()


def main_screen():
    global root
    root = Tk()
    root.title("Вход")
    root.geometry("275x175")
    Label(root,text="Добро пожаловать в меню Входа",font="bold",bg="white",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Войти",width="8",height="1",bg="red",font="bold",fg="white",command=log).pack()
    Label(root,text="").pack()
    Button(root, text="Регестрация",height="1",width="15",bg="red",font="bold",fg="white",command=reg).pack()

main_screen()
root.mainloop()
