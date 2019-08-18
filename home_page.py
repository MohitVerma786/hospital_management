from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import paitent_login_page
import doctor_login_page
import admin_login_page
class homepage:
    def staff(self):
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
        self.master.destroy()
        root = Tk()
        admin_login_page.main(root)
        root.mainloop()


    def __init__(self,master):
        self.master = master
        self.master.geometry('1000x600+150+50')
        self.master.title("Hospital Management System")
        self.widgets()
    def widgets(self):
        self.headframe = Frame(self.master, bg='#94b1b9')
        self.headframe.place(height=600, width=1000)
        head_label = Label(self.headframe, text="Hospital Management System", bg='#94b1b9', font=('',30))
        head_label.place(x=240, y=14)
        seprator1 = ttk.Separator(self.headframe, orient="horizontal")
        seprator1.place(x=50, y=80, width=895)
        seprator2 = ttk.Separator(self.headframe, orient="vertical")
        seprator2.place(x=500, y=100, height=330)
        pic1 = Image.open('images/staff.png')
        pic1 = pic1.resize((150, 150), Image.ANTIALIAS)
        self.pic1 = ImageTk.PhotoImage(pic1)
        self.staff_button_i = Button(self.headframe, image=self.pic1, bg='#94b1b9', relief='groove',
                                     activebackground='#94b1b9', command=self.staff)
        self.staff_button_i.place(x=170, y=170)
        self.staff_button = Button(self.headframe, text="STAFF LOGIN", font=('',15,'bold'), bg='#94b1b9',
                                   relief='groove', activebackground='#94b1b9', command=self.staff)
        self.staff_button.place(x=173, y=325)
        pic2 = Image.open('images/doctor.png')
        pic2 = pic2.resize((150,150), Image.ANTIALIAS)
        self.pic2 = ImageTk.PhotoImage(pic2)
        self.doctor_button_i = Button(self.headframe, image=self.pic2, bg='#94b1b9', relief='groove',
                                       activebackground='#94b1b9', command=self.doctor)
        self.doctor_button_i.place(x=670, y=170)
        self.doctor_button = Button(self.headframe, text="DOCTOR LOGIN", font=('', 15, 'bold'), bg='#94b1b9',
                                     relief='groove', activebackground='#94b1b9', command=self.doctor)
        self.doctor_button.place(x=662, y=325)
        pic3 = Image.open('images/admin.png')
        pic3 = pic3.resize((100, 100), Image.ANTIALIAS)
        self.pic3 = ImageTk.PhotoImage(pic3)
        self.admin_button_i = Button(self.headframe, image=self.pic3, bg='#94b1b9', relief='groove',
                                     activebackground='#94b1b9', command=self.admin)
        self.admin_button_i.place(x=447, y=450)
        self.admin_button = Button(self.headframe, text="ADMIN LOGIN", font=('', 12, 'bold'), bg='#94b1b9',
                                   relief='groove', activebackground='#94b1b9', command=self.admin)
        self.admin_button.place(x=440, y=555)



if __name__ == '__main__':
    window = Tk()
    obj = homepage(window)

    window.mainloop()