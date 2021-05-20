import tkinter as tk
from tkinter import messagebox

class SearchEmployeeDialog:

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
        self.__screenWidth = self.__searchEmployeeWindow.winfo_screenwidth()
        self.__screenHeight = self.__searchEmployeeWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__searchEmployeeWindow.geometry(f'{self.__windowWidth}'
                                             f'x{self.__windowHeight}'
                                             f'+{self.__positionRight}'
                                             f'+{self.__positionTop}')

    def setWindow(self):
        self.__searchEmployeeWindow = tk.Toplevel(self.__rootWindow)
        self.__searchEmployeeWindow.config(bg="aliceblue")
        self.__searchEmployeeWindow.title("Search Employee")
        self.__topLabel = tk.Label(self.__searchEmployeeWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Search customer",
                                   bg="aliceblue"
                                   ).pack()
        self.__searchEmployeeWindow.grab_set()

    def setTextFields(self):
        self.__txtId = tk.Entry(self.__searchEmployeeWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__txtFullName = tk.Entry(self.__searchEmployeeWindow)
        self.__txtFullName.place(x=125, y=140, width=240, height=25)
        self.__txtAddress = tk.Entry(self.__searchEmployeeWindow)
        self.__txtAddress.place(x=125, y=180, width=240, height=25)
        self.__txtPhoneNumber = tk.Entry(self.__searchEmployeeWindow)
        self.__txtPhoneNumber.place(x=125, y=220, width=240, height=25)
        self.__txtSalary = tk.Entry(self.__searchEmployeeWindow)
        self.__txtSalary.place(x=125, y=260, width=240, height=25)

    def setButtons(self):
        self.__radio1 = tk.Radiobutton(self.__searchEmployeeWindow,
                                       text="ID:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command = self.radioButtonsActionPerformed,
                                       value=0)
        self.__radio1.place(x=10, y=100)
        self.__radio2 = tk.Radiobutton(self.__searchEmployeeWindow,
                                       text="Full Name:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=1)
        self.__radio2.place(x=10, y=140)
        self.__radio3 = tk.Radiobutton(self.__searchEmployeeWindow,
                                       text="Address:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=2)
        self.__radio3.place(x=10, y=180)
        self.__radio4 = tk.Radiobutton(self.__searchEmployeeWindow,
                                       text="Phone Number:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=3)
        self.__radio4.place(x=10, y=220)
        self.__radio5 = tk.Radiobutton(self.__searchEmployeeWindow,
                                       text="Salary:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=4)
        self.__radio5.place(x=10, y=260)
        self.__btnSearch = tk.Button(self.__searchEmployeeWindow, text="Search",
                                     bg="lightyellow",
                                     command=self.btnSearchActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__searchEmployeeWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def radioButtonsActionPerformed(self):
        textFields = [self.__txtId, self.__txtFullName, self.__txtAddress,
                      self.__txtPhoneNumber, self.__txtSalary]
        for x in textFields:
            if self.__choice.get() != textFields.index(x):
                x.config(state = "readonly")
            else:
                x.config(state = "normal")

    def btnSearchActionPerformed(self):
        id = self.__txtId.get()
        fullName = self.__txtFullName.get()
        address = self.__txtAddress.get()
        phoneNumber = self.__txtPhoneNumber.get()
        salary = self.__txtSalary.get()
        if self.__choice.get() == 0:
            if len(id) > 0:
                self.__parent.searchByIdCallBack(id, 2)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 1:
            if len(fullName) > 0:
                self.__parent.searchByFullNameCallBack(fullName, 2)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 2:
            if len(address) > 0:
                self.__parent.searchByAddressCallBack(address, 2)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 3:
            if len(phoneNumber) > 0:
                self.__parent.searchByPhoneNumberCallBack(phoneNumber, 2)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        else:
            if len(salary) > 0:
                self.__parent.searchBySalaryCallBack(salary)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")


    def btnCancelActionPerformed(self):
        self.__searchEmployeeWindow.destroy()
