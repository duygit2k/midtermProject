import tkinter as tk
from tkinter import messagebox

from model.Customer import Customer
from model.Employee import Employee
from model.Item import Item
from model.Transaction import Transaction


class AddTransactionDialog:

    def __init__(self, parent, rootWindow, customers, items, employees) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__customers = customers
        self.__items = items
        self.__employees = employees
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
        self.__screenWidth = self.__addTransactionWindow.winfo_screenwidth()
        self.__screenHeight = self.__addTransactionWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__addTransactionWindow.geometry(f'{self.__windowWidth}'
                                             f'x{self.__windowHeight}'
                                             f'+{self.__positionRight}'
                                             f'+{self.__positionTop}')

    def setWindow(self):
        self.__addTransactionWindow = tk.Toplevel(self.__rootWindow)
        self.__addTransactionWindow.config(bg="aliceblue")
        self.__addTransactionWindow.title("Add Transaction")
        self.__topLabel = tk.Label(self.__addTransactionWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Add new transaction",
                                   bg="aliceblue"
                                   ).pack()
        self.__addTransactionWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__addTransactionWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__addTransactionWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__addTransactionWindow,
                                 text="Customer ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtCustomerId = tk.Entry(self.__addTransactionWindow)
        self.__txtCustomerId.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__addTransactionWindow,
                                 text="Item ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtItemId = tk.Entry(self.__addTransactionWindow)
        self.__txtItemId.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__addTransactionWindow,
                                 text="Number:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtNumber = tk.Entry(self.__addTransactionWindow)
        self.__txtNumber.place(x=125, y=220, width=240, height=25)
        self.__label5 = tk.Label(self.__addTransactionWindow,
                                 text="Employee ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=260)
        self.__txtEmployeeId = tk.Entry(self.__addTransactionWindow)
        self.__txtEmployeeId.place(x=125, y=260, width=240, height=25)

    def setButtons(self):
        self.__btnAdd = tk.Button(self.__addTransactionWindow, text="Add",
                                  bg="lightyellow",
                                  command=self.btnAddActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__addTransactionWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnAddActionPerformed(self):
        customerId = self.__txtCustomerId.get()
        itemId = self.__txtItemId.get()
        number = self.__txtNumber.get()
        employeeId = self.__txtEmployeeId.get()
        if len(customerId) > 0 and len(itemId) > 0 and len(number) > 0 and len(employeeId) > 0:
            try:
                customer = Customer(customerId, "", "", "")
                item = Item(itemId, "", "", "")
                employee = Employee(employeeId, "", "", "", "")
                if self.__customers.__contains__(customer) \
                        and self.__items.__contains__(item) and\
                        self.__employees.__contains__(employee):
                    cIndex = self.__customers.index(customer)
                    iIndex = self.__items.index(item)
                    eIndex = self.__employees.index(employee)
                    transaction = Transaction("", self.__customers[cIndex],
                                              self.__items[iIndex], number,
                                              self.__employees[eIndex])
                    transaction.fixId()
                    self.__parent.addTransactionCallBack(transaction)
                    messagebox.showinfo("Success", "A new transaction has been added")
                    self.showDefaultText()
                else:
                    messagebox.showerror("Error", "This information does not exist!")
            except Exception:
                messagebox.showerror("Error", "Invalid information format!")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__addTransactionWindow.destroy()

    def showDefaultText(self):
        self.__txtId.config(state="normal")
        self.__txtId.delete(0, tk.END)
        self.__txtId.insert(0, Transaction.transactionId)
        self.__txtId.config(state="readonly")
        self.__txtCustomerId.delete(0, tk.END)
        self.__txtCustomerId.insert(0, "")
        self.__txtItemId.delete(0, tk.END)
        self.__txtItemId.insert(0, "")
        self.__txtNumber.delete(0, tk.END)
        self.__txtNumber.insert(0, "")
        self.__txtEmployeeId.delete(0, tk.END)
        self.__txtEmployeeId.insert(0, "")
