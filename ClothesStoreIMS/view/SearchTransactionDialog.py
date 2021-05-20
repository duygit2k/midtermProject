import tkinter as tk
from tkinter import messagebox


class SearchTransactionDialog:

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
        self.__screenWidth = self.__searchTransactionWindow.winfo_screenwidth()
        self.__screenHeight = self.__searchTransactionWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__searchTransactionWindow.geometry(f'{self.__windowWidth}'
                                                f'x{self.__windowHeight}'
                                                f'+{self.__positionRight}'
                                                f'+{self.__positionTop}')

    def setWindow(self):
        self.__searchTransactionWindow = tk.Toplevel(self.__rootWindow)
        self.__searchTransactionWindow.config(bg="aliceblue")
        self.__searchTransactionWindow.title("Search Transaction")
        self.__topLabel = tk.Label(self.__searchTransactionWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Search transaction",
                                   bg="aliceblue"
                                   ).pack()
        self.__searchTransactionWindow.grab_set()

    def setTextFields(self):
        self.__txtId = tk.Entry(self.__searchTransactionWindow)
        self.__txtId.place(x=125, y=100, width=240, height=25)
        self.__txtCustomerId = tk.Entry(self.__searchTransactionWindow)
        self.__txtCustomerId.place(x=125, y=140, width=240, height=25)
        self.__txtItemId = tk.Entry(self.__searchTransactionWindow)
        self.__txtItemId.place(x=125, y=180, width=240, height=25)
        self.__txtEmployeeId = tk.Entry(self.__searchTransactionWindow)
        self.__txtEmployeeId.place(x=125, y=220, width=240, height=25)

    def setButtons(self):
        self.__radio1 = tk.Radiobutton(self.__searchTransactionWindow,
                                       text="ID:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=0)
        self.__radio1.place(x=10, y=100)
        self.__radio2 = tk.Radiobutton(self.__searchTransactionWindow,
                                       text="Customer ID:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=1)
        self.__radio2.place(x=10, y=140)
        self.__radio3 = tk.Radiobutton(self.__searchTransactionWindow,
                                       text="Item ID:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=2)
        self.__radio3.place(x=10, y=180)
        self.__radio4 = tk.Radiobutton(self.__searchTransactionWindow,
                                       text="Employee ID:",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       command=self.radioButtonsActionPerformed,
                                       value=3)
        self.__radio4.place(x=10, y=220)
        self.__btnSearch = tk.Button(self.__searchTransactionWindow, text="Search",
                                     bg="lightyellow",
                                     command=self.btnSearchActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__searchTransactionWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def radioButtonsActionPerformed(self):
        textFields = [self.__txtId, self.__txtCustomerId, self.__txtItemId,
                      self.__txtEmployeeId]
        for x in textFields:
            if self.__choice.get() != textFields.index(x):
                x.config(state="readonly")
            else:
                x.config(state="normal")

    def btnSearchActionPerformed(self):
        id = self.__txtId.get()
        customerId = self.__txtCustomerId.get()
        itemId = self.__txtItemId.get()
        employeeId = self.__txtEmployeeId.get()
        if self.__choice.get() == 0:
            if len(id) > 0:
                self.__parent.searchByIdCallBack(id, 4)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 1:
            if len(customerId) > 0:
                self.__parent.searchByCustomerIdCallBack(customerId)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        elif self.__choice.get() == 2:
            if len(itemId) > 0:
                self.__parent.searchByItemIdCallBack(itemId)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")
        else:
            if len(employeeId) > 0:
                self.__parent.searchByEmployeeIdCallBack(employeeId)
            else:
                messagebox.showerror("Error", "Input fields cannot be left blank!")

    def btnCancelActionPerformed(self):
        self.__searchTransactionWindow.destroy()
