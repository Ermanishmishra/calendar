from tkinter import *
from tkcalendar import*


root =Tk()
root.title('Codemy.com')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x400")
root.configure(bg="lightblue")

cal=Calendar(root,selectmode="day",year=2020,month=5,day=22)
cal.pack(pady=20,fill="both",expand=True)


def grab_date():
    my_label.config(text="Today is date"+ cal.get_date())
my_button=Button(root,text="today date",command=grab_date)
my_button.pack(pady=20)

my_label=Label(root,text="")
my_label.pack(pady=20)
root.mainloop()