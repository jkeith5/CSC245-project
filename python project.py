import tkinter as tk
from tkinter import *

FONT_TYPE=('Times New Roman', 12)
validLogin1= '524951'
validLogin2= '785412'
validLogin3= '225485'
cache = list()
cache2=list()
tableNumber=''
login = ''


class POSSystem(tk.Tk):

    def __init__(self, *args, **kwargs): ##this is the initializer, auto starts when program runs

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0, weight =1)##first number is the size, weight is priority
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}##dict of frames to house all the windows in the program
        for F in (LoginPage, PageAfterLogin, TabCreatePage): #F being the current frame
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)


        

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

class LoginPage(tk.Frame):##login page
    global cache,login,validLogin1,validLogin2,validLogin3
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome, enter your employee number to login!",font=FONT_TYPE)##this just shows text, not a button or anything
        label.grid(row=0, columnspan = 5, pady=10,padx=10)
        button1 =   tk.Button(self, text="1", command=lambda: verifyLogin(1))
        button1.grid(row=1, column=0)
        button2 =   tk.Button(self, text="2", command=lambda: verifyLogin(2))
        button2.grid(row=1, column=1)
        button3 =   tk.Button(self, text="3", command=lambda: verifyLogin(3))
        button3.grid(row=1,column=2)
        button4 =   tk.Button(self, text="4", command=lambda: verifyLogin(4))
        button4.grid(row=2,column=0)
        button5 =   tk.Button(self, text="5", command=lambda: verifyLogin(5))
        button5.grid(row=2, column=1)
        button6 =   tk.Button(self, text="6", command=lambda: verifyLogin(6))
        button6.grid(row=2, column=2)
        button7 =   tk.Button(self, text="7", command=lambda: verifyLogin(7))
        button7.grid(row=3,column=0)
        button8 =   tk.Button(self, text="8", command=lambda: verifyLogin(8))
        button8.grid(row=3,column=1)
        button9 =   tk.Button(self, text="9", command=lambda: verifyLogin(9))
        button9.grid(row=3,column=2)
        button0 =   tk.Button(self, text="0", command=lambda: verifyLogin(0))
        button0.grid(row=4,column=1)
        buttonClear= tk.Button(self, text="Clear", command= lambda:verifyLogin("Clear"))
        buttonClear.grid(row=4,column=0)
        buttonLogin =   tk.Button(self, text="Log In", command=lambda:verifyLogin("Login"))#Will return a different response based on whether login worked later
        buttonLogin.grid(row=4,column=2)
        def verifyLogin(argument):
            global cache
            global login
            global validLogin1,validLogin2,validLogin3
            if isinstance(argument, int):
                cache.append(str(argument))
                if len(cache)==6:
                    login=''.join(cache)
            elif isinstance(argument,str):
                if argument == 'Login':
                    if (login == validLogin1 or login== validLogin2 or login==validLogin3):
                        controller.show_frame(PageAfterLogin)
                    else:
                        root = Tk()
                        login=0
                        cache=[]
                        Errorbox = Text(root,height=2,width=30)
                        Errorbox.pack()
                        Errorbox.insert(END, "Incorrect login information, try again.")
                        controller.show_frame(LoginPage)
                        mainloop()
                elif argument == 'Clear':
                    login=0
                    cache=[]
                
        
class PageAfterLogin(tk.Frame):#Table Select Screen/Frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Create a new table!",font=FONT_TYPE)
        label.grid(row=0, columnspan=2, pady=5, padx=10)
        buttonBack = tk.Button(self, text ="Return to Log In Screen", command = lambda: self.NumberDelete(controller))
        buttonBack.grid(row=1,column=1)
        buttonTable = tk.Button(self,text ="Create new table", command = lambda: controller.show_frame(TabCreatePage))
        buttonTable.grid(row=1,column=2)
        
    def NumberDelete(self, controller):
        global cache, login
        cache = 0
        login = 0
        controller.show_frame(LoginPage)

class TabCreatePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        buttons = ButtonFrame(self,controller)
        buttons.grid(row=1)
        label = tk.Label(self,text="Select a Table Number",font=FONT_TYPE)
        label.grid(row=0,columnspan=200)

class ButtonFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        button1 =   tk.Button(self, text="1", command=lambda: constructSingleLine(1))
        button1.grid(row=1, column=0)
        button2 =   tk.Button(self, text="2", command=lambda: constructSingleLine(2))
        button2.grid(row=1, column=1)
        button3 =   tk.Button(self, text="3", command=lambda: constructSingleLine(3))
        button3.grid(row=1,column=2)
        button4 =   tk.Button(self, text="4", command=lambda: constructSingleLine(4))
        button4.grid(row=2,column=0)
        button5 =   tk.Button(self, text="5", command=lambda: constructSingleLine(5))
        button5.grid(row=2, column=1)
        button6 =   tk.Button(self, text="6", command=lambda: constructSingleLine(6))
        button6.grid(row=2, column=2)
        button7 =   tk.Button(self, text="7", command=lambda: constructSingleLine(7))
        button7.grid(row=3,column=0)
        button8 =   tk.Button(self, text="8", command=lambda: constructSingleLine(8))
        button8.grid(row=3,column=1)
        button9 =   tk.Button(self, text="9", command=lambda: constructSingleLine(9))
        button9.grid(row=3,column=2)
        button0 =   tk.Button(self, text="0", command=lambda: constructSingleLine(0))
        button0.grid(row=4,column=1)
        buttonClear = tk.Button(self,text="Clear", command = lambda: constructSingleLine("clear"))
        buttonClear.grid(row=4,column=0)
        buttonDone=tk.Button(self,text="Enter",command = lambda: constructSingleLine("done"))
        buttonDone.grid(row=4,column=2)

        def constructSingleLine(argument):
            global cache2
            global tableNumber
            if isinstance(argument,int):
                cache2.append(str(argument))
                if len(cache2)==2:
                    tableNumber=''.join(cache2)
            elif isinstance(argument,str):
                pass
            
class Table(tk.Frame):
    def __init__(self,parent,number,controller):
        contents = StringVar()
        pass
app=POSSystem()
app.mainloop()
