from model.Customer import Customer
from model.Employee import Employee
from model.Item import Item

class Transaction:

    transactionId = 1

    def __init__(self, id, customer, item, number, employee) -> None:
        self.setId(id)
        self.setCustomer(customer)
        self.setItem(item)
        self.setNumber(number)
        self.setTotalPrice()
        self.setEmployee(employee)

    def setTransactionId(newId):
        Transaction.transactionId = newId

    def fixId(self):
        self.__id = Transaction.transactionId
        Transaction.transactionId += 1

    def setId(self, id):
        if len(id) > 0:
            self.__id = int(id)

    def setCustomer(self, customer):
        if isinstance(customer, Customer):
            self.__customer = customer
        else:
            self.__customer = ""

    def setEmployee(self, employee):
        if isinstance(employee, Employee):
            self.__employee = employee
        else:
            self.__employee = ""

    def setItem(self, item):
        if isinstance(item, Item):
            self.__item = item
        else:
            self.__item = ""

    def setTotalPrice(self):
        if isinstance(self.__item, Item):
            self.__totalPrice = self.__item.getPrice() * self.__number

    def setNumber(self, number):
        if len(number) > 0:
            self.__number = int(number)

    def getId(self):
        return self.__id

    def getCustomer(self):
        return self.__customer

    def getEmployee(self):
        return self.__employee

    def getItem(self):
        return self.__item

    def getNumber(self):
        return self.__number

    def getTotalPrice(self):
        return self.__totalPrice

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Transaction):
            return self.__id == o.__id
        return False

    def __hash__(self) -> int:
        return hash(self.__id)

