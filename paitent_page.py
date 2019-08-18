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
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
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

        self.opd_id_e.delete(0,'end')

        self.button_value = 2
    def print(self):
        date_of_visit = datetime.datetime.now().strftime("%I:%M:%S %p , %d-%b-%Y")
        if (str(self.paitent_name.get()) == "" or str(self.opd_id.get()) == "" or str(self.amount.get()) == ""):
            messagebox.showerror("Error","Provide All The Values")
        else:
            self.store()
            messagebox.showinfo("succeed","Recipt Details are Recorded Sucessfully.")
            self.button_value = 2
            mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
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
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent")
        record = mycursor.fetchall()
        for row in record:
            text_box.insert(END, "| Paitent id: " + str(row[0]) + "| Transition ID: " + str(row[1]) + "| Patient Name: " + str(row[2]) +
                     "| Date Of Visit: " + str(row[3]) + "| Weight: " + str(row[4]) + "| Fever: " + str(row[5]) +
                     "| Next Visit: " + str(row[6]) + "| OPD ID: " + str(row[7]) + "| Problem: " + str(row[8]) +
                     "| Amount: " + str(row[9]) + "\n")


        mycursor.close()
        mydb.close()
        root.mainloop()

    def find(self):
        scroll_bar = Scrollbar(self.search_frame)
        text_box = Text(self.search_frame, width=200, height=50)
        scroll_bar.pack(side=RIGHT, fill=Y)
        text_box.pack(side=LEFT, fill=Y)
        scroll_bar.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_bar.set)
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent WHERE paitent_id = %s", (str(self.paitent_search_e.get()),))
        record = mycursor.fetchall()
        for row in record:
            text_box.insert(END, "| Paitent id: " + str(row[0]) + "| Transition ID: " + str(
                row[1]) + "| Patient Name: " + str(row[2]) +
                            "| Date Of Visit: " + str(row[3]) + "| Weight: " + str(row[4]) + "| Fever: " + str(
                row[5]) +
                            "| Next Visit: " + str(row[6]) + "| OPD ID: " + str(row[7]) + "| Problem: " + str(
                row[8]) +
                            "| Amount: " + str(row[9]) + "\n")

        mycursor.close()
        mydb.close()


    def reset_find(self,master):
        master.destroy()
        self.search()
    def delete(self,master):

        wanna = messagebox.askyesno("Confirm","Are You Sure You Want To Delete This Patient Details From Records")
        if(wanna):
            mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
            mycursor = mydb.cursor()
            mycursor.execute("DELETE FROM paitent WHERE paitent_id = %s", (str(self.paitent_search_e.get()),))
            mydb.commit()
            mycursor.close()
            mydb.close()
            messagebox.showinfo("sucess","Sucessfully Deleted")
            master.destroy()
            self.search()
        elif wanna!=TRUE:
            master.destroy()
            self.search()
    def search(self):
        root = Tk()

        self.search_frame = Frame(root, padx=5, pady=5)
        self.search_frame.pack()
        self.head = Label(self.search_frame, text='SEARCH FOR PATIENTS', font=('', 35), pady=10)
        self.head.pack()
        paitent_search_l = Label(self.search_frame, text='Paitent ID: ', font=('', 20), pady=5, padx=5)
        paitent_search_l.pack()

        self.paitent_search_e = Entry(self.search_frame, bd=5, font=('', 15))
        self.paitent_search_e.pack()
        find_button = Button(self.search_frame, text=' Search ', bd=3, font=('', 15), padx=5, pady=5, command=self.find)
        find_button.pack(side=TOP)
        reset_button = Button(self.search_frame, text=' Reset ', bd=3, font=('', 15), padx=5, pady=5, command=lambda:self.reset_find(root))
        reset_button.pack(side=TOP)
        delete_button = Button(self.search_frame, text=' Delete ', bd=3, font=('', 15), padx=5, pady=5, command=lambda:self.delete(root))
        delete_button.pack(side=TOP)
        edit_button = Button(self.search_frame, text=' Edit or Update ', bd=3, font=('', 15), padx=5, pady=5, command=lambda:self.update(root))
        edit_button.pack(side=TOP)

        root.mainloop()
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
    def edit_name(self):
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE paitent SET paitent_name = %s WHERE  paitent_id = %s", (self.name_update_e.get(),str(self.current_paitent_update[0])))
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("sucess","Sucessfully Updated")
    def edit_opd(self):
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE paitent SET opd_id = %s WHERE  paitent_id = %s",
                         (self.update_opd_e.get(), str(self.current_paitent_update[0])))
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("sucess", "Sucessfully Updated")

    def edit_amount(self):
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE paitent SET amount = %s WHERE  paitent_id = %s",
                         (self.amount_update_e.get(), str(self.current_paitent_update[0])))
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("sucess", "Sucessfully Updated")
    def update(self,master):
        self.temp = str(self.paitent_search_e.get())
        master.destroy()
        root = Tk()
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent WHERE paitent_id = %s", (self.temp,))
        record = mycursor.fetchone()
        self.current_paitent_update = record
        self.update_frame = Frame(root, padx=5, pady=5)
        self.update_frame.grid()
        self.head = Label(self.update_frame, text='EDIT OR UPDATE DETAILS', font=('', 35), pady=10)
        self.head.grid(row=0,column=0)
        paitent_id_update_l = Label(self.update_frame, text='Paitent ID: ', font=('', 20), pady=5, padx=5)
        paitent_id_update_l.grid(row=1,column=0)
        id_update_e = Label(self.update_frame, text=str(record[0]), font=('', 20), pady=5, padx=5)
        id_update_e.grid(row=1,column=1)
        paitent_trans_update_l = Label(self.update_frame, text='Transaction ID: ', font=('', 20), pady=5, padx=5)
        paitent_trans_update_l.grid(row=2,column=0)
        id_update_e = Label(self.update_frame, text=str(record[1]), font=('', 20), pady=5, padx=5)
        id_update_e.grid(row=2,column=1)
        paitent_name_update_l = Label(self.update_frame, text='Paitent Name: ', font=('', 20), pady=5, padx=5)
        paitent_name_update_l.grid(row=3,column=0)
        self.name_update_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.name_update_e.insert(END, str(record[2]))
        self.name_update_e.grid(row=3,column=1)
        edit_name = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5, command=self.edit_name)
        edit_name.grid(row=3,column=2)
        paitent_dov_update_l = Label(self.update_frame, text='Date Of Visit: ', font=('', 20), pady=5, padx=5)
        paitent_dov_update_l.grid(row=4,column=0)
        dov_update_e = Label(self.update_frame, text=str(record[3]), font=('', 20), pady=5, padx=5)
        dov_update_e.grid(row=4,column=1)
        paitent_weight_update_l = Label(self.update_frame, text='Weight: ', font=('', 20), pady=5, padx=5)
        paitent_weight_update_l.grid(row=5, column=0)
        weight_update_e = Label(self.update_frame, text=str(record[4]), font=('', 20), pady=5, padx=5)
        weight_update_e.grid(row=5, column=1)
        paitent_fever_update_l = Label(self.update_frame, text='Fever: ', font=('', 20), pady=5, padx=5)
        paitent_fever_update_l.grid(row=6,column=0)
        fever_update_e = Label(self.update_frame, text=str(record[5]), font=('', 20), pady=5, padx=5)
        fever_update_e.grid(row=6,column=1)
        paitent_nv_update_l = Label(self.update_frame, text='Next Visit: ', font=('', 20), pady=5, padx=5)
        paitent_nv_update_l.grid(row=7,column=0)
        nv_update_e = Label(self.update_frame, text=str(record[6]), font=('', 20), pady=5, padx=5)
        nv_update_e.grid(row=7,column=1)
        paitent_opd_update_l = Label(self.update_frame, text='OPD ID: ', font=('', 20), pady=5, padx=5)
        paitent_opd_update_l.grid(row=8,column=0)
        self.update_opd_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.update_opd_e.insert(END, str(record[7]))
        self.update_opd_e.grid(row=8,column=1)
        edit_opd = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5, command=self.edit_opd)
        edit_opd.grid(row=8,column=2)
        paitent_problem_update_l = Label(self.update_frame, text='Problem: ', font=('', 20), pady=5, padx=5)
        paitent_problem_update_l.grid(row=9,column=0)
        problem_update_e = Label(self.update_frame, text=str(record[8]), font=('', 20), pady=5, padx=5)
        problem_update_e.grid(row=9,column=1)
        paitent_amount_update_l = Label(self.update_frame, text='Amount: ', font=('', 20), pady=5, padx=5)
        paitent_amount_update_l.grid(row=10,column=0)
        self.amount_update_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.amount_update_e.insert(END, str(record[9]))
        self.amount_update_e.grid(row=10,column=1)
        edit_amount = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5, command=self.edit_amount)
        edit_amount.grid(row=10,column=2)
        mycursor.close()
        mydb.close()
        root.mainloop()
    def widget(self):


        self.menu_frame = Frame(self.master,bd=50,bg='grey',height=500, width=100, padx=5, pady=5)
        self.menu_frame.place()
        title1 = Label(self.menu_frame, text="Paitent Menu", font=('bold', 30))
        title1.place()
        new_paitent = Button(self.menu_frame, text="New Appointment", font=('bold', 20), command=self.recipt)
        new_paitent.place()
        list_all = Button(self.menu_frame, text="List All", font=('bold', 20), command=self.list_all)
        list_all.place()
        search = Button(self.menu_frame, text="Search/Update/Edit", font=('bold', 20),  command=self.search)
        search.place()

if __name__ == '__main__':
    window = Tk()
    paitent(window)
    window.mainloop()
