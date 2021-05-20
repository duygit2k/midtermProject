import mysql.connector

from model.Customer import Customer
from model.Employee import Employee
from model.Item import Item
from model.Transaction import Transaction


class SQLConnection:
    def __init__(self, database):
        self.__database = database
        self.__cursor = self.__database.cursor()

    def readCustomerTable(self):
        self.__customers = []
        sql = "SELECT * FROM customers"
        self.__cursor.execute(sql)
        records = self.__cursor.fetchall()
        for row in records:
            customer = Customer(str(row[0]), row[1], row[2], row[3])
            self.__customers.append(customer)
        return self.__customers

    def readItemTable(self):
        self.__items = []
        sql = "SELECT * FROM items"
        self.__cursor.execute(sql)
        records = self.__cursor.fetchall()
        for row in records:
            item = Item(str(row[0]), row[1], row[2], str(row[3]))
            self.__items.append(item)
        return self.__items

    def readTransactionTable(self):
        self.__transactions = []
        sql = "SELECT * FROM transactions"
        self.__cursor.execute(sql)
        records = self.__cursor.fetchall()
        for row in records:
            id = str(row[0])
            customerId = str(row[1])
            itemId = str(row[3])
            number = str(row[5])
            employeeId = str(row[7])
            cIndex = self.__customers.index(Customer(customerId, "", "", ""))
            iIndex = self.__items.index(Item(itemId, "", "", ""))
            eIndex = self.__employees.\
                index(Employee(employeeId, "", "", "", ""))
            transaction = Transaction(id, self.__customers[cIndex],
                                      self.__items[iIndex], number,
                                      self.__employees[eIndex])
            self.__transactions.append(transaction)
        return self.__transactions

    def readEmployeeTable(self):
        self.__employees = []
        sql = "SELECT * FROM employees"
        self.__cursor.execute(sql)
        records = self.__cursor.fetchall()
        for row in records:
            employee = Employee(str(row[0]), row[1], row[2], row[3],
                                str(row[4]))
            self.__employees.append(employee)
        return self.__employees

    def insertCustomer(self, customer):
        sql = "INSERT INTO customers (id, fullName, address, phoneNumber)" \
              " VALUES (%s, %s, %s, %s)"
        val = (customer.getId(), customer.getFullName(), customer.getAddress(),
               customer.getPhoneNumber())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def insertItem(self, item):
        sql = "INSERT INTO items (id, name, brand, price)" \
              " VALUES (%s, %s, %s, %s)"
        val = (item.getId(), item.getName(), item.getBrand(), item.getPrice())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def insertEmployee(self, employee):
        sql = "INSERT INTO employees" \
              " (id, fullName, address, phoneNumber, salary)" \
              " VALUES (%s, %s, %s, %s, %s)"
        val = (employee.getId(), employee.getFullName(), employee.getAddress(),
               employee.getPhoneNumber(), employee.getSalary())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def insertTransaction(self, transaction):
        sql = "INSERT INTO transactions (id, customerId, customerName, itemId," \
              " itemName, number, totalPrice, employeeId, employeeName) VALUES" \
              " (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (transaction.getId(), transaction.getCustomer().getId(),
               transaction.getCustomer().getFullName(),
               transaction.getItem().getId(), transaction.getItem().getName(),
               transaction.getNumber(),
               transaction.getTotalPrice(),
               transaction.getEmployee().getId(),
               transaction.getEmployee().getFullName())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def deleteCustomer(self, customerId):
        sql = "DELETE FROM customers WHERE id = %s"
        val = (customerId,)
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def deleteItem(self, itemId):
        sql = "DELETE FROM items WHERE id = %s"
        val = (itemId,)
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def deleteEmployee(self, employeeId):
        sql = "DELETE FROM employees WHERE id = %s"
        val = (employeeId,)
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def deleteTransaction(self, transactionId):
        sql = "DELETE FROM transactions WHERE id = %s"
        val = (transactionId,)
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def updateCustomer(self, customer):
        sql = "UPDATE customers SET fullName = %s, address = %s," \
              " phoneNumber = %s WHERE id = %s"
        val = (customer.getFullName(), customer.getAddress(),
               customer.getPhoneNumber(), customer.getId())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def updateEmployee(self, employee):
        sql = "UPDATE employees SET fullName = %s, address = %s," \
              " phoneNumber = %s, salary = %s WHERE id = %s"
        val = (employee.getFullName(), employee.getAddress(),
               employee.getPhoneNumber(), employee.getSalary(),
               employee.getId())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def updateItem(self, item):
        sql = "UPDATE items SET name = %s, brand = %s, price = %s WHERE id = %s"
        val = (item.getName(), item.getBrand(), item.getPrice(), item.getId())
        self.__cursor.execute(sql, val)
        self.__database.commit()

    def updateTransaction(self, transaction):
        sql = "UPDATE transactions SET customerId = %s," \
              " customerName = %s, itemId = %s, itemName = %s," \
              " number = %s, totalPrice = %s, employeeId = %s," \
              " employeeName = %s WHERE id = %s"
        val = (transaction.getCustomer().getId(),
               transaction.getCustomer().getFullName(),
               transaction.getItem().getId(),
               transaction.getItem().getName(), transaction.getNumber(),
               transaction.getTotalPrice(),
               transaction.getEmployee().getId(),
               transaction.getEmployee().getFullName(),
               transaction.getId())
        self.__cursor.execute(sql, val)
        self.__database.commit()