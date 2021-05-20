import tkinter as tk
from tkinter import messagebox

from model.Customer import Customer


class SortEmployeeDialog:

    def __init__(self, parent, rootWindow) -> None:
        self.__parent = parent
        self.__rootWindow = rootWindow
        self.__choice = tk.IntVar()
        self.__choice.set(0)
        self.setComponents()
        self.setLocation()

    def setComponents(self):
        self.setWindow()
        self.setButtons()

    def setLocation(self):
        self.__windowWidth = 400
        self.__windowHeight = 400
        self.__screenWidth = self.__sortEmployeeWindow.winfo_screenwidth()
        self.__screenHeight = self.__sortEmployeeWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__sortEmployeeWindow.geometry(f'{self.__windowWidth}'
                                             f'x{self.__windowHeight}'
                                             f'+{self.__positionRight}'
                                             f'+{self.__positionTop}')

    def setWindow(self):
        self.__sortEmployeeWindow = tk.Toplevel(self.__rootWindow)
        self.__sortEmployeeWindow.config(bg="aliceblue")
        self.__sortEmployeeWindow.title("Sort Customer")
        self.__topLabel = tk.Label(self.__sortEmployeeWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Sort employee",
                                   bg="aliceblue"
                                   ).pack()
        self.__sortEmployeeWindow.grab_set()

    def setButtons(self):
        self.__radio1 = tk.Radiobutton(self.__sortEmployeeWindow,
                                       text="ID",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=0)
        self.__radio1.place(x=100, y=100)
        self.__radio2 = tk.Radiobutton(self.__sortEmployeeWindow,
                                       text="Full Name",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=1)
        self.__radio2.place(x=100, y=140)
        self.__radio3 = tk.Radiobutton(self.__sortEmployeeWindow,
                                       text="Address",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=2)
        self.__radio3.place(x=100, y=180)
        self.__radio4 = tk.Radiobutton(self.__sortEmployeeWindow,
                                       text="Phone Number",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=3)
        self.__radio4.place(x=100, y=220)
        self.__radio5 = tk.Radiobutton(self.__sortEmployeeWindow,
                                       text="Salary",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=4)
        self.__radio5.place(x=100, y=260)
        self.__btnSearch = tk.Button(self.__sortEmployeeWindow, text="Sort",
                                     bg="lightyellow",
                                     command=self.btnSortActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__sortEmployeeWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnSortActionPerformed(self):
        if self.__choice.get() == 0:
            self.__parent.sortByIdCallBack(2)
        elif self.__choice.get() == 1:
            self.__parent.sortByFullNameCallBack(2)
        elif self.__choice.get() == 2:
            self.__parent.sortByAddressCallBack(2)
        elif self.__choice.get() == 3:
            self.__parent.sortByPhoneNumberCallBack(2)
        else:
            self.__parent.sortBySalaryCallBack()


    def btnCancelActionPerformed(self):
        self.__sortEmployeeWindow.destroy()