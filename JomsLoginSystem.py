from tkinter import *
from supabase import create_client
from datetime import datetime
from cryptography.fernet import Fernet
import os
key = b'G6UAzLBsNvjBxtX0_t3YIXYu1l4_GPveQqkmWraVSMA='
cipher = Fernet(key)
dt = datetime.now()
date = dt.strftime("%Y-%m-%d")

url = "https://wflctqihcpwthiurslqq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndmbGN0cWloY3B3dGhpdXJzbHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwMzgwMjMsImV4cCI6MjA3MzYxNDAyM30.35KUeEfKNO6Teil9Gv0_aN6Q6S0K-9YWi-YDcZ6q-JY"
account = create_client(url,key)

gui = Tk()
gui.title("Jomar Naval Login System")
if os.path.exists("JLS.ico"):
    gui.iconbitmap("JLS.ico")
gui.configure(bg="black")
class navs:
    @staticmethod
    def window(x):
        gui.geometry(x)
    @staticmethod
    def newWindow():
        for windows in gui.winfo_children():
            windows.destroy()
    def entrybox(self):
        self.ent = Entry(gui)
        self.ent.pack()
    def textlabel(self, text):
        self.textL = Label(gui,text=text,bg="black", fg="yellow", font=("Arial", 20, "bold"))
        self.textL.pack()
    def buttonSet(self,x,y):
        self.btn = Button(gui,text=x,command=y, width=15, height=2, font=("Arial", 12, "bold"), bg="yellow", fg="black")
        self.btn.pack(pady=5)
        
ui = navs()

def checkAcc():
    a = un.get().strip()
    b = pw.get().strip()

    # Fetch user
    result = account.from_("users") \
        .select("password") \
        .eq("username", a) \
        .execute()

    if not result.data:
        txt.config(text="Invalid account, create below")
        return

    stored_encrypted_str = result.data[0]["password"]
    stored_encrypted_bytes = stored_encrypted_str.encode("utf-8")
    decrypted_password = cipher.decrypt(stored_encrypted_bytes).decode("utf-8")

    if b == decrypted_password:
        mainpage(a)
    else:
        txt.config(text="Invalid account, create below")
def crAcc():
    a = cun.get().strip()
    b = cpw.get().strip()

    if a == "" or b == "":
        tx.config(text="Empty Input, Please Input!")
        return

    password_bytes = b.encode("utf-8")
    encrypted = cipher.encrypt(password_bytes)
    encrypted_str = encrypted.decode("utf-8")
    
    check = account.from_("users") \
        .select("username") \
        .eq("username", a) \
        .execute()

    if check.data:
        tx.config(text="Username already used!")
        return

    account.from_("users").insert({
        "username": a,
        "password": encrypted_str
    }).execute()

    tx.config(text="Account Created!")
    login()

def login():
    ui.newWindow()
    global un,pw,txt
    ui.window("600x400")
    ui.textlabel("Username")
    un = Entry(gui,bg="yellow", width=25, font=("Arial",20,"bold"), fg="black")
    un.pack(pady=20, padx=20)
    ui.textlabel("Password")
    pw = Entry(gui,bg="yellow", width=25, font=("Arial",20,"bold"), fg="black")
    pw.pack(pady=20, padx=20)
    txt = Label(gui,text='',bg="black", fg="yellow", pady=10, font=("Arial", 20, "bold"))
    txt.pack()
    ui.buttonSet("Login",checkAcc)
    ui.buttonSet("Create Account",createAcc)
    
def createAcc():
    ui.newWindow()
    global cun,cpw,tx
    ui.textlabel("Create Username")
    cun = Entry(gui,bg="yellow", width=25, font=("Arial",20,"bold"), fg="black")
    cun.pack(padx=10,pady=20)
    ui.textlabel("Create Password")
    cpw = Entry(gui,bg="yellow", width=25, font=("Arial",20,"bold"), fg="black")
    cpw.pack()
    ui.buttonSet("Create",crAcc)
    tx = Label(gui,text='',bg="black", fg="yellow", pady=10, font=("Arial", 20, "bold"))
    tx.pack()
    
def mainpage(uname):
    ui.newWindow()
    ui.textlabel(f"Hello {uname}, Welcome")
    ui.buttonSet("Logout", login)
login()
gui.mainloop()