import tkinter as tk
from tkinter import *

FONT_TYPE=('Times New Roman', 12)
validLogin1= '524951'
validLogin2= '785412'
validLogin3= '770894'
cache = list()
cache2=list()
tableNumber=''
login = ''
tableList=[None]*101
currentTable=0


class POSSystem(tk.Tk):

    def __init__(self, *args, **kwargs): ##this is the initializer, auto starts when program runs

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0, weight =1)##first number is the size, weight is priority
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}##dict of frames to house all the windows in the program
        for F in (LoginPage, PageAfterLogin, TabCreatePage, OrderPage, EntreeMenu, KidsMenu, DrinksMenu, SidesMenu, OrderSummary): #F being the current frame
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)


        

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
        
"""This class creates the login page and numbers in a grid to allow the user to enter their own employee number which is then validated to one of the three only working numbers"""
class LoginPage(tk.Frame):##login page
    global cache,login,validLogin1,validLogin2,validLogin3
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome, enter your employee number to login!",font=FONT_TYPE)##this just shows text, not a button or anything
        label.grid(row=0, columnspan = 5, pady=10,padx=10)
        button1 =   tk.Button(self, text="1", command=lambda: verifyLogin(1))
        button1.grid(sticky="nsew",row=1, column=1)
        button2 =   tk.Button(self, text="2", command=lambda: verifyLogin(2))
        button2.grid(sticky="nsew",row=1, column=2)
        button3 =   tk.Button(self, text="3", command=lambda: verifyLogin(3))
        button3.grid(sticky="nsew",row=1,column=3)
        button4 =   tk.Button(self, text="4", command=lambda: verifyLogin(4))
        button4.grid(sticky="nsew",row=2,column=1)
        button5 =   tk.Button(self, text="5", command=lambda: verifyLogin(5))
        button5.grid(sticky="nsew",row=2, column=2)
        button6 =   tk.Button(self, text="6", command=lambda: verifyLogin(6))
        button6.grid(sticky="nsew",row=2, column=3)
        button7 =   tk.Button(self, text="7", command=lambda: verifyLogin(7))
        button7.grid(sticky="nsew",row=3,column=1)
        button8 =   tk.Button(self, text="8", command=lambda: verifyLogin(8))
        button8.grid(sticky="nsew",row=3,column=2)
        button9 =   tk.Button(self, text="9", command=lambda: verifyLogin(9))
        button9.grid(sticky="nsew",row=3,column=3)
        button0 =   tk.Button(self, text="0", command=lambda: verifyLogin(0))
        button0.grid(sticky="nsew",row=4,column=2)
        buttonClear= tk.Button(self, text="Clear", command= lambda:verifyLogin("Clear"))
        buttonClear.grid(sticky="nsew",row=4,column=1)
        buttonLogin =   tk.Button(self, text="Log In", command=lambda:verifyLogin("Login"))#Will return a different response based on whether login worked later
        buttonLogin.grid(sticky="nsew",row=4,column=3)
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
                
"""This class creates the page after login where you are given the options to either logout or create a table"""
class PageAfterLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select",font=FONT_TYPE)
        label.grid(row=0, columnspan=2, pady=5, padx=10)
        buttonBack = tk.Button(self, text ="Logout", command = lambda: self.NumberDelete(controller))
        buttonBack.grid(row=11,column=1)
        buttonTable = tk.Button(self,text ="Create new table", command = lambda: controller.show_frame(TabCreatePage))
        buttonTable.grid(row=10,column=1)
        buttons=[]
        for table in tableList:
            if not table == None:
                result = table%5
                buttons[table]= tk.Button(self,text=str(table),command = lambda: None)
                buttons[table].grid(row=( 0 + result if not result == 0 else result),column= (result if not result == 0 else 0+result))
        
    def NumberDelete(self, controller):
        global cache, login
        cache = []
        login = 0
        controller.show_frame(LoginPage)
        
"""The table creation page prompts the user to enter the table number and creates a button to access the page"""
class TabCreatePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        labelContents= ''
        global tableNumber
        labelTabNumber =tk.Label(self, text = 'Number: ',font = FONT_TYPE)
        buttons = TableCreateFrame(self,controller)
        buttons.grid(row=1,rowspan=4, column=2)
        labelTabNumber.grid(row=1,column=1)
        labelNote= tk.Label(self,text='*Note: Table number cannot exceed 100*',font = FONT_TYPE)
        label = tk.Label(self,text="Select a Table Number",font=FONT_TYPE)
        label.grid(row=0,columnspan=3)
        
"""Creates the frame with buttons in a grid to let the user enter the table number"""
class TableCreateFrame(tk.Frame):
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

        def constructSingleLine(argument,):
            global cache2
            global tableNumber,tableList
            if isinstance(argument,int):
                cache2.append(str(argument))
                tableNumber=''.join(cache2)
                
            elif isinstance(argument,str):
                if argument == 'done':
                    try:
                        tableList[int(tableNumber)]=(Table(parent,controller = controller,number=tableNumber))#goes to Table class then to order screen from here
                        controller.show_frame(PageAfterLogin)
                        tableNumber=0
                        cache2=[]
                    except:
                        root = Tk()
                        cache=[]
                        Errorbox = Text(root,height=2,width=30)
                        Errorbox.pack()
                        Errorbox.insert(END, "Table number must be between 1-100.")
                        cache2=[]
                        tableNumber=0
                        mainloop()
                        
                        raise IndexError("Table number must be between 1-100.")
                elif argument == 'clear':
                    cache2=[]
                    tableNumber=0
                    controller.show_frame(TabCreatePage)

"""Creates a button that directs you to the specific table"""
class Table(tk.Button):
    def __init__(self,parent,controller,number):
        self.number= number
        if int(number) > 0 and int(number) < 101:
            global currentTable
            tk.Button.__init__(self,text=number,command=lambda: controller.show_frame(OrderPage))
            currentTable=int(number)
            self.pack()
        self._order= dict()
        self._price=0
        self._orderlist=''
    def addToOrder(self, plate):
        self._order.update(plate)
        print(str(plate.keys())[12:-3])
        self._orderlist+=str(plate.keys())[12:-3] + ', '
    def order(self,_order):
        return _order
    
"""Creates the buttons that allow for menu navigation to each of the respected menus"""
class OrderPage(tk.Frame):#Order Page after table is created
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        labelMenuTitle = tk.Label(self, text = 'Menu',font = FONT_TYPE)
        labelMenuTitle.grid(row=2,column=1)
        frame=''
        button1 = tk.Button(self, text='Entrees', command= lambda: controller.show_frame(EntreeMenu))#Path to appropriate menu
        button1.grid(row=3, column=1)
        button2 = tk.Button(self, text='Kids', command= lambda: controller.show_frame(KidsMenu))#Path to appropriate menu
        button2.grid(row=3, column=2)
        button3 = tk.Button(self, text='Sides', command= lambda: controller.show_frame(SidesMenu))#Path to appropriate menu
        button3.grid(row=3, column=3)
        button4 = tk.Button(self, text='Drinks', command= lambda: controller.show_frame(DrinksMenu))#Path to appropriate menu
        button4.grid(row=3, column=4)
        buttonBack = tk.Button(self, text ="Return", command = lambda: controller.show_frame(PageAfterLogin))
        buttonBack.grid(row=0,column=1)
        buttonCurrentOrder= tk.Button(self,text='Review Order', command=lambda: controller.show_frame(OrderSummary))
        buttonCurrentOrder.grid(row=0, column=2)
        buttonClose= tk.Button(self, text='Close ticket', command = lambda: controller.show_frame(TicketClose))
        
"""Creates the entree menu and returns the choices made"""
class EntreeMenu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        global tableList, currentTable
        labelDrinkTitle = tk.Label(self, text = 'Entrees',font = FONT_TYPE)
        labelDrinkTitle.grid(row=1,column=2)
        button1 =   tk.Button(self, text="Rib Plate", command=lambda: tableList[currentTable].addToOrder({'RibsPlate':15.99}))
        button1.grid(row=2, column=1)
        button2 =   tk.Button(self, text="Pulled Pork Plate", command=lambda: tableList[currentTable].addToOrder({'PorkPlate':12.99}))
        button2.grid(row=2, column=2)
        button3 =   tk.Button(self, text="Beef Plate", command=lambda: tableList[currentTable].addToOrder({'BeefPlate':13.49}))
        button3.grid(row=2,column=3)
        button4 =   tk.Button(self, text="Turkey Plate", command=lambda: tableList[currentTable].addToOrder({'TurkeyPlate':14.49}))
        button4.grid(row=3,column=1)
        button5 =   tk.Button(self, text="Sausage Plate", command=lambda: tableList[currentTable].addToOrder({'SausagePlate':12.49}))
        button5.grid(row=3, column=2)
        button6 =   tk.Button(self, text="Pork and Beef", command=lambda: tableList[currentTable].addToOrder({'PorkAndBeef':13.25}))
        button6.grid(row=3, column=3)
        button7 =   tk.Button(self, text="Soup", command=lambda: tableList[currentTable].addToOrder({'Soup':9.99}))
        button7.grid(row=4,column=1)
        button8 =   tk.Button(self, text="Entree Salad", command=lambda: tableList[currentTable].addToOrder({'BigSalad':9.99}))
        button8.grid(row=4,column=2)
        button9 =   tk.Button(self, text="Pork Sandwich", command=lambda: tableList[currentTable].addToOrder({'PorkSand':8.99}))
        button9.grid(row=4,column=3)
        button0 =   tk.Button(self, text="Beef Sandwich", command=lambda: tableList[currentTable].addToOrder({'BeefSand':9.99}))
        button0.grid(row=5,column=1)
        button0 =   tk.Button(self, text="Turkey Sandwich", command=lambda: tableList[tableNumber].addToOrder({'TurkeySand':10.49}))
        button0.grid(row=5,column=2)
        button0 =   tk.Button(self, text="Chili", command=lambda: tableList[tableNumber].addToOrder({'Chili':9.99}))
        button0.grid(row=5,column=3)
        buttonBack = tk.Button(self, text ="Return", command = lambda: controller.show_frame(OrderPage))
        buttonBack.grid(row=6,column=2)
        
"""Creates the kids menu and returns the choices made"""
class KidsMenu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        global tableList, currentTable
        labelDrinkTitle = tk.Label(self, text = 'Kids Entrees',font = FONT_TYPE)
        labelDrinkTitle.grid(row=1,column=2)
        button1 =   tk.Button(self, text="Kid Ribs", command=lambda: tableList[currentTable].addToOrder({'KidRib':6.99}))
        button1.grid(row=2, column=1)
        button2 =   tk.Button(self, text="Kid Pork", command=lambda: tableList[currentTable].addToOrder({'KidPork':5.99}))
        button2.grid(row=2, column=2)
        button3 =   tk.Button(self, text="Kid Beef", command=lambda: tableList[currentTable].addToOrder({'KidBeef':5.99}))
        button3.grid(row=2,column=3)
        button4 =   tk.Button(self, text="Kid Turkey", command=lambda: tableList[currentTable].addToOrder({'KidTurkey':6.99}))
        button4.grid(row=3,column=1)
        button5 =   tk.Button(self, text="Kid Sausage", command=lambda: tableList[currentTable].addToOrder({'KidSausage':5.99}))
        button5.grid(row=3, column=2)
        button6 =   tk.Button(self, text="Grilled Cheese", command=lambda: tableList[currentTable].addToOrder({'GrilledCheese':5.49}))
        button6.grid(row=3, column=3)
        button7 =   tk.Button(self, text="Pork 'n Beans", command=lambda: tableList[currentTable].addToOrder({"Pork'nBeans":5.99}))
        button7.grid(row=4,column=1)
        button8 =   tk.Button(self, text="Hotdog", command=lambda: tableList[currentTable].addToOrder({'Hotdog':5.49}))
        button8.grid(row=4,column=2)
        button9 =   tk.Button(self, text="Chicken Tenders", command=lambda: tableList[currentTable].addToOrder({'Tenders':5.99}))
        button9.grid(row=4,column=3)
        button0 =   tk.Button(self, text="Kid Chili", command=lambda: tableList[currentTable].addToOrder({'KidChili':5.99}))
        button0.grid(row=5,column=1)
        button0 =   tk.Button(self, text="Kid Pork Sandwich", command=lambda: tableList[currentTable].addToOrder({'KidPorkSand':4.49}))
        button0.grid(row=5,column=2)
        button0 =   tk.Button(self, text="Kid Turkey Sandwich", command=lambda: tableList[currentTable].addToOrder({'KidTurkSand':4.99}))
        button0.grid(row=5,column=3)
        buttonBack = tk.Button(self, text ="Return", command = lambda: controller.show_frame(OrderPage))
        buttonBack.grid(row=6,column=2)
        
"""Creates the sides menu and returns the choices made"""
class SidesMenu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        global tableList, currentTable
        labelDrinkTitle = tk.Label(self, text = 'Sides',font = FONT_TYPE)
        labelDrinkTitle.grid(row=1,column=2)
        button1 =   tk.Button(self, text="Baked Beans", command=lambda: tableList[currentTable].addToOrder({'Bakedbeans':0}))
        button1.grid(row=2, column=1)
        button2 =   tk.Button(self, text="Green Beans", command=lambda: tableList[currentTable].addToOrder({'GreenBeans':0}))
        button2.grid(row=2, column=2)
        button3 =   tk.Button(self, text="Corn", command=lambda: tableList[currentTable].addToOrder({'Corn':0}))
        button3.grid(row=2,column=3)
        button4 =   tk.Button(self, text="AppleSauce", command=lambda: tableList[currentTable].addToOrder({'Applesauce':0}))
        button4.grid(row=3,column=1)
        button5 =   tk.Button(self, text="Fries", command=lambda: tableList[currentTable].addToOrder({'Fries':0}))
        button5.grid(row=3, column=2)
        button6 =   tk.Button(self, text="Fried Okra", command=lambda: tableList[currentTable].addToOrder({'Okra':0}))
        button6.grid(row=3, column=3)
        button7 =   tk.Button(self, text="Potato Salad", command=lambda: tableList[currentTable].addToOrder({'Pot.Salad':0}))
        button7.grid(row=4,column=1)
        button8 =   tk.Button(self, text="Coleslaw", command=lambda: tableList[currentTable].addToOrder({'Slaw':0}))
        button8.grid(row=4,column=2)
        button9 =   tk.Button(self, text="Baked Potato", command=lambda: tableList[currentTable].addToOrder({'BakedPot':0}))
        button9.grid(row=4,column=3)
        buttonBack = tk.Button(self, text ="Return", command = lambda: controller.show_frame(OrderPage))
        buttonBack.grid(row=6,column=2)
        
"""Creates the drinks menu and returns the choices made"""
class DrinksMenu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        global tableList, currentTable
        labelDrinkTitle = tk.Label(self, text = 'Drinks',font = FONT_TYPE)
        labelDrinkTitle.grid(row=1,column=2)
        button1 =   tk.Button(self, text="Pepsi", command=lambda: tableList[currentTable].addToOrder({'Pepsi':2.49}))
        button1.grid(row=2, column=1)
        button2 =   tk.Button(self, text="Diet Pepsi", command=lambda: tableList[currentTable].addToOrder({'D.Pepsi':2.49}))
        button2.grid(row=2, column=2)
        button3 =   tk.Button(self, text="Mountain Dew", command=lambda: tableList[currentTable].addToOrder({'MtnDew':2.49}))
        button3.grid(row=2,column=3)
        button4 =   tk.Button(self, text="Diet Mountain Dew", command=lambda: tableList[currentTable].addToOrder({'D.MtnDew':2.49}))
        button4.grid(row=3,column=1)
        button5 =   tk.Button(self, text="Sierra Mist", command=lambda: tableList[currentTable].addToOrder({'SierraMist':2.49}))
        button5.grid(row=3, column=2)
        button6 =   tk.Button(self, text="Iced Tea", command=lambda: tableList[currentTable].addToOrder({'Tea':2.49}))
        button6.grid(row=3, column=3)
        button7 =   tk.Button(self, text="Lemonade", command=lambda: tableList[currentTable].addToOrder({'Lemonade':2.49}))
        button7.grid(row=4,column=1)
        button8 =   tk.Button(self, text="Coffee", command=lambda: tableList[currentTable].addToOrder({'Coffee':2.49}))
        button8.grid(row=4,column=2)
        button9 =   tk.Button(self, text="Decaf. Coffee", command=lambda: tableList[currentTable].addToOrder({'Decaf':2.49}))
        button9.grid(row=4,column=3)
        button0 =   tk.Button(self, text="Kids", command=lambda: tableList[currentTable].addToOrder({'KidsDrink':1.49}))
        button0.grid(row=5,column=1)
        button0 =   tk.Button(self, text="Water", command=lambda: tableList[currentTable].addToOrder({'Water':0}))
        button0.grid(row=5,column=2)
        button0 =   tk.Button(self, text="None", command=lambda: tableList[currentTable].addToOrder({'NoDrink':0}))
        button0.grid(row=5,column=3)
        buttonBack = tk.Button(self, text ="Return", command = lambda: controller.show_frame(OrderPage))
        buttonBack.grid(row=6,column=2)
        
"""Gives an overview of the the contents of what the table has ordered"""
class OrderSummary(tk.Frame):
    def __init__ (self,parent,controller):
        tk.Frame.__init__(self,parent)
        global tableList, currentTable
        labelTitle = tk.Label(self, text='Order overview')
        labelTitle.grid(row=1, column=1, columnspan=100)
        labelPlates = tk.Label(self,text='Plates')
        labelPlates.grid(row=2,column=0)   
        labelPlateall= tk.Label(self,text='') 
        labelPlateall.grid(row=3, column=0)
            
"""Presents the user with the total price and prompts the use to either go back or create a new table"""
class SubmissionPage(tk.Button):
    def _init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        labelTotal = tk.Label(self, text = "Your total is:", font = FONT_TYPE)
        labelTotal.grid(row=1, column=2)
        labelFinalPrice = tk.Label(self, text = finalPrice, font = FONT_TYPE)
        labelFinalPrice.grid(row=2, column=2)
        buttonBack = tk.button(self, text = 'Return', command = lambda: controller.show_frame(OrderSummary))
        buttonBack.grid(row=5, column=2)
        buttonTable = tk.Button(self,text ="Create new table", command = lambda: controller.show_frame(TabCreatePage))
        buttonTable.grid(row=6, column=2)
        
app=POSSystem()
app.mainloop()
