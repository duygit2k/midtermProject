import tkinter as tk
from tkinter import messagebox
from model.Employee import Employee


class EditEmployeeDialog:

    def __init__(self, parent, rootWindow, employees, employee) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__customers = employees
        self.__employee = employee
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
        self.__screenWidth = self.__editEmployeeWindow.winfo_screenwidth()
        self.__screenHeight = self.__editEmployeeWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__editEmployeeWindow.geometry(f'{self.__windowWidth}'
                                          f'x{self.__windowHeight}'
                                          f'+{self.__positionRight}'
                                          f'+{self.__positionTop}')

    def setWindow(self):
        self.__editEmployeeWindow = tk.Toplevel(self.__rootWindow)
        self.__editEmployeeWindow.config(bg="aliceblue")
        self.__editEmployeeWindow.title("Edit Employee")
        self.__topLabel = tk.Label(self.__editEmployeeWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Edit Employee",
                                   bg="aliceblue"
                                   ).pack()
        self.__editEmployeeWindow.grab_set()

    def setTextFields(self):
        self.__label1 = tk.Label(self.__editEmployeeWindow,
                                 text="ID:",
                                 bg="aliceblue"
                                 ).place(x=35, y=100)
        self.__txtId = tk.Entry(self.__editEmployeeWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__label2 = tk.Label(self.__editEmployeeWindow,
                                 text="Full Name:",
                                 bg="aliceblue"
                                 ).place(x=35, y=140)
        self.__txtFullName = tk.Entry(self.__editEmployeeWindow)
        self.__txtFullName.place(x=125, y=140, width=240, height=25)
        self.__label3 = tk.Label(self.__editEmployeeWindow,
                                 text="Address:",
                                 bg="aliceblue"
                                 ).place(x=35, y=180)
        self.__txtAddress = tk.Entry(self.__editEmployeeWindow)
        self.__txtAddress.place(x=125, y=180, width=240, height=25)
        self.__label4 = tk.Label(self.__editEmployeeWindow,
                                 text="Phone Number:",
                                 bg="aliceblue"
                                 ).place(x=35, y=220)
        self.__txtPhoneNumber = tk.Entry(self.__editEmployeeWindow)
        self.__txtPhoneNumber.place(x=125, y=220, width=240, height=25)
        self.__label5 = tk.Label(self.__editEmployeeWindow,
                                 text="Salary:",
                                 bg="aliceblue"
                                 ).place(x=35, y=260)
        self.__txtSalary = tk.Entry(self.__editEmployeeWindow)
        self.__txtSalary.place(x=125, y=260, width=240, height=25)

    def setButtons(self):
        self.__btnEdit = tk.Button(self.__editEmployeeWindow, text="Edit",
                                   bg="lightyellow",
                                   command=self.btnEditActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__editEmployeeWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnEditActionPerformed(self):
        fullName = self.__txtFullName.get()
        address = self.__txtAddress.get()
        phoneNumber = self.__txtPhoneNumber.get()
        salary = self.__txtSalary.get()
        if len(fullName) > 0 and len(address) > 0 and len(phoneNumber) > 0:
            try:
                employee = Employee(str(self.__employee.getId()), fullName, address, phoneNumber, salary)
                self.__parent.editEmployeeCallBack(employee)
                self.__editEmployeeWindow.destroy()
                messagebox.showinfo("Success", "Employee information has been edited")
            except Exception:
                messagebox.showerror("Error", "Invalid information format!")
        else:
            messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__editEmployeeWindow.destroy()

    def showDefaultText(self):
        self.__txtId.insert(0, self.__employee.getId())
        self.__txtId.config(state="readonly")
        self.__txtFullName.insert(0, self.__employee.getFullName())
        self.__txtAddress.insert(0, self.__employee.getAddress())
        self.__txtPhoneNumber.insert(0, self.__employee.getPhoneNumber())
        self.__txtSalary.insert(0, self.__employee.getSalary())