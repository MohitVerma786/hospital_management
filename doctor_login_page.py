from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import home_page

# main Class
class main:
    def __init__(self, master):

        self.master = master
        self.master.geometry("800x450+260+110")
        self.master.title("LOGIN PAGE")
        self.username = StringVar()
        self.password = StringVar()
        self.widgets()
    def back(self):
        self.master.destroy()
        root = Tk()
        home_page.homepage(root)
        root.mainloop()
    # Login Function
    def login(self):
        if self.username.get()=="mohit" and self.password.get()=="12345":
            print("welcome")
        else:
            messagebox.showerror("Error","username or password is incorrect")

    # Draw Widgets
    def widgets(self):
        self.logf = Frame(self.master, bg='#d9d9d9', padx=10, pady=10)
        self.logf.place(height=500, width=800)
        self.TSeparator1 = ttk.Separator(self.logf)
        self.TSeparator1.configure(orient="vertical")
        self.TSeparator1.place(x=480, y=5, height=420)
        pic1 = Image.open('images/doctor.png')
        pic1 = pic1.resize((150, 150), Image.ANTIALIAS)
        self.pic1 = ImageTk.PhotoImage(pic1)

        self.head_image = Label(self.logf, image=self.pic1, bg='#d9d9d9')
        self.head_image.place(x=150, y=40)
        self.head_label = Label(self.logf, bg='#d9d9d9', text="DOCTOR LOGIN", font=('', 30)).place(x=90, y=180)
        self.user_label = Label(self.logf, bg='#d9d9d9', text="USERNAME:", font=('', 15)).place(x=490, y=140)
        self.user_entry = Entry(self.logf, textvariable=self.username, font=('', 10)).place(x=620, y=146)
        self.password_label = Label(self.logf, bg='#d9d9d9', text="PASSWORD:", font=('', 15)).place(x=490, y=180)
        self.user_entry = Entry(self.logf, textvariable=self.password, font=('', 10), show="*").place(x=620, y=186)
        self.button = Button(self.logf, text="LOGIN", background='#d9d9d9', font=('', 13), command=self.login).place(x=580, y=240)
        pic2 = Image.open('images/back.png')
        pic2 = pic2.resize((35, 35), Image.ANTIALIAS)
        self.pic2 = ImageTk.PhotoImage(pic2)
        self.back_button_i = Button(self.logf, image=self.pic2, bg='#94b1b9', relief='groove',
                                    activebackground='#94b1b9', command=self.back).place(x=5, y=5)

