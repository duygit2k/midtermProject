import tkinter as tk
from tkinter import messagebox

class SearchItemDialog:

    def __init__(self, parent, rootWindow) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__choice = tk.IntVar()
        self.__choice.set(0)
        self.setComponents()
        self.setLocation()

    def setComponents(self):
        self.setWindow()
        self.setTextFields()
        self.setButtons()
        self.radioButtonsActionPerformed()

    def setLocation(self):
        self.__windowWidth = 400
        self.__windowHeight = 400
        self.__screenWidth = self.__searchItemWindow.winfo_screenwidth()
        self.__screenHeight = self.__searchItemWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__searchItemWindow.geometry(f'{self.__windowWidth}'
                                             f'x{self.__windowHeight}'
                                             f'+{self.__positionRight}'
                                             f'+{self.__positionTop}')

    def setWindow(self):
        self.__searchItemWindow = tk.Toplevel(self.__rootWindow)
        self.__searchItemWindow.config(bg="aliceblue")
        self.__searchItemWindow.title("Search Item")
        self.__topLabel = tk.Label(self.__searchItemWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Search item",
                                   bg="aliceblue"
                                   ).pack()
        self.__searchItemWindow.grab_set()

    def setTextFields(self):
        self.__txtId = tk.Entry(self.__searchItemWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__txtName = tk.Entry(self.__searchItemWindow)
        self.__txtName.place(x=125, y=140, width=240, height=25)
        self.__txtBrand = tk.Entry(self.__searchItemWindow)
        self.__txtBrand.place(x=125, y=180, width=240, height=25)
        self.__txtPrice = tk.Entry(self.__searchItemWindow)
        self.__txtPrice.place(x=125, y=220, width=240, height=25)

    def setButtons(self):
        self.__radio1 = tk.Radiobutton(self.__searchItemWindow,
                                       text="ID:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command = self.radioButtonsActionPerformed,
                                       value=0)
        self.__radio1.place(x=10, y=100)
        self.__radio2 = tk.Radiobutton(self.__searchItemWindow,
                                       text="Name:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=1)
        self.__radio2.place(x=10, y=140)
        self.__radio3 = tk.Radiobutton(self.__searchItemWindow,
                                       text="Brand:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=2)
        self.__radio3.place(x=10, y=180)
        self.__radio4 = tk.Radiobutton(self.__searchItemWindow,
                                       text="Price:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=3)
        self.__radio4.place(x=10, y=220)
        self.__btnSearch = tk.Button(self.__searchItemWindow, text="Search",
                                     bg="lightyellow",
                                     command=self.btnSearchActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__searchItemWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def radioButtonsActionPerformed(self):
        textFields = [self.__txtId, self.__txtName, self.__txtBrand,
                      self.__txtPrice]
        for x in textFields:
            if self.__choice.get() != textFields.index(x):
                x.config(state = "readonly")
            else:
                x.config(state = "normal")

    def btnSearchActionPerformed(self):
        id = self.__txtId.get()
        name = self.__txtName.get()
        brand = self.__txtBrand.get()
        price = self.__txtPrice.get()
        if self.__choice.get() == 0:
            if len(id) > 0:
                self.__parent.searchByIdCallBack(id, 3)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 1:
            if len(name) > 0:
                self.__parent.searchByNameCallBack(name)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 2:
            if len(brand) > 0:
                self.__parent.searchByBrandCallBack(brand)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        else:
            if len(price) > 0:
                self.__parent.searchByPriceCallBack(price)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")


    def btnCancelActionPerformed(self):
        self.__searchItemWindow.destroy()
