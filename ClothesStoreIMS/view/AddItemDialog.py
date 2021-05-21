import tkinter as tk
from tkinter import messagebox

from model.Customer import Customer
from model.Item import Item


class AddItemDialog:

    def __init__(self, parent, rootWindow, items) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__items = items
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
        self.__screenWidth = self.__addItemWindow.winfo_screenwidth()
        self.__screenHeight = self.__addItemWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__addItemWindow.geometry(f'{self.__windowWidth}'
                                          f'x{self.__windowHeight}'
                                          f'+{self.__positionRight}'
                                          f'+{self.__positionTop}')

    def setWindow(self):
        self.__addItemWindow = tk.Toplevel(self.__rootWindow)
        self.__addItemWindow.config(bg="aliceblue")
        self.__addItemWindow.title("Add Item")
        self.__topLabel = tk.Label(self.__addItemWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Add new item",
                                   bg="aliceblue"
                                   ).pack()
        self.__addItemWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__addItemWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__addItemWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__addItemWindow,
                                 text="Name:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtName = tk.Entry(self.__addItemWindow)
        self.__txtName.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__addItemWindow,
                                 text="Brand:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtBrand = tk.Entry(self.__addItemWindow)
        self.__txtBrand.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__addItemWindow,
                                 text="Price:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtPrice = tk.Entry(self.__addItemWindow)
        self.__txtPrice.place(x=125, y=220, width=240, height=25)

    def setButtons(self):
        self.__btnAdd = tk.Button(self.__addItemWindow, text="Add",
                                  bg="lightyellow",
                                  command=self.btnAddActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__addItemWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnAddActionPerformed(self):
        name = self.__txtName.get()
        brand = self.__txtBrand.get()
        price = self.__txtPrice.get()
        if len(name) > 0 and len(brand) > 0 and len(price) > 0:
            try:
                item = Item("", name, brand, price)
                if self.__items.__contains__(item):
                    messagebox.showerror("Error", "Item information already exists!")
                else:
                    item.fixId()
                    self.__parent.addItemCallBack(item)
                    messagebox.showinfo("Success", "A new item has been added")
                    self.showDefaultText()
            except Exception:
                messagebox.showerror("Error", "Invalid information format!")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__addItemWindow.destroy()

    def showDefaultText(self):
        self.__txtId.config(state="normal")
        self.__txtId.delete(0, tk.END)
        self.__txtId.insert(0, Item.itemId)
        self.__txtId.config(state="readonly")
        self.__txtName.delete(0, tk.END)
        self.__txtName.insert(0, "")
        self.__txtBrand.delete(0, tk.END)
        self.__txtBrand.insert(0, "")
        self.__txtPrice.delete(0, tk.END)
        self.__txtPrice.insert(0, "")
