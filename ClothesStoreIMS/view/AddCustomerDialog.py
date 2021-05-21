import tkinter as tk
from tkinter import messagebox

from model.Customer import Customer
from model.Person import Person


class AddCustomerDialog:

    def __init__(self, parent, rootWindow, customers) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__customers = customers
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
        self.__screenWidth = self.__addCustomerWindow.winfo_screenwidth()
        self.__screenHeight = self.__addCustomerWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__addCustomerWindow.geometry(f'{self.__windowWidth}'
                                          f'x{self.__windowHeight}'
                                          f'+{self.__positionRight}'
                                          f'+{self.__positionTop}')

    def setWindow(self):
        self.__addCustomerWindow = tk.Toplevel(self.__rootWindow)
        self.__addCustomerWindow.config(bg="aliceblue")
        self.__addCustomerWindow.title("Add Customer")
        self.__topLabel = tk.Label(self.__addCustomerWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Add new customer",
                                   bg="aliceblue"
                                   ).pack()
        self.__addCustomerWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__addCustomerWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__addCustomerWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__addCustomerWindow,
                                 text="Full Name:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtFullName = tk.Entry(self.__addCustomerWindow)
        self.__txtFullName.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__addCustomerWindow,
                                 text="Address:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtAddress = tk.Entry(self.__addCustomerWindow)
        self.__txtAddress.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__addCustomerWindow,
                                 text="Phone Number:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtPhoneNumber = tk.Entry(self.__addCustomerWindow)
        self.__txtPhoneNumber.place(x=125, y=220, width=240, height=25)

    def setButtons(self):
        self.__btnAdd = tk.Button(self.__addCustomerWindow, text="Add",
                                  bg="lightyellow",
                                  command=self.btnAddActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__addCustomerWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnAddActionPerformed(self):
        fullName = self.__txtFullName.get()
        address = self.__txtAddress.get()
        phoneNumber = self.__txtPhoneNumber.get()
        if len(fullName) > 0 and len(address) > 0 and len(phoneNumber) > 0:
            try:
                customer = Person(fullName, address, phoneNumber)
                if self.__customers.__contains__(customer):
                    messagebox.showerror("Error", "Customer information already exists!")
                else:
                    customer = Customer("", fullName, address, phoneNumber)
                    customer.fixId()
                    self.__parent.addCustomerCallBack(customer)
                    messagebox.showinfo("Success", "A new customer has been added")
                    self.showDefaultText()
            except Exception:
                messagebox.showerror("Error", "Invalid information format!")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__addCustomerWindow.destroy()

    def showDefaultText(self):
        self.__txtId.config(state="normal")
        self.__txtId.delete(0, tk.END)
        self.__txtId.insert(0, Customer.customerId)
        self.__txtId.config(state="readonly")
        self.__txtFullName.delete(0, tk.END)
        self.__txtFullName.insert(0, "")
        self.__txtAddress.delete(0, tk.END)
        self.__txtAddress.insert(0, "")
        self.__txtPhoneNumber.delete(0, tk.END)
        self.__txtPhoneNumber.insert(0, "")
