import mysql.connector
import datetime
from tkinter import *
from tkinter import messagebox
#root = Tk()
#t = Text(root,height=10, width=30)
#t.pack()
#x = datetime.datetime.now().strftime("%I:%M %p , %d-%b-%Y")
#mydb = mysql.connector.connect(host="localhost",user="root",passwd="mohit")
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE IF NOT EXISTS sysytem")
#mycursor.execute("USE sysytem")
#mycursor.execute("CREATE TABLE IF NOT EXISTS paa (paitent_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
 #                "paitent_name VARCHAR(50),date_of_visit VARCHAR(55),weight VARCHAR(10),fever VARCHAR(10),"
  #               "next_visit VARCHAR(55),opd_id VARCHAR(10),problem VARCHAR(10000))")
#mycursor.execute("INSERT INTO paa(paitent_name,date_of_visit,weight,fever,opd_id)VALUES(%s,%s,%s,%s,%s)",('mohit',x,'68kg','102C','5'))
#mydb.commit()
mydb = mysql.connector.connect(host="localhost",database="sysytem",user="root",passwd="mohit")
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM paa WHERE paitent_id = %s",("2",))
#root.mainloop()
mydb.commit()
mycursor.close()
mydb.close()
print("deleted")