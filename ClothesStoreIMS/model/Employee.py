from model.Person import Person

class Employee(Person):

    employeeId = 1

    def __init__(self, id, fullName, address, phoneNumber, salary) -> None:
        super().__init__(fullName, address, phoneNumber)
        self.setId(id)
        self.setSalary(salary)

    def setEmployeeId(newId):
        Employee.employeeId = newId

    def setId(self, id):
        if len(id) > 0:
            self.__id = int(id)
        else:
            self.__id = ""

    def setSalary(self, salary):
        if len(salary) > 0:
            self.__salary = int(salary)
        else:
            self.__salary = ""

    def fixId(self):
        self.__id = Employee.employeeId
        Employee.employeeId += 1

    def getId(self):
        return self.__id

    def getSalary(self):
        return self.__salary

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Employee):
            return self.__id == o.__id
        else:
            return super().__eq__(o)

    def __hash__(self) -> int:
        return hash(self.__id)






