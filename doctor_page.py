from tkinter import*
from tkinter import messagebox
import datetime
import mysql.connector
class paitent(database):
    def __init__(self,master):
        self.button_value =1
        self.master = master
        self.paitent_name = StringVar()
        self.date_of_visit = datetime.datetime.now().strftime("%I:%M %p , %d-%b-%Y")
        self.fever = StringVar()
        self.weight = StringVar()
        self.next_visit = StringVar()
        self.opd_id = StringVar()
        self.problem = StringVar()
        self.widget()
    def store(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mohit")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS paitent_sysytem")
        mycursor.execute("USE paitent_sysytem")
        mycursor.execute("CREATE TABLE IF NOT EXISTS paitent (paitent_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                         "paitent_name VARCHAR(50),date_of_visit VARCHAR(55),weight VARCHAR(10),fever VARCHAR(10),"
                         "next_visit VARCHAR(55),opd_id VARCHAR(10),problem VARCHAR(10000))")
        mycursor.execute("INSERT INTO paitent(paitent_name,date_of_visit,weight,fever,opd_id)VALUES(%s,%s,%s,%s,%s)",(self.paitent_name.get(),
                                                                                                                      self.date_of_visit,
                                                                                                                      self.weight.get(),
                                                                                                                      self.fever.get(),
                                                                                                                      self.opd_id.get()))
        mydb.commit()
    def submit(self):

        messagebox.showinfo("succeed","Paitent Details are Recorded Sucessfully.")
        self.paitent_name_e.delete(0,'end')
        self.fever_e.delete(0,'end')
        self.opd_id_e.delete(0,'end')
        self.weight_e.delete(0,'end')
        self.button_value = 2
    def new_entry(self):
        if(self.button_value==2):
            self.entry_frame.grid_forget()
        self.entry_frame = Frame(self.master, padx=5, pady=5)
        self.head = Label(self.entry_frame, text='NEW PAITENT', font=('', 35), pady=10)
        self.head.grid(row=0, column=0)
        paitent_name_l = Label(self.entry_frame, text='Paitent Name: ', font=('', 20), pady=5, padx=5)
        paitent_name_l.grid(row=1, column=0)
        self.paitent_name_e = Entry(self.entry_frame, textvariable=self.paitent_name, bd=5, font=('', 15))
        self.paitent_name_e.grid(row=1, column=1)
        fever_l = Label(self.entry_frame, text='Fever: ', font=('', 20), pady=5, padx=5)
        fever_l.grid(row=2, column=0)
        self.fever_e = Entry(self.entry_frame, textvariable=self.fever, bd=5, font=('', 15), show='*')
        self.fever_e.grid(row=2, column=1)
        opd_id_l = Label(self.entry_frame, text='OPD ID: ', font=('', 20), pady=5, padx=5)
        opd_id_l.grid(row=3, column=0)
        self.opd_id_e = Entry(self.entry_frame, textvariable=self.opd_id, bd=5, font=('', 15), show='*')
        self.opd_id_e.grid(row=3, column=1)
        weight_l = Label(self.entry_frame, text='Weight: ', font=('', 20), pady=5, padx=5)
        weight_l.grid(row=4, column=0)
        self.weight_e = Entry(self.entry_frame, textvariable=self.weight, bd=5, font=('', 15), show='*')
        self.weight_e.grid(row=4, column=1)
        Button(self.entry_frame, text=' SUBMIT ', bd=3, font=('', 15), padx=5, pady=5, command=self.submit).grid()
        self.entry_frame.grid()
    def list_all(self):
        print("hello")
    def widget(self):

        title1 = Label(self.master, text="Paitent Menu", font=('bold', 30))
        title1.grid()
        self.menu_frame = Frame(self.master, padx=5, pady=5)
        self.menu_frame.grid()
        new_paitent = Button(self.menu_frame, text="New Paitent", font=('bold', 20), command=self.new_entry)
        new_paitent.grid(row=1, column=1, pady=100, ipadx=50)
        list_all = Button(self.menu_frame, text="List All", font=('bold', 20), command=self.list_all)
        list_all.grid(row=1, column=2, pady=100, ipadx=50)
        search = Button(self.menu_frame, text="Search", font=('bold', 20))
        search.grid(row=1, column=3, pady=100, ipadx=50)
        edit = Button(self.menu_frame, text="Edit", font=('bold', 20))
        edit.grid(row=1, column=4, pady=100, ipadx=50)
        delete = Button(self.menu_frame, text="Delete", font=('bold', 20))
        delete.grid(row=1, column=5, pady=100, ipadx=50)

if __name__ == '__main__':
    window = Tk()
    paitent(window)
    window.mainloop()