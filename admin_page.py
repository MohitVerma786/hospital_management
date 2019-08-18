from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog
from PIL import Image,ImageTk
from tkcalendar import Calendar,DateEntry
import mysql.connector
class staff():

    def __init__(self,master):
        self.master = master

        self.master.resizable(0,0)
        self.master.geometry('1080x540+260+140')
        self.master.title("Staff Member Info")
        self.master.configure(background="#d9d9d9")


        self.widgets()

    def widgets(self):

        font15 = "-family Arial -size 12 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"
        font16 = "-family Arial -size 18 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"
        font9 = "-family Arial -size 20 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"

        self.Label1 = Label(self.master)
        self.Label1.place(relx=0.0, rely=0.018, height=51, width=284)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Staff Member Info''')
        self.Label1.configure(width=284)

        self.TSeparator1 = ttk.Separator(self.master)
        self.TSeparator1.place(relx=0.037, rely=0.107, relwidth=0.935)

        self.name = Label(self.master)
        self.name.place(relx=0.046, rely=0.179, height=31, width=84)
        self.name.configure(background="#d9d9d9")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font=font15)
        self.name.configure(foreground="#000000")
        self.name.configure(text='''Name :''')
        self.name.configure(width=84)

        self.name_entry = Entry(self.master)
        self.name_entry.place(relx=0.176, rely=0.196, height=20, relwidth=0.152)
        self.name_entry.configure(background="white")
        self.name_entry.configure(disabledforeground="#a3a3a3")
        self.name_entry.configure(font="TkFixedFont")
        self.name_entry.configure(foreground="#000000")
        self.name_entry.configure(insertbackground="black")

        self.gender = Label(self.master)
        self.gender.place(relx=0.046, rely=0.304, height=31, width=84)
        self.gender.configure(activebackground="#f9f9f9")
        self.gender.configure(activeforeground="black")
        self.gender.configure(background="#d9d9d9")
        self.gender.configure(disabledforeground="#a3a3a3")
        self.gender.configure(font=font15)
        self.gender.configure(foreground="#000000")
        self.gender.configure(highlightbackground="#d9d9d9")
        self.gender.configure(highlightcolor="black")
        self.gender.configure(text='''Gender :''')
        self.gender.configure(width=84)

        self.gender_v = StringVar()
        self.gender_rm = Radiobutton(self.master, value="Male", variable=self.gender_v, text="Male", bg='#d9d9d9',
                                  activebackground='#d9d9d9').place(relx=0.176, rely=0.313,
                                                                    relheight=0.045, relwidth=0.05)
        self.gender_rf = Radiobutton(self.master, value="Female", variable=self.gender_v, text="Female", bg='#d9d9d9',
                                  activebackground='#d9d9d9').place(relx=0.241, rely=0.313,
                                                                    relheight=0.045, relwidth=0.05)

        self.dob = Label(self.master)
        self.dob.place(relx=0.046, rely=0.571, height=31, width=84)
        self.dob.configure(activebackground="#f9f9f9")
        self.dob.configure(activeforeground="black")
        self.dob.configure(background="#d9d9d9")
        self.dob.configure(disabledforeground="#a3a3a3")
        self.dob.configure(font=font15)
        self.dob.configure(foreground="#000000")
        self.dob.configure(highlightbackground="#d9d9d9")
        self.dob.configure(highlightcolor="black")
        self.dob.configure(text='''D.O.B :''')
        self.dob.configure(width=84)


        self.dob_e = DateEntry(self.master, background='grey', foreground='white', borderwidth=2)
        self.dob_e.place(relx=0.176, rely=0.580, height=20, width=120)

        self.marital_status = Label(self.master)
        self.marital_status.place(relx=0.046, rely=0.429, height=31, width=134)
        self.marital_status.configure(activebackground="#f9f9f9")
        self.marital_status.configure(activeforeground="black")
        self.marital_status.configure(background="#d9d9d9")
        self.marital_status.configure(disabledforeground="#a3a3a3")
        self.marital_status.configure(font=font15)
        self.marital_status.configure(foreground="#000000")
        self.marital_status.configure(highlightbackground="#d9d9d9")
        self.marital_status.configure(highlightcolor="black")
        self.marital_status.configure(text='''Marital Status :''')
        self.marital_status.configure(width=134)

        self.marital_combobox = ttk.Combobox(self.master, values=["Single", "Married", "Divorced"])
        self.marital_combobox.current(0)
        self.marital_combobox.place(relx=0.176, rely=0.444, height=20, relwidth=0.152)

        self.Member_id = Label(self.master)
        self.Member_id.place(relx=0.417, rely=0.179, height=31, width=121)
        self.Member_id.configure(activebackground="#f9f9f9")
        self.Member_id.configure(activeforeground="black")
        self.Member_id.configure(background="#d9d9d9")
        self.Member_id.configure(disabledforeground="#a3a3a3")
        self.Member_id.configure(font=font15)
        self.Member_id.configure(foreground="#000000")
        self.Member_id.configure(highlightbackground="#d9d9d9")
        self.Member_id.configure(highlightcolor="black")
        self.Member_id.configure(text='''Staff ID :''')
        self.Member_id.configure(width=121)

        self.phone_number = Label(self.master)
        self.phone_number.place(relx=0.417, rely=0.304, height=36, width=134)
        self.phone_number.configure(activebackground="#f9f9f9")
        self.phone_number.configure(activeforeground="black")
        self.phone_number.configure(background="#d9d9d9")
        self.phone_number.configure(disabledforeground="#a3a3a3")
        self.phone_number.configure(font=font15)
        self.phone_number.configure(foreground="#000000")
        self.phone_number.configure(highlightbackground="#d9d9d9")
        self.phone_number.configure(highlightcolor="black")
        self.phone_number.configure(text='''Phone Number :''')
        self.phone_number.configure(width=134)

        self.adhaar_number = Label(self.master)
        self.adhaar_number.place(relx=0.407, rely=0.429, height=36, width=154)
        self.adhaar_number.configure(activebackground="#f9f9f9")
        self.adhaar_number.configure(activeforeground="black")
        self.adhaar_number.configure(background="#d9d9d9")
        self.adhaar_number.configure(disabledforeground="#a3a3a3")
        self.adhaar_number.configure(font=font15)
        self.adhaar_number.configure(foreground="#000000")
        self.adhaar_number.configure(highlightbackground="#d9d9d9")
        self.adhaar_number.configure(highlightcolor="black")
        self.adhaar_number.configure(text='''Adhaar Number :''')
        self.adhaar_number.configure(width=154)

        self.address = Label(self.master)
        self.address.place(relx=0.407, rely=0.571, height=36, width=184)
        self.address.configure(activebackground="#f9f9f9")
        self.address.configure(activeforeground="black")
        self.address.configure(background="#d9d9d9")
        self.address.configure(disabledforeground="#a3a3a3")
        self.address.configure(font=font15)
        self.address.configure(foreground="#000000")
        self.address.configure(highlightbackground="#d9d9d9")
        self.address.configure(highlightcolor="black")
        self.address.configure(text='''Permanent Address :''')
        self.address.configure(width=184)

        self.ph_number_entry = Entry(self.master)
        self.ph_number_entry.place(relx=0.611, rely=0.321, height=20
                                   , relwidth=0.152)
        self.ph_number_entry.configure(background="white")
        self.ph_number_entry.configure(disabledforeground="#a3a3a3")
        self.ph_number_entry.configure(font="TkFixedFont")
        self.ph_number_entry.configure(foreground="#000000")
        self.ph_number_entry.configure(highlightbackground="#d9d9d9")
        self.ph_number_entry.configure(highlightcolor="black")
        self.ph_number_entry.configure(insertbackground="black")
        self.ph_number_entry.configure(selectbackground="#c4c4c4")
        self.ph_number_entry.configure(selectforeground="black")

        self.adhaar_entry = Entry(self.master)
        self.adhaar_entry.place(relx=0.611, rely=0.446, height=20, relwidth=0.152)
        self.adhaar_entry.configure(background="white")
        self.adhaar_entry.configure(disabledforeground="#a3a3a3")
        self.adhaar_entry.configure(font="TkFixedFont")
        self.adhaar_entry.configure(foreground="#000000")
        self.adhaar_entry.configure(highlightbackground="#d9d9d9")
        self.adhaar_entry.configure(highlightcolor="black")
        self.adhaar_entry.configure(insertbackground="black")
        self.adhaar_entry.configure(selectbackground="#c4c4c4")
        self.adhaar_entry.configure(selectforeground="black")

        self.TSeparator2 = ttk.Separator(self.master)
        self.TSeparator2.place(relx=0.037, rely=0.768, relwidth=0.935)

        self.staff_id_entry = Entry(self.master)
        self.staff_id_entry.place(relx=0.611, rely=0.196, height=20, relwidth=0.152)
        self.staff_id_entry.configure(background="white")
        self.staff_id_entry.configure(disabledforeground="#a3a3a3")
        self.staff_id_entry.configure(font="TkFixedFont")
        self.staff_id_entry.configure(foreground="#000000")
        self.staff_id_entry.configure(highlightbackground="#d9d9d9")
        self.staff_id_entry.configure(highlightcolor="black")
        self.staff_id_entry.configure(insertbackground="black")
        self.staff_id_entry.configure(selectbackground="#c4c4c4")
        self.staff_id_entry.configure(selectforeground="black")
        #self.staff_id_entry.insert(END,"Auto Assigned")

        self.search_button = Button(self.master)
        self.search_button.place(relx=0.157, rely=0.786, height=34, width=107)
        self.search_button.configure(activebackground="#ececec")
        self.search_button.configure(activeforeground="#000000")
        self.search_button.configure(background="#d9d9d9")
        self.search_button.configure(disabledforeground="#a3a3a3")
        self.search_button.configure(font=font16)
        self.search_button.configure(foreground="#000000")
        self.search_button.configure(highlightbackground="#d9d9d9")
        self.search_button.configure(highlightcolor="black")
        self.search_button.configure(pady="0")
        self.search_button.configure(text='''Search''')
        self.search_button.configure(width=107)
        self.search_button.configure(command=self.search)

        self.addnew_button = Button(self.master)
        self.addnew_button.place(relx=0.046, rely=0.786, height=34, width=117)
        self.addnew_button.configure(activebackground="#ececec")
        self.addnew_button.configure(activeforeground="#000000")
        self.addnew_button.configure(background="#d9d9d9")
        self.addnew_button.configure(disabledforeground="#a3a3a3")
        self.addnew_button.configure(font=font16)
        self.addnew_button.configure(foreground="#000000")
        self.addnew_button.configure(highlightbackground="#d9d9d9")
        self.addnew_button.configure(highlightcolor="black")
        self.addnew_button.configure(pady="0")
        self.addnew_button.configure(text='''Add New''')
        self.addnew_button.configure(width=117)
        self.addnew_button.configure(command=self.addnew)

        self.update_button = Button(self.master)
        self.update_button.place(relx=0.259, rely=0.786, height=34, width=107)
        self.update_button.configure(activebackground="#ececec")
        self.update_button.configure(activeforeground="#000000")
        self.update_button.configure(background="#d9d9d9")
        self.update_button.configure(disabledforeground="#a3a3a3")
        self.update_button.configure(font=font16)
        self.update_button.configure(foreground="#000000")
        self.update_button.configure(highlightbackground="#d9d9d9")
        self.update_button.configure(highlightcolor="black")
        self.update_button.configure(pady="0")
        self.update_button.configure(text='''Update''')

        self.delete_button = Button(self.master)
        self.delete_button.place(relx=0.361, rely=0.786, height=34, width=107)
        self.delete_button.configure(activebackground="#ececec")
        self.delete_button.configure(activeforeground="#000000")
        self.delete_button.configure(background="#d9d9d9")
        self.delete_button.configure(disabledforeground="#a3a3a3")
        self.delete_button.configure(font=font16)
        self.delete_button.configure(foreground="#000000")
        self.delete_button.configure(highlightbackground="#d9d9d9")
        self.delete_button.configure(highlightcolor="black")
        self.delete_button.configure(pady="0")
        self.delete_button.configure(text='''Delete''')

        self.scroll_frame = Frame(self.master, bg="red")
        self.scroll_frame.place(relx=0.611, rely=0.571, height=35, relwidth=0.152)
        self.scrollbar = Scrollbar(self.scroll_frame, orient="horizontal")
        self.scrolled_entry = Entry(self.scroll_frame, xscrollcommand=self.scrollbar.set)
        self.scrolled_entry.focus()
        self.scrolled_entry.pack(side="top", fill="x")
        self.scrollbar.pack(fill="x")
        self.scrollbar.config(command=self.scrolled_entry.xview)
        self.scrolled_entry.config()

    def addnew(self):

        if(str(self.name_entry.get())!="" and
           str(self.gender_v.get())!="" and
           str(self.dob_e.get_date())!="" and
           str(self.ph_number_entry.get())!="" and
           str(self.adhaar_entry.get())!="" and
           str(self.scrolled_entry.get())!=""):
            self.password = simpledialog.askstring("Enter Password", "Enter a Password For This New Staff Member",
                                                   parent=self.master)

            if (self.password == ""):
                messagebox.showerror("Password Must", "Password Can't be Empty")
                self.addnew()

            else:
                try:
                    mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
                    try:
                        mycursor = mydb.cursor()
                        mycursor.execute("CREATE DATABASE IF NOT EXISTS staff")
                        mycursor.execute("USE staff")
                        mycursor.execute(
                            "CREATE TABLE IF NOT EXISTS staff_member_record (staff_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),"
                            "gender VARCHAR(10),date_of_birth VARCHAR(20),"
                            "marital_status VARCHAR(15),phone_number VARCHAR(16),adhaar_number VARCHAR(20),permanent_address VARCHAR(200),password VARCHAR(50))")

                        mycursor.execute(
                            "INSERT INTO staff_member_record(name,gender,date_of_birth,marital_status,"
                            "phone_number,adhaar_number,permanent_address,password)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (str(self.name_entry.get()),
                             str(self.gender_v.get()),
                             str(self.dob_e.get_date()),
                             str(self.marital_combobox.get()),
                             str(self.ph_number_entry.get()),
                             str(self.adhaar_entry.get()),
                             str(self.scrolled_entry.get()),
                             str(self.password),
                             ))

                        mycursor.close()
                        mydb.commit()
                        messagebox.showinfo("Succed", "Table Has Been Succesfully Created")
                    except Exception as ex:
                        messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
                    finally:
                        mydb.close()

                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))
        else:
            messagebox.showerror("Error Occured", "Please Fill All The Fields")
            self.master.deiconify()


    def search(self):


        if(True):
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
                try:

                    mycursor = mydb.cursor()
                    mycursor.execute("USE staff")
                    mycursor.execute("SELECT * FROM staff_member_record WHERE staff_id = %s", (str(self.staff_id_entry.get()),))
                    record = mycursor.fetchall()

                    for row in record:
                        print(row[1],row[2],row[3],row[4],row[5])
                        self.staff_id_entry.delete(0, END)
                        self.staff_id_entry.insert(END,str(row[0]))
                        self.name_entry.delete(0, END)
                        self.name_entry.insert(END, str(row[1]))
                        if(str(row[2]) == "Male"):
                            self.gender_v.set("Male")
                        elif(str(row[2]) == "Female"):
                            self.gender_v.set("Female")
                        self.dob_e.delete(0, END)
                        self.dob_e.insert(END,str(row[3]))
                        self.marital_combobox.delete(0, END)
                        self.marital_combobox.insert(END, str(row[4]))
                        self.ph_number_entry.delete(0, END)
                        self.ph_number_entry.insert(END, str(row[5]))
                        self.adhaar_entry.delete(0, END)
                        self.adhaar_entry.insert(END, str(row[6]))
                        self.scrolled_entry.delete(0, END)
                        self.scrolled_entry.insert(END, str(row[7]))

                    mycursor.close()
                    mydb.commit()
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
                finally:
                    mydb.close()

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

# main Class
class main:
    def __init__(self, master):

        self.master = master
        master.state("zoomed")

        self.master.title("ADMIN ACCOUNT")

        self.widgets()

    # Login Function

    def staff(self):

        window = Toplevel(self.master)
        obj = staff(window)

        window.mainloop()

    def widgets(self):
        self.logf = Frame(self.master, bg='#c5cde0', padx=10, pady=10)
        self.logf.place(height=1000, width=1500)
        pic0 = Image.open('images/admin.png')
        pic0 = pic0.resize((100, 100), Image.ANTIALIAS)
        self.pic0 = ImageTk.PhotoImage(pic0)
        self.head_image = Label(self.logf, image=self.pic0, bg='#c5cde0').place(x=90, y=0)
        self.head_label = Label(self.logf, bg='#c5cde0', text="ADMIN ACCOUNT", font=('',25,'bold')).place(x=200, y=35)
        self.TSeparator1 = ttk.Separator(self.logf)
        self.TSeparator1.configure(orient="vertical")
        self.TSeparator1.place(x=250, y=120, height=550)
        pic1 = Image.open('images/staff.png')
        pic1 = pic1.resize((150, 150), Image.ANTIALIAS)
        self.pic1 = ImageTk.PhotoImage(pic1)
        self.staff_image = Button(self.logf, image=self.pic1, bg='#c5cde0', relief='groove',
                                  activebackground='#c5cde0', command=self.staff).place(x=50, y=140)
        self.staff_label = Button(self.logf, bg='#c5cde0', text="STAFF", font=('', 15, 'bold'), relief='groove',
                                 activebackground='#c5cde0', command=self.staff).place(x=87, y=295)
        pic2 = Image.open('images/doctor.png')
        pic2 = pic2.resize((150, 150), Image.ANTIALIAS)
        self.pic2 = ImageTk.PhotoImage(pic2)
        self.doctor_image = Button(self.logf, image=self.pic2, bg='#c5cde0', relief='groove', activebackground='#c5cde0')
        self.doctor_image.place(x=50, y=380)
        self.doctor_label = Button(self.logf, bg='#c5cde0', text="DOCTOR", font=('', 15, 'bold'), relief='groove',
                                 activebackground='#c5cde0').place(x=75, y=535)
        self.TSeparator2 = ttk.Separator(self.logf)
        self.TSeparator2.configure(orient="horizontal")
        self.TSeparator2.place(x=300, y=100, width=1000)




if __name__ == '__main__':
    window = Tk()
    obj = main(window)

    window.mainloop()