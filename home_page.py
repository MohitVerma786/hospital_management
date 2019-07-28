from tkinter import*
from PIL import Image,ImageTk
import paitent_login_page
class homepage:
    def paitent(self):
        self.master.destroy()
        root = Tk()
        paitent_login_page.main(root)
        root.mainloop()
    def doctor(self):
        self.master.destroy()
        root = Tk()
        doctor_login_page.main(root)
        root.mainloop()
    def admin(self):
        import admin_login_page


    def __init__(self,master):
        self.master = master
        self.widgets()
    def widgets(self):
        hei = self.master.winfo_screenheight()
        wid = self.master.winfo_screenwidth()
        self.frame = Frame(self.master, width=wid, height=hei)
        self.frame.pack()
        self.canvas = Canvas(self.frame, width=wid, height=hei)
        self.canvas.pack()
        c_img = Image.open("images/main.png")
        c_img = c_img.resize((wid,hei), Image.ANTIALIAS)
        self.canvas.img = ImageTk.PhotoImage(c_img)
        self.canvas.create_image(0,0,image=self.canvas.img, anchor=NW)
        self.paitent_button = Button(self.canvas, text="Paitent", bd=12, font=('', 40), padx=5, pady=5, command=self.paitent)
        self.canvas.create_window(50,630,window=self.paitent_button, anchor=SW)
        self.doctor_button = Button(self.canvas, text="Doctor", bd=12, font=('', 40), padx=5, pady=5, command=self.doctor)
        self.canvas.create_window(400,630,window=self.doctor_button, anchor=SW)
        self.admin_button = Button(self.canvas, text="Admin", bd=12, font=('', 40), padx=5, pady=5, command=self.admin)
        self.canvas.create_window(800,630,window=self.admin_button, anchor=SW)



if __name__ == '__main__':
    window = Tk()
    obj = homepage(window)

    window.mainloop()