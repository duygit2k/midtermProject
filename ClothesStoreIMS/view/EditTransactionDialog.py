import tkinter as tk
from tkinter import messagebox

from model.Customer import Customer
from model.Employee import Employee
from model.Item import Item
from model.Transaction import Transaction


class EditTransactionDialog:

    def __init__(self, parent, rootWindow, customers, items, employees, transaction) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__customers = customers
        self.__items = items
        self.__employees = employees
        self.__transaction = transaction
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
        self.__screenWidth = self.__editTransactionWindow.winfo_screenwidth()
        self.__screenHeight = self.__editTransactionWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__editTransactionWindow.geometry(f'{self.__windowWidth}'
                                       f'x{self.__windowHeight}'
                                       f'+{self.__positionRight}'
                                       f'+{self.__positionTop}')

    def setWindow(self):
        self.__editTransactionWindow = tk.Toplevel(self.__rootWindow)
        self.__editTransactionWindow.config(bg="aliceblue")
        self.__editTransactionWindow.title("Edit Transaction")
        self.__topLabel = tk.Label(self.__editTransactionWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Edit Transaction",
                                   bg="aliceblue"
                                   ).pack()
        self.__editTransactionWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__editTransactionWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__editTransactionWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__editTransactionWindow,
                                 text="Customer ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtCustomerId = tk.Entry(self.__editTransactionWindow)
        self.__txtCustomerId.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__editTransactionWindow,
                                 text="Item ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtItemId = tk.Entry(self.__editTransactionWindow)
        self.__txtItemId.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__editTransactionWindow,
                                 text="Number:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtNumber = tk.Entry(self.__editTransactionWindow)
        self.__txtNumber.place(x=125, y=220, width=240, height=25)
        self.__label5 = tk.Label(self.__editTransactionWindow,
                                 text="Employee ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=260)
        self.__txtEmployeeId = tk.Entry(self.__editTransactionWindow)
        self.__txtEmployeeId.place(x=125, y=260, width=240, height=25)

    def setButtons(self):
        self.__btnEdit = tk.Button(self.__editTransactionWindow, text="Edit",
                                   bg="lightyellow",
                                   command=self.btnEditActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__editTransactionWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnEditActionPerformed(self):
        customerId = self.__txtCustomerId.get()
        itemId = self.__txtItemId.get()
        number = self.__txtNumber.get()
        employeeId = self.__txtEmployeeId.get()
        if len(customerId) > 0 and len(itemId) > 0 and len(number) > 0 and len(employeeId) > 0:
            try:
                customer = Customer(customerId, "", "", "")
                employee = Employee(employeeId, "", "", "", "")
                item = Item(itemId, "", "", "")
                if self.__customers.__contains__(customer) and \
                        self.__items.__contains__(item) and \
                        self.__employees.__contains__(employee):
                    cIndex = self.__customers.index(customer)
                    iIndex = self.__items.index(item)
                    eIndex = self.__employees.index(employee)
                    transaction = Transaction(str(self.__transaction.getId()),
                                              self.__customers[cIndex], self.__items[iIndex],
                                              number, self.__employees[eIndex])
                    self.__parent.editTransactionCallBack(transaction)
                    messagebox.showinfo("Success", "A transaction has been edited")
                    self.__editTransactionWindow.destroy()
                else:
                    messagebox.showerror("Error", "This information does not exist!")
            except Exception:
                messagebox.showerror("Error", "Invalid information format!")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__editTransactionWindow.destroy()

    def showDefaultText(self):
        self.__txtId.config(state="normal")
        self.__txtId.insert(0, self.__transaction.getId())
        self.__txtId.config(state="readonly")
        self.__txtCustomerId.delete(0, tk.END)
        self.__txtCustomerId.insert(0, self.__transaction.getCustomer().getId())
        self.__txtItemId.delete(0, tk.END)
        self.__txtItemId.insert(0, self.__transaction.getItem().getId())
        self.__txtNumber.delete(0, tk.END)
        self.__txtNumber.insert(0, self.__transaction.getNumber())
        self.__txtEmployeeId.delete(0, tk.END)
        self.__txtEmployeeId.insert(0, self.__transaction.getEmployee().getId())
