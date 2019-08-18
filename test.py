import mysql.connector
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkcalendar import Calendar,DateEntry
from tkinter import messagebox
root = Tk()
def dateentry_view():
        def print_sel():
            print(cal.get_date())
        top = Toplevel(root)
        ttk.Label(top, text="choose").pack()
        cal = DateEntry(top, width=12, background="darkblue",foreground="white",borderwidth=2)
        cal.pack()
        ttk.Button(top, text="ok",command=print_sel).pack()

ttk.Button(root, text="dateentry",command=dateentry_view).pack()


root.mainloop()
