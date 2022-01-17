
from cgitb import text
from email.mime import image
from msilib.schema import ListBox
from textwrap import fill
import tkinter as tk
from tkinter import ANCHOR, Canvas, Menu, Listbox, Label, Button, Toplevel
from tkinter.ttk import Separator
from turtle import width
from PIL import ImageTk, Image 


from packages_manager import PackadgeManager


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.appWidth = 1200
        self.appHeight = 800



        self.parent = parent
        self.parent.title("GFXMaker")
        self.parent.geometry(str(self.appWidth)+"x"+str(self.appHeight))
        self.addTopMenu()

        self.packages = PackadgeManager.loadPackages()


        self.widgets = tk.Frame(parent, bg='#d9d9d9', width=self.appWidth, height=40, relief='groove', borderwidth=2)
        self.widgets.grid(row=0, column=0, columnspan=3)
        self.widgets.grid_propagate(False)

        self.sidebar = tk.Frame(parent, width=40, height=730, relief='groove', borderwidth=2)
        self.sidebar.grid(row=1, column=0)
        self.sidebar.grid_propagate(False)

        self.mainarea = tk.Frame(parent, width=910, height=730)
        self.mainarea.grid(row=1, column=1)
        self.mainarea.grid_propagate(False)

        self.properties = tk.Frame(parent, width=250, height=730, relief='groove', borderwidth=2)
        self.properties.grid(row=1, column=2, sticky="nw")
        self.properties.grid_propagate(False)

        self.notifications = tk.Frame(parent, width=1200, bg='#d9d9d9', height=30, relief='groove', borderwidth=2)
        self.notifications.grid(row=2, column=0, columnspan=3)
        self.notifications.grid_propagate(False)

        self.insertCanvas()
        self.fillSideBar()
        # self.fillPropertiesBar()
        # self.fillWidtgets()
    
    # def fillWidtgets(self):
    #     self.lineIcon = ImageTk.PhotoImage(Image.open('images/icons/line.png').resize((24,24)))
    #     Button(self.widgets, image=self.lineIcon, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")
        
    #     self.square = ImageTk.PhotoImage(Image.open('images/icons/square.png').resize((24,24)))
    #     Button(self.widgets, image=self.square, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")

    #     self.squareRounded = ImageTk.PhotoImage(Image.open('images/icons/square_rounded.png').resize((24,24)))
    #     Button(self.widgets, image=self.squareRounded, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")

    #     self.triangle = ImageTk.PhotoImage(Image.open('images/icons/triangle.png').resize((24,24)))
    #     Button(self.widgets, image=self.triangle, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")

    #     self.circle = ImageTk.PhotoImage(Image.open('images/icons/circle.png').resize((24,24)))
    #     Button(self.widgets, image=self.circle, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")

    #     self.hexagon = ImageTk.PhotoImage(Image.open('images/icons/hexagon.png').resize((24,24)))
    #     Button(self.widgets, image=self.hexagon, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")

    #     self.text = ImageTk.PhotoImage(Image.open('images/icons/text.png').resize((24,24)))
    #     Button(self.widgets, image=self.text, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")

    #     self.button = ImageTk.PhotoImage(Image.open('images/icons/button.png').resize((24,24)))
    #     Button(self.widgets, image=self.button, highlightthickness = 0, bd = 0).pack(padx=(5,0), side="left", anchor="w")


    def fillSideBar(self):
        
        
        self.sidebar.columnconfigure(0, weight=1)

        borderType = "flat"
        borderWeight = 1

        row = 0

        
        self.cursor = ImageTk.PhotoImage(Image.open('images/icons/cursor.png').resize((24,24)))
        Button(self.sidebar, image=self.cursor, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row += 1
        Separator(self.sidebar, orient="horizontal").grid(row=row, column=0, sticky="ew")

        row += 1
        self.lineIcon = ImageTk.PhotoImage(Image.open('images/icons/line.png').resize((24,24)))
        Button(self.sidebar, image=self.lineIcon, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        self.square = ImageTk.PhotoImage(Image.open('images/icons/square.png').resize((24,24)))
        Button(self.sidebar, image=self.square, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        self.squareRounded = ImageTk.PhotoImage(Image.open('images/icons/square_rounded.png').resize((24,24)))
        Button(self.sidebar, image=self.squareRounded, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        self.circle = ImageTk.PhotoImage(Image.open('images/icons/circle.png').resize((24,24)))
        Button(self.sidebar, image=self.circle, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)
        
        row +=1
        self.triangle = ImageTk.PhotoImage(Image.open('images/icons/triangle.png').resize((24,24)))
        Button(self.sidebar, image=self.triangle, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        self.hexagon = ImageTk.PhotoImage(Image.open('images/icons/hexagon.png').resize((24,24)))
        Button(self.sidebar, image=self.hexagon, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        Separator(self.sidebar, orient="horizontal").grid(row=row, column=0, sticky="ew")

        row +=1
        self.text = ImageTk.PhotoImage(Image.open('images/icons/text.png').resize((24,24)))
        Button(self.sidebar, image=self.text, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        self.button = ImageTk.PhotoImage(Image.open('images/icons/button.png').resize((24,24)))
        Button(self.sidebar, image=self.button, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)

        row +=1
        self.frame = ImageTk.PhotoImage(Image.open('images/icons/frame.png').resize((24,24)))
        Button(self.sidebar, image=self.frame, borderwidth=borderWeight, relief=borderType).grid(row=row, column=0, pady=2)
        # Label(self.sidebar, text="Available units:", font=('Myriad 12'), bg="#e6e6e6").pack(pady=(10,0))
        

        # self.lineIcon = ImageTk.PhotoImage(Image.open('images/icons/line.png').resize((24,24)))
        # Label(self.sidebar, image=self.lineIcon).grid(row=1, column=1)
        # Label(self.sidebar, text="Simple Line").pack(anchor="nw", padx=(5,0), side="left")

        # Lb1 = Listbox(self.sidebar, height=18)
        # for p in self.packages:
        #     Lb1.insert(1, p["name"])
        # Lb1.pack(pady=(10,0), padx=(5,5), fill="x")

        # Label(self.sidebar, text="Package info:", font=('Myriad 12'), bg="#e6e6e6").pack(pady=(10,0))

        # img = Image.open('images/no_preview.png').resize((100,100))
        # self.preview = ImageTk.PhotoImage(img)
        # Label(self.sidebar, image=self.preview).pack()

    
    # def fillPropertiesBar(self):
    #     Label(self.properties, text="Properties:", font=('Myriad 12'), bg="#e6e6e6").pack(pady=(0,0))

    def canvasKeyCallback(self, event):
        print(event)
    
    def canvasMouseClickCallback(self, event):
        print(event)

    

    def insertCanvas(self):

        canvasDimensions = (400,400)
        self.canvas = Canvas(self.mainarea, width=canvasDimensions[0], height=canvasDimensions[1], borderwidth=0, highlightthickness=0)
        self.mainarea.columnconfigure(0, weight=1)
        self.mainarea.rowconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0)
        self.canvas.config(background="white")
        self.canvas.bind("<Key>", self.canvasKeyCallback)
        self.canvas.bind("<Button-1>", self.canvasMouseClickCallback)

        self.canvas.create_text(canvasDimensions[0]/2, canvasDimensions[1]/2, text="Please choose a package to begin...", fill="black", font=('Meriad 15 bold'))


        # # fill grid
        # colSize=canvasDimensions[0]/30
        # for row in range(31):
        #     self.canvas.create_line(0, row*colSize, canvasDimensions[0], row*colSize, fill='#ccc')
        # for col in range(31):
        #     self.canvas.create_line(col*colSize, 0, col*colSize, canvasDimensions[0], fill='#ccc')
                
                    

        # pilImage = Image.open("Packages/TFT2.4_I96535/frame.jpg")

        # self.image = ImageTk.PhotoImage(pilImage)
        # self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.update


    def choosePackage(self):
        # self.menubar.entryconfig("Choose package", state="disabled")
        managerWin = Toplevel(self.parent)
        managerWin.title("Package Manager")
        managerWin.geometry("800x400")
        managerWin.resizable(False, False)

        Label(managerWin, text="Available Packages:").grid(row=0, column=0, pady=(5,0))
        pack = Listbox(managerWin, width=30, height=22)
        pack.grid(row=1, column=0, padx=5, pady=(5,0))

        Label(managerWin, text="Information about package:").grid(row=0, column=1, pady=(5,0))
        managerWin.columnconfigure(1, weight=1)

        



        if self.packages:
            for p in self.packages:
                pack.insert(1, self.packages[p]['name'])
        else:
                pack.insert(1, "NO packages found!")
        
        
    
        


    def addTopMenu(self):
        self.menubar = Menu(self.parent)

        file = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='File', menu = file)
        file.add_command(label ='New File', command = None)
        file.add_command(label ='Open...', command = None)
        file.add_command(label ='Save', command = None)
        file.add_separator()
        
        packageManager = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Package Manager', menu = packageManager)
        packageManager.add_command(label ='Choose package', command = self.choosePackage)
        packageManager.add_command(label ='Add new packadge from zip', command = None)

        # Adding Edit Menu and commands
        edit = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)
        

        self.parent.config(menu = self.menubar)

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid(row=0, column=0)
    root.mainloop()