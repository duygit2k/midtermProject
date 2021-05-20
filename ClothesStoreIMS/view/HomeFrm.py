import tkinter as tk
from tkinter import messagebox, ttk, CENTER, W, NO
import mysql.connector
from model.Customer import Customer
from model.Employee import Employee
from model.Item import Item
from model.Transaction import Transaction
from view.AddEmployeeDialog import AddEmployeeDialog
from view.AddItemDialog import AddItemDialog
from view.AddTransactionDialog import AddTransactionDialog
from view.EditEmployeeDialog import EditEmployeeDialog
from view.EditItemDialog import EditItemDialog
from view.EditTransactionDialog import EditTransactionDialog
from view.SearchEmployeeDialog import SearchEmployeeDialog
from view.SearchItemDialog import SearchItemDialog
from view.SearchTransactionDialog import SearchTransactionDialog
from view.SortCustomerDialog import SortCustomerDialog
from view.AddCustomerDialog import AddCustomerDialog
from view.EditCustomerDialog import EditCustomerDialog
from view.SearchCustomerDialog import SearchCustomerDialog
from view.SortEmployeeDialog import SortEmployeeDialog
from view.SortItemDialog import SortItemDialog
from view.SortTransactionDialog import SortTransactionDialog

from controller.SQLConnection import SQLConnection


class HomeFrm:

    def __init__(self):
        self.setSQLConnection()
        self.setData()
        self.setComponents()
        self.setLocation()
        self.showCustomers(self.__customers)
        self.showEmployees(self.__employees)
        self.showItems(self.__items)
        self.showTransactions(self.__transactions)

    def setComponents(self):
        self.setRootWindow()
        self.setTabbedPane()
        self.setCustomerTable()
        self.setEmployeeTable()
        self.setItemTable()
        self.setTransactionTable()
        self.setButtons()

    def setSQLConnection(self):
        myDb = mysql.connector.connect(
            host="localhost",
            user="duya1",
            password="123456789",
            database="clothesstore"
        )
        self.__sqlConnection = SQLConnection(myDb)

    def setLocation(self):
        self.__windowWidth = 850
        self.__windowHeight = 600
        self.__screenWidth = self.__rootWindow.winfo_screenwidth()
        self.__screenHeight = self.__rootWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__rootWindow.geometry(f'{self.__windowWidth}'
                                   f'x{self.__windowHeight}'
                                   f'+{self.__positionRight}'
                                   f'+{self.__positionTop}')

    def setData(self):
        self.__customers = self.__sqlConnection.readCustomerTable()
        self.__employees = self.__sqlConnection.readEmployeeTable()
        self.__items = self.__sqlConnection.readItemTable()
        self.__transactions = self.__sqlConnection.readTransactionTable()
        self.fixCustomerId()
        self.fixEmployeeId()
        self.fixItemId()
        self.fixTransactionId()

    def setVisible(self, mode):
        if mode == True:
            self.__rootWindow.mainloop()
        else:
            self.__rootWindow.destroy()

    def setRootWindow(self):
        self.__rootWindow = tk.Tk()
        self.__rootWindow.title("Clothes Store Information Management System")
        self.__rootWindow.resizable(False, False)

    def setTabbedPane(self):
        self.__tabbedPane = ttk.Notebook(self.__rootWindow)
        self.__customerTab = tk.Frame(self.__tabbedPane, bg="aliceblue")
        self.__employeeTab = tk.Frame(self.__tabbedPane, bg="aliceblue")
        self.__itemTab = tk.Frame(self.__tabbedPane, bg="aliceblue")
        self.__transactionTab = tk.Frame(self.__tabbedPane, bg="aliceblue")
        self.__tabbedPane.add(self.__customerTab, text="Customer")
        self.__tabbedPane.add(self.__employeeTab, text="Employee")
        self.__tabbedPane.add(self.__itemTab, text="Item")
        self.__tabbedPane.add(self.__transactionTab, text="Transaction")
        self.__tabbedPane.pack(expand=1, fill="both")

    def setButtons(self):
        self.__btnExit = tk.Button(self.__rootWindow,
                                   text="Exit",
                                   command=self.btnExitActionPerformed,
                                   bg="lightyellow"
                                   ).place(
            x=365, y=530, width=120, height=35)
        self.__btnAddCustomer = tk.Button(self.__customerTab,
                                          text="Add",
                                          command=self.btnAddCustomerActionPerformed,
                                          bg="lightyellow"
                                          ).place(
            x=300, y=350, width=120, height=35)
        self.__btnEditCustomer = tk.Button(self.__customerTab,
                                           text="Edit",
                                           command=self.btnEditCustomerActionPerformed,
                                           bg="lightyellow"
                                           ).place(
            x=430, y=350, width=120, height=35)
        self.__btnRemoveCustomer = tk.Button(self.__customerTab,
                                             text="Remove",
                                             command=self.btnRemoveCustomerActionPerformed,
                                             bg="lightyellow"
                                             ).place(
            x=300, y=400, width=120, height=35)
        self.__btnSearchCustomer = tk.Button(self.__customerTab,
                                             text="Search",
                                             command=self.btnSearchCustomerActionPerformed,
                                             bg="lightyellow"
                                             ).place(
            x=430, y=400, width=120, height=35)
        self.__btnRefreshCustomer = tk.Button(self.__customerTab,
                                              text="Refresh",
                                              command=self.btnRefreshCustomerActionPerformed,
                                              bg="lightyellow"
                                              ).place(
            x=300, y=450, width=120, height=35)
        self.__btnSortCustomer = tk.Button(self.__customerTab,
                                           text="Sort",
                                           command=self.btnSortCustomerActionPerformed,
                                           bg="lightyellow"
                                           ).place(
            x=430, y=450, width=120, height=35)
        self.__btnAddEmployee = tk.Button(self.__employeeTab,
                                          text="Add",
                                          command=self.btnAddEmployeeActionPerformed,
                                          bg="lightyellow"
                                          ).place(
            x=300, y=350, width=120, height=35)
        self.__btnEditEmployee = tk.Button(self.__employeeTab,
                                           text="Edit",
                                           command=self.btnEditEmployeeActionPerformed,
                                           bg="lightyellow"
                                           ).place(
            x=430, y=350, width=120, height=35)
        self.__btnRemoveEmployee = tk.Button(self.__employeeTab,
                                             text="Remove",
                                             command=self.btnRemoveEmployeeActionPerformed,
                                             bg="lightyellow"
                                             ).place(
            x=300, y=400, width=120, height=35)
        self.__btnSearchEmployee = tk.Button(self.__employeeTab,
                                             text="Search",
                                             command=self.btnSearchEmployeeActionPerformed,
                                             bg="lightyellow"
                                             ).place(
            x=430, y=400, width=120, height=35)
        self.__btnRefreshEmployee = tk.Button(self.__employeeTab,
                                              text="Refresh",
                                              command=self.btnRefreshEmployeeActionPerformed,
                                              bg="lightyellow"
                                              ).place(
            x=300, y=450, width=120, height=35)
        self.__btnSortEmployee = tk.Button(self.__employeeTab,
                                           text="Sort",
                                           command=self.btnSortEmployeeActionPerformed,
                                           bg="lightyellow"
                                           ).place(
            x=430, y=450, width=120, height=35)
        self.__btnAddItem = tk.Button(self.__itemTab,
                                      text="Add",
                                      command=self.btnAddItemActionPerformed,
                                      bg="lightyellow"
                                      ).place(
            x=300, y=350, width=120, height=35)
        self.__btnEditItem = tk.Button(self.__itemTab,
                                       text="Edit",
                                       command=self.btnEditItemActionPerformed,
                                       bg="lightyellow"
                                       ).place(
            x=430, y=350, width=120, height=35)
        self.__btnRemoveItem = tk.Button(self.__itemTab,
                                         text="Remove",
                                         command=self.btnRemoveItemActionPerformed,
                                         bg="lightyellow"
                                         ).place(
            x=300, y=400, width=120, height=35)
        self.__btnSearchItem = tk.Button(self.__itemTab,
                                         text="Search",
                                         command=self.btnSearchItemActionPerformed,
                                         bg="lightyellow"
                                         ).place(
            x=430, y=400, width=120, height=35)
        self.__btnRefreshItem = tk.Button(self.__itemTab,
                                          text="Refresh",
                                          command=self.btnRefreshItemActionPerformed,
                                          bg="lightyellow"
                                          ).place(
            x=300, y=450, width=120, height=35)
        self.__btnSortEmployee = tk.Button(self.__itemTab,
                                           text="Sort",
                                           command=self.btnSortItemActionPerformed,
                                           bg="lightyellow"
                                           ).place(
            x=430, y=450, width=120, height=35)
        self.__btnAddTransaction = tk.Button(self.__transactionTab,
                                             text="Add",
                                             command=self.btnAddTransactionActionPerformed,
                                             bg="lightyellow"
                                             ).place(
            x=300, y=350, width=120, height=35)
        self.__btnEditTransaction = tk.Button(self.__transactionTab,
                                              text="Edit",
                                              command=self.btnEditTransactionActionPerformed,
                                              bg="lightyellow"
                                              ).place(
            x=430, y=350, width=120, height=35)
        self.__btnRemoveTransaction = tk.Button(self.__transactionTab,
                                                text="Remove",
                                                command=self.btnRemoveTransactionActionPerformed,
                                                bg="lightyellow"
                                                ).place(
            x=300, y=400, width=120, height=35)
        self.__btnSearchTransaction = tk.Button(self.__transactionTab,
                                                text="Search",
                                                command=self.btnSearchTransactionActionPerformed,
                                                bg="lightyellow"
                                                ).place(
            x=430, y=400, width=120, height=35)
        self.__btnRefreshTransaction = tk.Button(self.__transactionTab,
                                                 text="Refresh",
                                                 command=self.btnRefreshTransactionActionPerformed,
                                                 bg="lightyellow"
                                                 ).place(
            x=300, y=450, width=120, height=35)
        self.__btnSortTransaction = tk.Button(self.__transactionTab,
                                              text="Sort",
                                              command=self.btnSortTransactionActionPerformed,
                                              bg="lightyellow"
                                              ).place(
            x=430, y=450, width=120, height=35)

    def setCustomerTable(self):
        self.__topLabel1 = tk.Label(self.__customerTab,
                                    height=2,
                                    font=("Arial", 20),
                                    text="Customer Information",
                                    bg="aliceblue"
                                    ).pack()
        self.__scroll1 = tk.Scrollbar(self.__customerTab)
        self.__scroll1.place(x=774, y=70, width=20, height=227)
        self.__tblCustomer = ttk.Treeview(self.__customerTab, yscrollcommand=self.__scroll1.set)
        self.__tblCustomer.pack()
        self.__scroll1.config(command=self.__tblCustomer.yview)
        self.__tblCustomer["columns"] = ("ID", "Full Name", "Address",
                                         "Phone Number")
        self.__tblCustomer.column("#0", width=0, stretch=NO)
        self.__tblCustomer.column("ID", anchor=CENTER, width=100)
        self.__tblCustomer.column("Full Name", anchor=CENTER, width=200)
        self.__tblCustomer.column("Address", anchor=CENTER, width=200)
        self.__tblCustomer.column("Phone Number", anchor=CENTER, width=200)
        self.__tblCustomer.heading("#0", text="", anchor=CENTER)
        self.__tblCustomer.heading("ID", text="ID", anchor=CENTER)
        self.__tblCustomer.heading("Full Name", text="Full Name", anchor=CENTER)
        self.__tblCustomer.heading("Address", text="Address", anchor=CENTER)
        self.__tblCustomer.heading("Phone Number", text="Phone Number",
                                   anchor=CENTER)

    def setEmployeeTable(self):
        self.__topLabel1 = tk.Label(self.__employeeTab,
                                    height=2,
                                    font=("Arial", 20),
                                    text="Employee Information",
                                    bg="aliceblue"
                                    ).pack()
        self.__scroll1 = tk.Scrollbar(self.__employeeTab)
        self.__scroll1.place(x=774, y=70, width=20, height=227)
        self.__tblEmployee = ttk.Treeview(self.__employeeTab, yscrollcommand=self.__scroll1.set)
        self.__tblEmployee.pack()
        self.__scroll1.config(command=self.__tblEmployee.yview)
        self.__tblEmployee["columns"] = ("ID", "Full Name", "Address",
                                         "Phone Number", "Salary")
        self.__tblEmployee.column("#0", width=0, stretch=NO)
        self.__tblEmployee.column("ID", anchor=CENTER, width=100)
        self.__tblEmployee.column("Full Name", anchor=CENTER, width=150)
        self.__tblEmployee.column("Address", anchor=CENTER, width=150)
        self.__tblEmployee.column("Phone Number", anchor=CENTER, width=150)
        self.__tblEmployee.column("Salary", anchor=CENTER, width=150)
        self.__tblEmployee.heading("#0", text="", anchor=CENTER)
        self.__tblEmployee.heading("ID", text="ID", anchor=CENTER)
        self.__tblEmployee.heading("Full Name", text="Full Name", anchor=CENTER)
        self.__tblEmployee.heading("Address", text="Address", anchor=CENTER)
        self.__tblEmployee.heading("Phone Number", text="Phone Number",
                                   anchor=CENTER)
        self.__tblEmployee.heading("Salary", text="Salary",
                                   anchor=CENTER)

    def setItemTable(self):
        self.__topLabel1 = tk.Label(self.__itemTab,
                                    height=2,
                                    font=("Arial", 20),
                                    text="Item Information",
                                    bg="aliceblue"
                                    ).pack()
        self.__scroll1 = tk.Scrollbar(self.__itemTab)
        self.__scroll1.place(x=774, y=70, width=20, height=227)
        self.__tblItem = ttk.Treeview(self.__itemTab, yscrollcommand=self.__scroll1.set)
        self.__tblItem.pack()
        self.__scroll1.config(command=self.__tblItem.yview)
        self.__tblItem["columns"] = ("ID", "Name", "Brand",
                                     "Price")
        self.__tblItem.column("#0", width=0, stretch=NO)
        self.__tblItem.column("ID", anchor=CENTER, width=100)
        self.__tblItem.column("Name", anchor=CENTER, width=200)
        self.__tblItem.column("Brand", anchor=CENTER, width=200)
        self.__tblItem.column("Price", anchor=CENTER, width=200)
        self.__tblItem.heading("#0", text="", anchor=CENTER)
        self.__tblItem.heading("ID", text="ID", anchor=CENTER)
        self.__tblItem.heading("Name", text="Name", anchor=CENTER)
        self.__tblItem.heading("Brand", text="Brand", anchor=CENTER)
        self.__tblItem.heading("Price", text="Price",
                               anchor=CENTER)

    def setTransactionTable(self):
        self.__topLabel1 = tk.Label(self.__transactionTab,
                                    height=2,
                                    font=("Arial", 20),
                                    text="Transaction Information",
                                    bg="aliceblue"
                                    ).pack()
        self.__scroll1 = tk.Scrollbar(self.__transactionTab)
        self.__scroll1.place(x=790, y=70, width=20, height=227)
        self.__tblTransaction = ttk.Treeview(self.__transactionTab, yscrollcommand=self.__scroll1.set)
        self.__tblTransaction.pack()
        self.__scroll1.config(command=self.__tblTransaction.yview)
        self.__tblTransaction["columns"] = ("ID", "Customer ID",
                                            "Customer Name", "Item ID",
                                            "Item Name", "Number",
                                            "Total Price",
                                            "Employee ID",
                                            "Employee Name")
        self.__tblTransaction.column("#0", width=0, stretch=NO)
        self.__tblTransaction.column("ID", anchor=CENTER, width=50)
        self.__tblTransaction.column("Customer ID", anchor=CENTER, width=50)
        self.__tblTransaction.column("Customer Name", anchor=CENTER, width=120)
        self.__tblTransaction.column("Item ID", anchor=CENTER, width=50)
        self.__tblTransaction.column("Item Name", anchor=CENTER, width=120)
        self.__tblTransaction.column("Number", anchor=CENTER, width=55)
        self.__tblTransaction.column("Employee ID", anchor=CENTER, width=50)
        self.__tblTransaction.column("Employee Name", anchor=CENTER, width=120)
        self.__tblTransaction.column("Total Price", anchor=CENTER, width=120)
        self.__tblTransaction.heading("#0", text="", anchor=W)
        self.__tblTransaction.heading("ID", text="ID", anchor=CENTER)
        self.__tblTransaction.heading("Customer ID", text="CID", anchor=CENTER)
        self.__tblTransaction.heading("Customer Name", text="Customer Name", anchor=CENTER)
        self.__tblTransaction.heading("Item ID", text="IID", anchor=CENTER)
        self.__tblTransaction.heading("Item Name", text="Item Name", anchor=CENTER)
        self.__tblTransaction.heading("Number", text="Number", anchor=CENTER)
        self.__tblTransaction.heading("Employee ID", text="EID", anchor=CENTER)
        self.__tblTransaction.heading("Employee Name", text="Employee Name", anchor=CENTER)
        self.__tblTransaction.heading("Total Price", text="Total Price", anchor=CENTER)

    # -------------------------------------GENERAL METHODS-------------------------------------

    def btnExitActionPerformed(self):
        response = messagebox.askyesno("Confirm", "Do you really want to exit?")
        if response == 1:
            self.setVisible(False)

    def searchByIdCallBack(self, id, table):
        if table == 1:
            self.removeAllCustomers()
            customer = Customer(id, "", "", "")
            if self.__customers.__contains__(customer):
                index = self.__customers.index(customer)
                self.showCustomer(self.__customers[index], 0)
        elif table == 2:
            self.removeAllEmployees()
            employee = Employee(id, "", "", "", "")
            if self.__employees.__contains__(employee):
                index = self.__employees.index(employee)
                self.showEmployee(self.__employees[index], 0)
        elif table == 3:
            self.removeAllItems()
            item = Item(id, "", "", "")
            if self.__items.__contains__(item):
                index = self.__items.index(item)
                self.showItem(self.__items[index], 0)
        else:
            self.removeAllTransactions()
            transaction = Transaction(id, "", "", "", "")
            if self.__transactions.__contains__(transaction):
                index = self.__transactions.index(transaction)
                self.showTransaction(self.__transactions[index], 0)

    def searchByFullNameCallBack(self, fullName, table):
        data = []
        if table == 1:
            self.removeAllCustomers()
            for customer in self.__customers:
                if fullName in customer.getFullName():
                    data.append(customer)
            self.showCustomers(data)
            messagebox.showinfo("Message", "Found " + str(len(data)) + " results!")
        elif table == 2:
            self.removeAllEmployees()
            for employee in self.__employees:
                if fullName in employee.getFullName():
                    data.append(employee)
            self.showEmployees(data)
            messagebox.showinfo("Message", "Found " + str(len(data)) + " results!")

    def searchByAddressCallBack(self, address, table):
        data = []
        if table == 1:
            self.removeAllCustomers()
            for customer in self.__customers:
                if address in customer.getAddress():
                    data.append(customer)
            self.showCustomers(data)
            messagebox.showinfo("Message", "Found " + str(len(data)) + " results!")
        elif table == 2:
            self.removeAllEmployees()
            for employee in self.__employees:
                if address in employee.getAddress():
                    data.append(employee)
            self.showEmployees(data)
            messagebox.showinfo("Message", "Found " + str(len(data)) + " results!")

    def searchByPhoneNumberCallBack(self, phoneNumber, table):
        data = []
        if table == 1:
            self.removeAllCustomers()
            for customer in self.__customers:
                if phoneNumber in customer.getPhoneNumber():
                    data.append(customer)
            self.showCustomers(data)
        elif table == 2:
            self.removeAllEmployees()
            for employee in self.__employees:
                if phoneNumber in employee.getPhoneNumber():
                    data.append(employee)
            self.showEmployees(data)

    def sortByIdCallBack(self, table):
        if table == 1:
            data = sorted(self.__customers, key=lambda x: x.getId())
            self.showCustomers(data)
        elif table == 2:
            data = sorted(self.__employees, key=lambda x: x.getId())
            self.showEmployees(data)
        elif table == 3:
            data = sorted(self.__items, key=lambda x: x.getId())
            self.showItems(data)
        else:
            data = sorted(self.__transactions, key=lambda x: x.getId())
            self.showTransactions(data)

    def sortByFullNameCallBack(self, table):
        if table == 1:
            data = sorted(self.__customers, key=lambda x: x.getFullName())
            self.showCustomers(data)
        elif table == 2:
            data = sorted(self.__employees, key=lambda x: x.getFullName())
            self.showEmployees(data)

    def sortByAddressCallBack(self, table):
        if table == 1:
            data = sorted(self.__customers, key=lambda x: x.getAddress())
            self.showCustomers(data)
        elif table == 2:
            data = sorted(self.__employees, key=lambda x: x.getAddress())
            self.showEmployees(data)

    def sortByPhoneNumberCallBack(self, table):
        if table == 1:
            data = sorted(self.__customers, key=lambda x: x.getPhoneNumber())
            self.showCustomers(data)
        elif table == 2:
            data = sorted(self.__employees, key=lambda x: x.getPhoneNumber())
            self.showEmployees(data)

    # -------------------------------------CUSTOMER-------------------------------------

    def btnAddCustomerActionPerformed(self):
        AddCustomerDialog(self, self.__rootWindow, self.__customers)

    def btnEditCustomerActionPerformed(self):
        if not self.__tblCustomer.selection():
            messagebox.showerror("Error", "Please select a row to edit")
        else:
            index = int(self.__tblCustomer.selection()[0])
            customer = self.__customers[index]
            EditCustomerDialog(self, self.__rootWindow, self.__customers, customer)

    def btnRemoveCustomerActionPerformed(self):
        if not self.__tblCustomer.selection():
            messagebox.showerror("Error", "Please select a row to delete")
        else:
            response = messagebox.askyesno("Confirm", "Do you really want to remove this customer?")
            if response == 1:
                try:
                    index = int(self.__tblCustomer.selection()[0])
                    self.__sqlConnection.deleteCustomer(self.__customers[index].getId())
                    self.__customers.pop(index)
                    self.showCustomers(self.__customers)
                except Exception:
                    messagebox.showerror("Error", "Cannot remove this customer!")

    def btnSearchCustomerActionPerformed(self):
        SearchCustomerDialog(self, self.__rootWindow)

    def btnRefreshCustomerActionPerformed(self):
        self.showCustomers(self.__customers)

    def btnSortCustomerActionPerformed(self):
        SortCustomerDialog(self, self.__rootWindow)

    def addCustomerCallBack(self, customer):
        self.__customers.append(customer)
        self.__sqlConnection.insertCustomer(customer)
        self.showCustomer(customer, int(len(self.__customers)) - 1)

    def editCustomerCallBack(self, customer):
        self.__sqlConnection.updateCustomer(customer)
        index = int(self.__tblCustomer.selection()[0])
        self.__customers[index] = customer
        self.__tblCustomer.delete(index)
        self.__tblCustomer.insert(parent="",
                                  index=index,
                                  iid=index,
                                  text="",
                                  values=(
                                      customer.getId(),
                                      customer.getFullName(),
                                      customer.getAddress(),
                                      customer.getPhoneNumber()))

    def removeAllCustomers(self):
        for row in self.__tblCustomer.get_children():
            self.__tblCustomer.delete(row)

    def showCustomers(self, customers):
        self.removeAllCustomers()
        count = 0
        for customer in customers:
            self.showCustomer(customer, count)
            count += 1

    def showCustomer(self, customer, count):
        row = (customer.getId(),
               customer.getFullName(),
               customer.getAddress(),
               customer.getPhoneNumber())
        self.__tblCustomer.insert(parent="", iid=count, index="end", values=row)

    def fixCustomerId(self):
        if len(self.__customers) > 0:
            max = 0
            for customer in self.__customers:
                if max <= customer.getId():
                    max = customer.getId() + 1
            Customer.setCustomerId(max)

    # -------------------------------------EMPLOYEE-------------------------------------

    def btnAddEmployeeActionPerformed(self):
        AddEmployeeDialog(self, self.__rootWindow, self.__employees)

    def btnEditEmployeeActionPerformed(self):
        if not self.__tblEmployee.selection():
            messagebox.showerror("Error", "Please select a row to edit")
        else:
            index = int(self.__tblEmployee.selection()[0])
            employee = self.__employees[index]
            EditEmployeeDialog(self, self.__rootWindow, self.__employees, employee)

    def btnRemoveEmployeeActionPerformed(self):
        if not self.__tblEmployee.selection():
            messagebox.showerror("Error", "Please select a row to delete")
        else:
            response = messagebox.askyesno("Confirm", "Do you really want to remove this employee?")
            if response == 1:
                index = int(self.__tblEmployee.selection()[0])
                self.__sqlConnection.deleteEmployee(self.__employees[index].getId())
                self.__employees.pop(index)
                self.showEmployees(self.__employees)

    def btnSearchEmployeeActionPerformed(self):
        SearchEmployeeDialog(self, self.__rootWindow)

    def btnRefreshEmployeeActionPerformed(self):
        self.showEmployees(self.__employees)

    def btnSortEmployeeActionPerformed(self):
        SortEmployeeDialog(self, self.__rootWindow)

    def addEmployeeCallBack(self, employee):
        self.__employees.append(employee)
        self.__sqlConnection.insertEmployee(employee)
        self.showEmployee(employee, len(self.__employees) - 1)

    def editEmployeeCallBack(self, employee):
        self.__sqlConnection.updateEmployee(employee)
        index = int(self.__tblEmployee.selection()[0])
        self.__employees[index] = employee
        self.__tblEmployee.delete(index)
        self.__tblEmployee.insert(parent="",
                                  index=index,
                                  iid=index,
                                  text="",
                                  values=(
                                      employee.getId(),
                                      employee.getFullName(),
                                      employee.getAddress(),
                                      employee.getPhoneNumber(),
                                      employee.getSalary()
                                  ))

    def searchBySalaryCallBack(self, salary):
        data = []
        for employee in self.__employees:
            if employee.getSalary() == int(salary):
                data.append(employee)
        self.showEmployees(data)

    def sortBySalaryCallBack(self):
        data = sorted(self.__employees, key=lambda x: x.getSalary())
        self.showEmployees(data)

    def removeAllEmployees(self):
        for row in self.__tblEmployee.get_children():
            self.__tblEmployee.delete(row)

    def showEmployees(self, employees):
        self.removeAllEmployees()
        count = 0
        for employee in employees:
            self.showEmployee(employee, count)
            count += 1

    def showEmployee(self, employee, count):
        row = (employee.getId(),
               employee.getFullName(),
               employee.getAddress(),
               employee.getPhoneNumber(),
               employee.getSalary())
        self.__tblEmployee.insert(parent="", iid=count, index="end", values=row)

    def fixEmployeeId(self):
        if len(self.__employees) > 0:
            max = 0
            for employee in self.__employees:
                if max <= employee.getId():
                    max = employee.getId() + 1
            Employee.setEmployeeId(max)

    # -------------------------------------ITEM-------------------------------------

    def btnAddItemActionPerformed(self):
        AddItemDialog(self, self.__rootWindow, self.__items)

    def btnEditItemActionPerformed(self):
        if not self.__tblItem.selection():
            messagebox.showerror("Error", "Please select a row to edit")
        else:
            index = int(self.__tblItem.selection()[0])
            item = self.__items[index]
            EditItemDialog(self, self.__rootWindow, self.__items, item)

    def btnRemoveItemActionPerformed(self):
        if not self.__tblItem.selection():
            messagebox.showerror("Error", "Please select a row to delete")
        else:
            response = messagebox.askyesno("Confirm", "Do you really want to remove this item?")
            if response == 1:
                index = int(self.__tblEmployee.selection()[0])
                self.__sqlConnection.deleteEmployee(self.__employees[index].getId())
                self.__employees.pop(index)
                self.showCustomers(self.__employees)

    def btnSearchItemActionPerformed(self):
        SearchItemDialog(self, self.__rootWindow)

    def btnRefreshItemActionPerformed(self):
        self.showItems(self.__items)

    def btnSortItemActionPerformed(self):
        SortItemDialog(self, self.__rootWindow)

    def sortByNameCallBack(self):
        data = sorted(self.__items, key=lambda x: x.getName())
        self.showItems(data)

    def sortByBrandCallBack(self):
        data = sorted(self.__items, key=lambda x: x.getBrand())
        self.showItems(data)

    def sortByPriceCallBack(self):
        data = sorted(self.__items, key=lambda x: x.getPrice())
        self.showItems(data)

    def addItemCallBack(self, item):
        self.__items.append(item)
        self.__sqlConnection.insertItem(item)
        self.showItem(item, len(self.__items) - 1)

    def editItemCallBack(self, item):
        self.__sqlConnection.updateItem(item)
        index = int(self.__tblItem.selection()[0])
        self.__items[index] = item
        self.__tblItem.delete(index)
        self.__tblItem.insert(parent="",
                              index=index,
                              iid=index,
                              text="",
                              values=(
                                  item.getId(),
                                  item.getName(),
                                  item.getBrand(),
                                  item.getPrice()))

    def searchByNameCallBack(self, name):
        self.removeAllItems()
        data = []
        for item in self.__items:
            if name in item.getName():
                data.append(item)
        self.showItems(data)
        messagebox.showinfo("Message", "Found " + str(len(data)) + " results!")

    def searchByBrandCallBack(self, brand):
        self.removeAllItems()
        data = []
        for item in self.__items:
            if brand in item.getBrand():
                data.append(item)
        self.showItems(data)

    def removeAllItems(self):
        for row in self.__tblItem.get_children():
            self.__tblItem.delete(row)

    def showItems(self, items):
        self.removeAllItems()
        count = 0
        for item in items:
            self.showItem(item, count)
            count += 1

    def showItem(self, item, count):
        row = (item.getId(),
               item.getName(),
               item.getBrand(),
               item.getPrice())
        self.__tblItem.insert(parent="", iid=count, index="end", values=row)

    def fixItemId(self):
        if len(self.__items) > 0:
            max = 0
            for item in self.__items:
                if max <= item.getId():
                    max = item.getId() + 1
            Item.setItemId(max)

    # -------------------------------------TRANSACTION-------------------------------------

    def btnAddTransactionActionPerformed(self):
        AddTransactionDialog(self, self.__rootWindow, self.__customers, self.__items, self.__employees)

    def btnEditTransactionActionPerformed(self):
        if not self.__tblTransaction.selection():
            messagebox.showerror("Error", "Please select a row to edit")
        else:
            index = int(self.__tblTransaction.selection()[0])
            transaction = self.__transactions[index]
            EditTransactionDialog(self, self.__rootWindow, self.__customers, self.__items, self.__employees,
                                  transaction)

    def btnRemoveTransactionActionPerformed(self):
        if not self.__tblTransaction.selection():
            messagebox.showerror("Error", "Please select a row to delete")
        else:
            response = messagebox.askyesno("Confirm", "Do you really want to remove this item?")
            if response == 1:
                index = int(self.__tblTransaction.selection()[0])
                self.__sqlConnection.deleteTransaction(self.__transactions[index].getId())
                self.__transactions.pop(index)
                self.showTransactions(self.__transactions)

    def btnSearchTransactionActionPerformed(self):
        SearchTransactionDialog(self, self.__rootWindow)

    def btnRefreshTransactionActionPerformed(self):
        self.showTransactions(self.__transactions)

    def btnSortTransactionActionPerformed(self):
        SortTransactionDialog(self, self.__rootWindow)

    def addTransactionCallBack(self, transaction):
        self.__transactions.append(transaction)
        self.__sqlConnection.insertTransaction(transaction)
        self.showTransaction(transaction, len(self.__transactions) - 1)

    def editTransactionCallBack(self, transaction):
        self.__sqlConnection.updateTransaction(transaction)
        index = int(self.__tblTransaction.selection()[0])
        self.__transactions[index] = transaction
        self.__tblTransaction.delete(index)
        self.__tblTransaction.insert(parent="",
                                     index=index,
                                     iid=index,
                                     text="",
                                     values=(transaction.getId(),
                                             transaction.getCustomer().getId(),
                                             transaction.getCustomer().
                                             getFullName(),
                                             transaction.getItem().getId(),
                                             transaction.getItem().getName(),
                                             transaction.getNumber(),
                                             transaction.getTotalPrice(),
                                             transaction.getEmployee().getId(),
                                             transaction.getEmployee().
                                             getFullName()
                                             ))

    def searchByCustomerIdCallBack(self, customerId):
        self.removeAllTransactions()
        data = []
        for transaction in self.__transactions:
            if transaction.getCustomer().getId() == int(customerId):
                data.append(transaction)
        self.showTransactions(data)

    def searchByItemIdCallBack(self, itemId):
        self.removeAllTransactions()
        data = []
        for transaction in self.__transactions:
            if transaction.getItem().getId() == int(itemId):
                data.append(transaction)
        self.showTransactions(data)

    def searchByEmployeeIdCallBack(self, employeeId):
        self.removeAllTransactions()
        data = []
        for transaction in self.__transactions:
            if transaction.getEmployee().getId() == int(employeeId):
                data.append(transaction)
        self.showTransactions(data)

    def sortByCustomerIdCallBack(self):
        data = sorted(self.__transactions, key=lambda x: x.getCustomer().getId())
        self.showTransactions(data)

    def sortByItemIdCallBack(self):
        data = sorted(self.__transactions, key=lambda x: x.getItem().getId())
        self.showTransactions(data)

    def sortByEmployeeIdCallBack(self):
        data = sorted(self.__transactions, key=lambda x: x.getEmployee().getId())
        self.showTransactions(data)

    def removeAllTransactions(self):
        for row in self.__tblTransaction.get_children():
            self.__tblTransaction.delete(row)

    def showTransactions(self, transactions):
        self.removeAllTransactions()
        count = 0
        for transaction in transactions:
            self.showTransaction(transaction, count)
            count += 1

    def showTransaction(self, transaction, count):
        row = (transaction.getId(),
               transaction.getCustomer().getId(),
               transaction.getCustomer().getFullName(),
               transaction.getItem().getId(),
               transaction.getItem().getName(),
               transaction.getNumber(),
               transaction.getTotalPrice(),
               transaction.getEmployee().getId(),
               transaction.getEmployee().getFullName()
               )
        self.__tblTransaction.insert(parent="", iid=count, index="end", values=row)

    def fixTransactionId(self):
        if len(self.__transactions) > 0:
            max = 0
            for transaction in self.__transactions:
                if max <= transaction.getId():
                    max = transaction.getId() + 1
            Transaction.setTransactionId(max)
