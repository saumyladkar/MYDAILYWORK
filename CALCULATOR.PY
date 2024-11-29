from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("312x394")

root.title("Calculator")



def about():
    messagebox.showinfo('About',
                        " \n Created by Saumy ladkar \n \n  linkedin :\n  www.linkedin.com/in/saumy-ladkar-a3a517277")


def click_b(item):
    global expression
    inputText.set(inputText.get() + (str(item)))


def clear_b():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])


def clear_all():
    inputText.set("")


def equal_b():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "_ERROR_"
        inputText.set(result)



menubar = Menu( bg="black", fg="grey")

filemenu = Menu(menubar, tearoff=0, bg="black", fg="white")
filemenu.add_command(label="Cut", accelerator="Ctrl+X")
filemenu.add_command(label="Copy", accelerator="Ctrl+C")
filemenu.add_command(label="Paste", accelerator="Ctrl+V")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0, bg="black", fg="white")
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

root.config(bg="grey", menu=menubar)

expression = ""
inputText = StringVar()
inputFrame = Frame( width=312, height=50, bd=0, highlightbackground="black", highlightcolor="crimson",
                   highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 17), textvariable=inputText, width=50, fg="white", bg="black", bd=0,
                   justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=19)


frame = Frame( width=312, height=272.5, bg="grey")
frame.pack()

"----------------------------------------- 1st row -----------------------------------------------"

clearall = Button(frame, text="C", fg="white", width=10, height=3, bd=0, bg="black",
                  command=lambda: clear_all()).grid(row=1, column=0, padx=1, pady=1)
l_bracket = Button(frame, text="(", fg="white", width=10, height=3, bd=0, bg="black",
                   command=lambda: click_b("(")).grid(row=1, column=1, padx=1, pady=1)
r_bracket = Button(frame, text=")", fg="white", width=10, height=3, bd=0, bg="black",
                   command=lambda: click_b(")")).grid(row=1, column=2, padx=1, pady=1)
clear = Button(frame, text="<", fg="white", width=10, height=3, bd=0, bg="black",
               command=lambda: clear_b()).grid(row=1, column=3, padx=1, pady=1)

"----------------------------------------- 2nd  row -----------------------------------------------"

power = Button(frame, text="^", fg="white", width=10, height=3, bd=0, bg="black",
               command=lambda: click_b("**")).grid(row=2, column=0, padx=1, pady=1)
pie = Button(frame, text="π", fg="white", width=10, height=3, bd=0, bg="black",
             command=lambda: click_b(3.1415)).grid(row=2, column=1, padx=1, pady=1)
exp = Button(frame, text="e", fg="white", width=10, height=3, bd=0, bg="black",
             command=lambda: click_b(2.7182)).grid(row=2, column=2, padx=1, pady=1)
divide_ = Button(frame, text="/", fg="white", width=10, height=3, bd=0, bg="black",
                 command=lambda: click_b("/")).grid(row=2, column=3, padx=1, pady=1)

"----------------------------------------- 3rd row -----------------------------------------------"


seven = Button(frame, text="7", fg="white", width=10, height=3, bd=0, bg="#121212",
               command=lambda: click_b(7)).grid(row=3, column=0, padx=1, pady=1)
eight = Button(frame, text="8", fg="white", width=10, height=3, bd=0, bg="#121212",
               command=lambda: click_b(8)).grid(row=3, column=1, padx=1, pady=1)
nine = Button(frame, text="9", fg="white", width=10, height=3, bd=0, bg="#121212",
              command=lambda: click_b(9)).grid(row=3, column=2, padx=1, pady=1)
multiply = Button(frame, text="x", fg="white", width=10, height=3, bd=0, bg="black",
                  command=lambda: click_b("*")).grid(row=3, column=3, padx=1, pady=1)

"----------------------------------------- 4th row -----------------------------------------------"



four = Button(frame, text = "4", fg = "white", width = 10, height = 3, bd = 0, bg = "#121212", command = lambda: click_b(4)).grid(row = 4, column = 0, padx = 1, pady = 1)
five = Button(frame, text="5", fg="white", width=10, height=3, bd=0, bg="#121212",
              command=lambda: click_b(5)).grid(row=4, column=1, padx=1, pady=1)
six = Button(frame, text="6", fg="white", width=10, height=3, bd=0, bg="#121212",
             command=lambda: click_b(6)).grid(row=4, column=2, padx=1, pady=1)
minus = Button(frame, text="-", fg="white", width=10, height=3, bd=0, bg="black",
               command=lambda: click_b("-")).grid(row=4, column=3, padx=1, pady=1)


"----------------------------------------- 5th row -----------------------------------------------"


one = Button(frame, text="1", fg="white", width=10, height=3, bd=0, bg="#121212",
             command=lambda: click_b(1)).grid(row=5, column=0, padx=1, pady=1)
two = Button(frame, text="2", fg="white", width=10, height=3, bd=0, bg="#121212",
             command=lambda: click_b(2)).grid(row=5, column=1, padx=1, pady=1)
three = Button(frame, text="3", fg="white", width=10, height=3, bd=0, bg="#121212",
               command=lambda: click_b(3)).grid(row=5, column=2, padx=1, pady=1)
plus = Button(frame, text="+", fg="white", width=10, height=3, bd=0, bg="black",
              command=lambda: click_b("+")).grid(row=5, column=3, padx=1, pady=1)


"----------------------------------------- 6th row -----------------------------------------------"


point = Button(frame, text=".", fg="white", width=10, height=3, bd=0, bg="black",
               command=lambda: click_b(".")).grid(row=6, column=0, padx=1, pady=1)
zero = Button(frame, text="0", fg="white", width=10, height=3, bd=0, bg="#121212",
              command=lambda: click_b(0)).grid(row=6, column=1, padx=1, pady=1)
equals = Button(frame, text="=", fg="crimson", width=21, height=3, bd=0, bg="black",
                command=lambda: equal_b()).grid(row=6, column=2, columnspan=2, padx=1, pady=1)

mainloop()
