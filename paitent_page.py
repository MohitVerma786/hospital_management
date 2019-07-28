from tkinter import*
from tkinter import messagebox
import datetime
import mysql.connector
class paitent:
    def __init__(self,master):
        self.button_value =1
        self.master = master
        self.paitent_name = StringVar()
        self.fever = StringVar()
        self.weight = StringVar()
        self.next_visit = StringVar()
        self.opd_id = StringVar()
        self.problem = StringVar()
        self.amount = StringVar()
        self.widget()
    def store(self):
        date_of_visit = datetime.datetime.now().strftime("%I:%M:%S %p , %d-%b-%Y")
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mohit")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS paitent_sysytem")
        mycursor.execute("USE paitent_sysytem")
        mycursor.execute("CREATE TABLE IF NOT EXISTS paitent (paitent_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,trans_id VARCHAR(20),"
                         "paitent_name VARCHAR(50),date_of_visit VARCHAR(55),"
                         "weight VARCHAR(10),fever VARCHAR(10),next_visit VARCHAR(55),opd_id VARCHAR(10),problem VARCHAR(10000),amount VARCHAR(50))")
        mycursor.execute("INSERT INTO paitent(paitent_name,date_of_visit,opd_id,amount,trans_id)VALUES(%s,%s,%s,%s,%s)",(str(self.paitent_name.get()),
                                                                                                                      str(date_of_visit),
                                                                                                                      str(self.opd_id.get()),
                                                                                                                    str(self.amount.get()),
                                                                                                                         str(datetime.datetime.now().strftime("%I%M%p%d%b%Y"))))
        mydb.commit()
        mycursor.close()
        mydb.close()
    def submit(self):

        messagebox.showinfo("succeed","Paitent Details are Recorded Sucessfully.")
        self.paitent_name_e.delete(0,'end')
        self.fever_e.delete(0,'end')
        self.opd_id_e.delete(0,'end')
        self.weight_e.delete(0,'end')
        self.button_value = 2
    def print(self):
        date_of_visit = datetime.datetime.now().strftime("%I:%M:%S %p , %d-%b-%Y")
        self.store()
        messagebox.showinfo("succeed","Recipt Details are Recorded Sucessfully.")
        self.button_value = 2
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="mohit")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent WHERE date_of_visit = %s",(str(date_of_visit), ))
        record = mycursor.fetchall()
        for row in record:
            print("current_paitent_id =", row[0])

        messagebox.showinfo("succeed", "Recipt Is Printed Sucessfully.")
        mycursor.close()
        mydb.close()
        self.recipt_frame.grid_forget()
        self.menu_frame.grid_forget()
        self.widget()
        self.recipt()

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
        Button(self.entry_frame, text=' SUBMIT ', bd=3, font=('', 15), padx=5, pady=5, command=self.print).grid()
        self.entry_frame.grid()
    def list_all(self):
        root = Tk()
        self.list_all_frame = Frame(root, padx=5, pady=5)
        self.list_all_frame.pack()
        self.head = Label(self.list_all_frame, text='LIST OF ALL PATIENTS', font=('', 35), pady=10)
        self.head.pack()
        scroll_bar = Scrollbar(self.list_all_frame)
        text_box = Text(self.list_all_frame,width=200,height=50)
        scroll_bar.pack(side=RIGHT,fill=Y)
        text_box.pack(side=LEFT,fill=Y)
        scroll_bar.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_bar.set)
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="mohit")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent")
        record = mycursor.fetchall()
        for row in record:
            text_box.insert(END, "| Paitent id: " + str(row[0]) + "| Transition ID: " + str(row[1]) + "| Patient Name: " + str(row[2]) +
                     "| Date Of Visit: " + str(row[3]) + "| Weight: " + str(row[4]) + "| Fever: " + str(row[5]) +
                     "| Next Visit: " + str(row[6]) + "| OPD ID: " + str(row[7]) + "| Problem: " + str(row[8]) +
                     "| Amount: " + str(row[9]) + "\n")

        root.mainloop()
        mycursor.close()
        mydb.close()

    def recipt(self):
        date_of_visit = datetime.datetime.now().strftime("%I:%M:%S %p , %d-%b-%Y")
        if(self.button_value==2):
            self.recipt_frame.grid_forget()
        self.recipt_frame = Frame(self.master, padx=5, pady=5)
        self.head = Label(self.recipt_frame, text='NEW APPOINTMENT', font=('', 35), pady=10)
        self.head.grid(row=0, column=0)
        paitent_name_l = Label(self.recipt_frame, text='Paitent Name: ', font=('', 20), pady=5, padx=5)
        paitent_name_l.grid(row=1, column=0)
        self.paitent_name_e = Entry(self.recipt_frame, textvariable=self.paitent_name, bd=5, font=('', 15))
        self.paitent_name_e.grid(row=1, column=1)
        dov = Label(self.recipt_frame, text='Date Of Visit: ', font=('', 20), pady=5, padx=5)
        dov.grid(row=2, column=0)
        dovl = Label(self.recipt_frame, text=date_of_visit, font=('', 20), pady=5, padx=5)
        dovl.grid(row=2, column=1)
        opd_id_l = Label(self.recipt_frame, text='OPD ID: ', font=('', 20), pady=5, padx=5)
        opd_id_l.grid(row=3, column=0)
        self.opd_id_e = Entry(self.recipt_frame, textvariable=self.opd_id, bd=5, font=('', 15),)
        self.opd_id_e.grid(row=3, column=1)
        amt_l = Label(self.recipt_frame, text='Amount: ', font=('', 20), pady=5, padx=5)
        amt_l.grid(row=4, column=0)
        self.amt_e = Entry(self.recipt_frame, textvariable=self.amount, bd=5, font=('', 15),)
        self.amt_e.grid(row=4, column=1)
        Button(self.recipt_frame, text=' PRINT ', bd=3, font=('', 15), padx=5, pady=5, command=self.print).grid()
        self.recipt_frame.grid()
        self.button_value=2
    def widget(self):


        self.menu_frame = Frame(self.master, padx=5, pady=5)
        self.menu_frame.grid()
        title1 = Label(self.menu_frame, text="Paitent Menu", font=('bold', 30))
        title1.grid(row=0, column=2)
        new_paitent = Button(self.menu_frame, text="New Appointment", font=('bold', 20), command=self.recipt)
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