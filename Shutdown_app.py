from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def Log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /r /t 1")


st = Tk()
st.title("Shut_Down")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st,text="restart", font=("Time new roman",20,"bold"),
relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="restart time", font=("Time new roman",20,"bold"),
relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="Log-out", font=("Time new roman",20,"bold"),
relief=RAISED,cursor="plus",command=Log_out)
lg_button.place(x=150,y=270,height=50,width=200)

st_button = Button(st,text="Shut-Down", font=("Time new roman",20,"bold"),
relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)



st.mainloop()