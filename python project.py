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
        frame = loginPage(container, self)
        self.frames[loginPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(loginPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

class loginPage(tk.Frame):##login page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome, enter your employee number to login!",font=FONT_TYPE)##this just shows text, not a button or anything
        label.pack(pady=10,padx=10)

app=POSSystem()
app.mainloop()
