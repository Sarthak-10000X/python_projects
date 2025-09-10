# Creating a digital clock!
import tkinter as tk 
from datetime import datetime
 
app=tk.Tk()
app.title("DIGITAL CLOCK")
app.resizable(False , False)
app.geometry("500x500")
app.configure(bg="black")

clock_label= tk.Label( bg="black", fg="white", font=("Aerial", 40), relief='flat')
clock_label.place(x=20,y=20)

def update_time():
   now=datetime.now()
   current_date= now.strftime("%d-%m-%Y")
   current_time=now.strftime("%H : %M : %S")
   clock_label.config(text=f"{current_time}\n{current_date}")
   clock_label.after(1000, update_time)

update_time()
app.mainloop()