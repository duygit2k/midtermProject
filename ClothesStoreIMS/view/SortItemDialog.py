import tkinter as tk

class SortItemDialog:

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
        self.__screenWidth = self.__sortItemWindow.winfo_screenwidth()
        self.__screenHeight = self.__sortItemWindow.winfo_screenheight()
        self.__positionTop = int(self.__screenHeight / 2 -
                                 self.__windowHeight / 2)
        self.__positionRight = int(self.__screenWidth / 2 -
                                   self.__windowWidth / 2)
        self.__sortItemWindow.geometry(f'{self.__windowWidth}'
                                             f'x{self.__windowHeight}'
                                             f'+{self.__positionRight}'
                                             f'+{self.__positionTop}')

    def setWindow(self):
        self.__sortItemWindow = tk.Toplevel(self.__rootWindow)
        self.__sortItemWindow.config(bg="aliceblue")
        self.__sortItemWindow.title("Sort Item")
        self.__topLabel = tk.Label(self.__sortItemWindow,
                                   height=3,
                                   font=("Arial", 20),
                                   text="Sort item",
                                   bg="aliceblue"
                                   ).pack()
        self.__sortItemWindow.grab_set()

    def setButtons(self):
        self.__radio1 = tk.Radiobutton(self.__sortItemWindow,
                                       text="ID",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=0)
        self.__radio1.place(x=100, y=100)
        self.__radio2 = tk.Radiobutton(self.__sortItemWindow,
                                       text="Name",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=1)
        self.__radio2.place(x=100, y=140)
        self.__radio3 = tk.Radiobutton(self.__sortItemWindow,
                                       text="Brand",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=2)
        self.__radio3.place(x=100, y=180)
        self.__radio4 = tk.Radiobutton(self.__sortItemWindow,
                                       text="Price",
                                       variable=self.__choice,
                                       bg="aliceblue",
                                       value=3)
        self.__radio4.place(x=100, y=220)
        self.__btnSearch = tk.Button(self.__sortItemWindow, text="Sort",
                                     bg="lightyellow",
                                     command=self.btnSortActionPerformed).place(
            x=100, y=300, width=50, height=35)
        self.__btnCancel = tk.Button(self.__sortItemWindow, text="Cancel",
                                     bg="lightyellow",
                                     command=self.btnCancelActionPerformed).place(
            x=250, y=300, width=50, height=35)

    def btnSortActionPerformed(self):
        if self.__choice.get() == 0:
            self.__parent.sortByIdCallBack(3)
        elif self.__choice.get() == 1:
            self.__parent.sortByNameCallBack()
        elif self.__choice.get() == 2:
            self.__parent.sortByBrandCallBack()
        else:
            self.__parent.sortByPriceCallBack()


    def btnCancelActionPerformed(self):
        self.__sortItemWindow.destroy()