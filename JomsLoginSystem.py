from tkinter import *
from supabase import create_client
from datetime import datetime

dt = datetime.now()
date = dt.strftime("%Y-%m-%d")

url = 'https://wflctqihcpwthiurslqq.supabase.co'
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndmbGN0cWloY3B3dGhpdXJzbHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwMzgwMjMsImV4cCI6MjA3MzYxNDAyM30.35KUeEfKNO6Teil9Gv0_aN6Q6S0K-9YWi-YDcZ6q-JY"

account = create_client(url,key)

gui = Tk()
gui.title("Jomar Naval Login System")
gui.iconbitmap("JLS.ico")
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
        self.textL = Label(gui,text=text)
        self.textL.pack()
    def buttonSet(self,x,y):
        self.btn = Button(gui,text=x,command=y)
        self.btn.pack()
        
ui = navs()

def checkAcc():
    a = un.get()
    b = pw.get()

    result = account.table("LogSysContractorIssue") \
    .select("*") \
    .eq("username", a) \
    .eq("password", b) \
    .execute()
    if result.data:
        mainpage(a)
    else:
        txt.config(text="invalid account, create below")

def crAcc():
    a = cun.get()
    b = cpw.get()

    result = account.table("LogSysContractorIssue") \
    .select("*") \
    .eq("username", a) \
    .execute()
    if result.data:
        tx.config(text="username already used!")
    else:
        account.table("LogSysContractorIssue").insert({
        "accountdateCreated" : date ,
        "username" : a,
        "password" : b
        }).execute()
        tx.config(text="Account Created!")
        login()     

def login():
    ui.newWindow()
    global un,pw,txt
    ui.window("600x400")
    ui.textlabel("Username")
    un = Entry(gui)
    un.pack()
    ui.textlabel("Password")
    pw = Entry(gui)
    pw.pack()
    txt = Label(gui,text='')
    txt.pack()
    ui.buttonSet("Login",checkAcc)
    ui.buttonSet("Create Account",createAcc)
    
def createAcc():
    ui.newWindow()
    global cun,cpw,tx
    ui.textlabel("Create Username")
    cun = Entry(gui)
    cun.pack()
    ui.textlabel("Create Password")
    cpw = Entry(gui)
    cpw.pack()
    ui.buttonSet("Create",crAcc)
    tx = Label(gui,text='')
    tx.pack()
    
def mainpage(uname):
    ui.newWindow()
    ui.textlabel(f"Hello {uname}, Welcome")
    ui.buttonSet("Logout", login)
login()
gui.mainloop()