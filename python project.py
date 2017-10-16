import tkinter as tk

FONT_TYPE=('Times New Roman', 12)

class POSSystem(tk.Tk):

    def __init__(self, *args, **kwargs): ##this is the initializer, auto starts when program runs

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0, weight =1)##first number is the size, weight is priority
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}##dict of frames to house all the windows in the program
        for F in (LoginPage, PageAfterLogin): #F being the current frame
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

def printText(inside):
    print(inside)

class LoginPage(tk.Frame):##login page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome, enter your employee number to login!",font=FONT_TYPE)##this just shows text, not a button or anything
        label.pack(pady=10,padx=10)

        button1 =   tk.Button(self, text="1", command=lambda: printText("1"))
        button1.pack()
        button2 =   tk.Button(self, text="2", command=lambda: printText("2"))
        button2.pack()
        button3 =   tk.Button(self, text="3", command=lambda: printText("3"))
        button3.pack()
        button4 =   tk.Button(self, text="4", command=lambda: printText("4"))
        button4.pack()
        button5 =   tk.Button(self, text="5", command=lambda: printText("5"))
        button5.pack()
        button6 =   tk.Button(self, text="6", command=lambda: printText("6"))
        button6.pack()
        button7 =   tk.Button(self, text="7", command=lambda: printText("7"))
        button7.pack()
        button8 =   tk.Button(self, text="8", command=lambda: printText("8"))
        button8.pack()
        button9 =   tk.Button(self, text="9", command=lambda: printText("9"))
        button9.pack()
        button0 =   tk.Button(self, text="0", command=lambda: printText("0"))
        button0.pack()
        buttonLogin =   tk.Button(self, text="Log In", command=lambda: controller.show_frame(PageAfterLogin))#Will return a different response based on whether login worked later
        buttonLogin.pack()
        
class PageAfterLogin(tk.Frame):#placeholder name
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Placeholder Text",font=FONT_TYPE)
        label.pack(pady=10,padx=10)

        buttonBack = tk.Button(self, text ="Return to Log In Screen", command = lambda: controller.show_frame(LoginPage))
        buttonBack.pack()
app=POSSystem()
app.mainloop()
