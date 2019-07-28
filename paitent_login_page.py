from tkinter import *
from tkinter import messagebox


# main Class
class main:
    def __init__(self, master):

        self.master = master

        self.username = StringVar()
        self.password = StringVar()
        self.widgets()

    # Login Function
    def login(self):
        if self.username.get()=="mohit" and self.password.get()=="12345":
            print("welcome")
        else:
            messagebox.showerror("Error","username or password is incorrect")

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='PAITENT LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        self.logf.pack()



