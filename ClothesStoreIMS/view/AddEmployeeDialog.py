import tkinter as tk
from tkinter import messagebox

from model.Employee import Employee
from model.Person import Person


class AddEmployeeDialog:

    def __init__(self, parent, rootWindow, employees) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
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
        self.__screenWidth = self.__addEmployeeWindow.winfo_screenwidth()
        self.__screenHeight = self.__addEmployeeWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__addEmployeeWindow.geometry(f'{self.__windowWidth}'
                                          f'x{self.__windowHeight}'
                                          f'+{self.__positionRight}'
                                          f'+{self.__positionTop}')

    def setWindow(self):
        self.__addEmployeeWindow = tk.Toplevel(self.__rootWindow)
        self.__addEmployeeWindow.config(bg="aliceblue")
        self.__addEmployeeWindow.title("Add Employee")
        self.__topLabel = tk.Label(self.__addEmployeeWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Add new employee",
                                   bg="aliceblue"
                                   ).pack()
        self.__addEmployeeWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__addEmployeeWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__addEmployeeWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__addEmployeeWindow,
                                 text="Full Name:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtFullName = tk.Entry(self.__addEmployeeWindow)
        self.__txtFullName.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__addEmployeeWindow,
                                 text="Address:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtAddress = tk.Entry(self.__addEmployeeWindow)
        self.__txtAddress.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__addEmployeeWindow,
                                 text="Phone Number:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtPhoneNumber = tk.Entry(self.__addEmployeeWindow)
        self.__txtPhoneNumber.place(x=125, y=220, width=240, height=25)
        self.__label5 = tk.Label(self.__addEmployeeWindow,
                                 text="Salary:",
                                 bg="aliceblue"
                                 ).place(x=35, y=260)
        self.__txtSalary = tk.Entry(self.__addEmployeeWindow)
        self.__txtSalary.place(x=125, y=260, width=240, height=25)

    def setButtons(self):
        self.__btnAdd = tk.Button(self.__addEmployeeWindow, text="Add",
                                  bg="lightyellow",
                                  command=self.btnAddActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__addEmployeeWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnAddActionPerformed(self):
        fullName = self.__txtFullName.get()
        address = self.__txtAddress.get()
        phoneNumber = self.__txtPhoneNumber.get()
        salary = self.__txtSalary.get()
        if len(fullName) > 0 and len(address) > 0 and len(phoneNumber) > 0:
            try:
                employee = Person(fullName, address, phoneNumber)
                if self.__employees.__contains__(employee):
                    messagebox.showerror("Error", "Employee information already exists!")
                else:
                    employee = Employee("", fullName, address, phoneNumber, salary)
                    employee.fixId()
                    self.__parent.addEmployeeCallBack(employee)
                    messagebox.showinfo("Success", "A new customer has been added")
                    self.showDefaultText()
            except Exception:
                messagebox.showerror("Error", "Invalid information format!")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__addEmployeeWindow.destroy()

    def showDefaultText(self):
        self.__txtId.config(state="normal")
        self.__txtId.delete(0, tk.END)
        self.__txtId.insert(0, Employee.employeeId)
        self.__txtId.config(state="readonly")
        self.__txtFullName.delete(0, tk.END)
        self.__txtFullName.insert(0, "")
        self.__txtAddress.delete(0, tk.END)
        self.__txtAddress.insert(0, "")
        self.__txtPhoneNumber.delete(0, tk.END)
        self.__txtPhoneNumber.insert(0, "")
        self.__txtSalary.delete(0, tk.END)
        self.__txtSalary.insert(0, "")
