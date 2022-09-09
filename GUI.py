from tkinter import *
import pyautogui

def process():
    name= b.get()
    passwd = c.get()
    a  = d.get()
    print(name)
    print(passwd)
    print(a)
    if a ==1:
        pyautogui.alert(name+passwd, "login")
    else:
        pyautogui.alert("error")


# button label checkbox text wqidget 
window = Tk()
window.title("Class")
a = PhotoImage(file='insta.png')
window.iconphoto(False,a)
window.geometry("600x400")
window.config(bg="#404e91")

Label(window,text="Welcome to Screen",
        bg="#404e91",
        fg="white",
        font=("Algerian",21)).grid(row=0,columnspan=2,column=1)
Label(window,bg="#404e91").grid(row=1,column=0)
Label(window,text="Name: ",
        bg="#404e91",
        fg="white",
        font=("Times New Roman",15)).grid(row=2,column=0)
Label(window,bg="#404e91").grid(row=3,column=0)
Label(window,text="Password: ",
        bg="#404e91",
        fg="white",
        font=("Times New Roman",15)).grid(row=4,column=0)
b = StringVar()
c = StringVar()

Entry(window,textvariable=b,font=("Times New Roman",15)).grid(row=2,column=1)
Entry(window,textvariable=c,font=("Times New Roman",15),show="*").grid(row=4,column=1)
d = IntVar()
Label(window,bg="#404e91").grid(row=5,column=0)
Checkbutton(window,text="Agree the condition",bg="#404e91",fg="white",font=("Times New Roman",15),variable=d).grid(row=6,column=0)
Label(window,bg="#404e91").grid(row=7,column=0)
Button(window,text="login",bg="#000000",fg="white",font=("Broadway",20),command=process).grid(row=8,column=1)





window.mainloop()