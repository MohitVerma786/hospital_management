from tkinter import*
from tkinter import messagebox
import datetime
import mysql.connector
class doctor:
    def __init__(self,master,opd_id):
        self.master = master
        self.opd_id = opd_id
        self.widget()


    def attend(self,master):
        self.temp = str(self.paitent_search_e.get())
        master.destroy()
        root = Tk()
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="mohit")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent WHERE paitent_id = %s", (self.temp,))
        record = mycursor.fetchone()
        self.current_paitent_update = record
        self.update_frame = Frame(root, padx=5, pady=5)
        self.update_frame.grid()
        self.head = Label(self.update_frame, text=' DETAILS ', font=('', 35), pady=10)
        self.head.grid(row=0, column=0)
        paitent_id_update_l = Label(self.update_frame, text='Paitent ID: ', font=('', 20), pady=5, padx=5)
        paitent_id_update_l.grid(row=1, column=0)
        id_update_e = Label(self.update_frame, text=str(record[0]), font=('', 20), pady=5, padx=5)
        id_update_e.grid(row=1, column=1)
        paitent_trans_update_l = Label(self.update_frame, text='Transaction ID: ', font=('', 20), pady=5, padx=5)
        paitent_trans_update_l.grid(row=2, column=0)
        id_update_e = Label(self.update_frame, text=str(record[1]), font=('', 20), pady=5, padx=5)
        id_update_e.grid(row=2, column=1)
        paitent_name_update_l = Label(self.update_frame, text='Paitent Name: ', font=('', 20), pady=5, padx=5)
        paitent_name_update_l.grid(row=3, column=0)
        self.name_update_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.name_update_e.insert(END, str(record[2]))
        self.name_update_e.grid(row=3, column=1)
        edit_name = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5,
                           command=self.edit_name)
        edit_name.grid(row=3, column=2)
        paitent_dov_update_l = Label(self.update_frame, text='Date Of Visit: ', font=('', 20), pady=5, padx=5)
        paitent_dov_update_l.grid(row=4, column=0)
        dov_update_e = Label(self.update_frame, text=str(record[3]), font=('', 20), pady=5, padx=5)
        dov_update_e.grid(row=4, column=1)
        paitent_weight_update_l = Label(self.update_frame, text='Weight: ', font=('', 20), pady=5, padx=5)
        paitent_weight_update_l.grid(row=5, column=0)
        self.weight_update_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.weight_update_e.insert(END, str(record[2]))
        self.weight_update_e.grid(row=3, column=1)
        edit_weight = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5,
                           command=self.edit_weight)
        edit_weight.grid(row=3, column=2)
        paitent_fever_update_l = Label(self.update_frame, text='Fever: ', font=('', 20), pady=5, padx=5)
        paitent_fever_update_l.grid(row=6, column=0)
        self.fever_update_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.fever_update_e.insert(END, str(record[2]))
        self.fever_update_e.grid(row=3, column=1)
        edit_fever = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5,
                           command=self.edit_fever)
        edit_fever.grid(row=3, column=2)
        paitent_nv_update_l = Label(self.update_frame, text='Next Visit: ', font=('', 20), pady=5, padx=5)
        paitent_nv_update_l.grid(row=7, column=0)
        nv_update_e = Label(self.update_frame, text=str(record[6]), font=('', 20), pady=5, padx=5)
        nv_update_e.grid(row=7, column=1)
        paitent_opd_update_l = Label(self.update_frame, text='OPD ID: ', font=('', 20), pady=5, padx=5)
        paitent_opd_update_l.grid(row=8, column=0)
        self.update_opd_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.update_opd_e.insert(END, str(record[7]))
        self.update_opd_e.grid(row=8, column=1)
        edit_opd = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5,
                          command=self.edit_opd)
        edit_opd.grid(row=8, column=2)
        paitent_problem_update_l = Label(self.update_frame, text='Problem: ', font=('', 20), pady=5, padx=5)
        paitent_problem_update_l.grid(row=9, column=0)
        problem_update_e = Label(self.update_frame, text=str(record[8]), font=('', 20), pady=5, padx=5)
        problem_update_e.grid(row=9, column=1)
        paitent_amount_update_l = Label(self.update_frame, text='Amount: ', font=('', 20), pady=5, padx=5)
        paitent_amount_update_l.grid(row=10, column=0)
        self.amount_update_e = Entry(self.update_frame, bd=5, font=('', 15))
        self.amount_update_e.insert(END, str(record[9]))
        self.amount_update_e.grid(row=10, column=1)
        edit_amount = Button(self.update_frame, text=' Update ', bd=3, font=('', 15), padx=5, pady=5,
                             command=self.edit_amount)
        edit_amount.grid(row=10, column=2)
        mycursor.close()
        mydb.close()
        root.mainloop()

    def take_appointment(self):
        root = Tk()

        self.search_frame = Frame(root, padx=5, pady=5)
        self.search_frame.pack()
        self.head = Label(self.search_frame, text='ATTEND PATIENT', font=('', 35), pady=10)
        self.head.pack()
        paitent_search_l = Label(self.search_frame, text='Paitent ID: ', font=('', 20), pady=5, padx=5)
        paitent_search_l.pack()

        self.paitent_search_e = Entry(self.search_frame, bd=5, font=('', 15))
        self.paitent_search_e.pack()
        find_button = Button(self.search_frame, text=' Attend ', bd=3, font=('', 15), padx=5, pady=5, command=lambda:self.attend(root))
        find_button.pack(side=TOP)
        root.mainloop()
    def view_all_appointment(self):
        root = Tk()
        self.list_all_frame = Frame(root, padx=5, pady=5)
        self.list_all_frame.pack()
        self.head = Label(self.list_all_frame, text='LIST OF ALL PATIENTS', font=('', 35), pady=10)
        self.head.pack()
        scroll_bar = Scrollbar(self.list_all_frame)
        text_box = Text(self.list_all_frame, width=200, height=50)
        scroll_bar.pack(side=RIGHT, fill=Y)
        text_box.pack(side=LEFT, fill=Y)
        scroll_bar.config(command=text_box.yview)
        text_box.config(yscrollcommand=scroll_bar.set)
        mydb = mysql.connector.connect(host="localhost", database="paitent_sysytem", user="root", passwd="mohit")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM paitent WHERE opd_id = %s",(self.opd_id,))
        record = mycursor.fetchall()
        for row in record:
            text_box.insert(END, "| Paitent id: " + str(row[0]) + "| Transition ID: " + str(
                row[1]) + "| Patient Name: " + str(row[2]) +
                            "| Date Of Visit: " + str(row[3]) + "| Weight: " + str(row[4]) + "| Fever: " + str(row[5]) +
                            "| Next Visit: " + str(row[6]) + "| OPD ID: " + str(row[7]) + "| Problem: " + str(row[8]) +
                            "| Amount: " + str(row[9]) + "\n")

        mycursor.close()
        mydb.close()
        root.mainloop()
    def my_profile(self):
        print("hello3")
    def widget(self):
        self.menu_frame = Frame(self.master, padx=5, pady=5)
        self.menu_frame.grid()
        title1 = Label(self.menu_frame, text=" Doctor's HomePage ", font=('bold', 30))
        title1.grid(row=0, column=2)
        take_apponitment = Button(self.menu_frame, text=" Take Appointment ", font=('bold', 20), command=self.take_appointment)
        take_apponitment.grid(row=1, column=1, pady=100, ipadx=50)
        view_all_appointment = Button(self.menu_frame, text=" View All Appointments ", font=('bold', 20), command=self.view_all_appointment)
        view_all_appointment.grid(row=1, column=2, pady=100, ipadx=50)
        my_profile = Button(self.menu_frame, text=" My Profile ", font=('bold', 20), command=self.my_profile)
        my_profile.grid(row=1, column=3, pady=100, ipadx=50)

if __name__ == '__main__':
    window = Tk()
    opd_id = 47
    doctor(window,opd_id)
    window.mainloop()