import tkinter as tk
from tkinter import messagebox

from model.Item import Item

class EditItemDialog:

    def __init__(self, parent, rootWindow, items, item) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__items = items
        self.__item = item
        self.setComponents()
        self.setLocation()
        self.showDefaultText()

    def setComponents(self):
        self.setWindow()
        self.setTextFields()
        self.setButtons()

    def setLocation(self):
        self.__windowWidth = 400
        self.__windowHeight = 400
        self.__screenWidth = self.__editItemWindow.winfo_screenwidth()
        self.__screenHeight = self.__editItemWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__editItemWindow.geometry(f'{self.__windowWidth}'
                                       f'x{self.__windowHeight}'
                                       f'+{self.__positionRight}'
                                       f'+{self.__positionTop}')

    def setWindow(self):
        self.__editItemWindow = tk.Toplevel(self.__rootWindow)
        self.__editItemWindow.config(bg="aliceblue")
        self.__editItemWindow.title("Edit Item")
        self.__topLabel = tk.Label(self.__editItemWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Edit Item",
                                   bg="aliceblue"
                                   ).pack()
        self.__editItemWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__editItemWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__editItemWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__editItemWindow,
                                 text="Name:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtName = tk.Entry(self.__editItemWindow)
        self.__txtName.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__editItemWindow,
                                 text="Brand:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtBrand = tk.Entry(self.__editItemWindow)
        self.__txtBrand.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__editItemWindow,
                                 text="Price:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtPrice = tk.Entry(self.__editItemWindow)
        self.__txtPrice.place(x=125, y=220, width=240, height=25)

    def setButtons(self):
        self.__btnEdit = tk.Button(self.__editItemWindow, text="Edit",
                                   bg="lightyellow",
                                   command=self.btnEditActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__editItemWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnEditActionPerformed(self):
        name = self.__txtName.get()
        brand = self.__txtBrand.get()
        price = self.__txtPrice.get()
        if len(name) > 0 and len(brand) > 0 and len(price) > 0:
            item = Item(str(self.__item.getId()), name, brand, price)
            self.__parent.editItemCallBack(item)
            self.__editItemWindow.destroy()
            messagebox.showinfo("Success", "Item information has been edited")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__editItemWindow.destroy()

    def showDefaultText(self):
        self.__txtId.insert(0, self.__item.getId())
        self.__txtId.config(state="readonly")
        self.__txtName.insert(0, self.__item.getName())
        self.__txtBrand.insert(0, self.__item.getBrand())
        self.__txtPrice.insert(0, self.__item.getPrice())
