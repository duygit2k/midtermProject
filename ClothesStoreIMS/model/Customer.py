from model.Person import Person

class Customer(Person):

    customerId = 1

    def __init__(self, id, fullName, address, phoneNumber) -> None:
        super().__init__(fullName, address, phoneNumber)
        self.setId(id)

    def setCustomerId(newId):
        Customer.customerId = newId

    def setId(self, id):
        if len(id) > 0:
            self.__id = int(id)
        else:
            self.__id = ""

    def fixId(self):
        self.__id = Customer.customerId
        Customer.customerId += 1

    def getId(self):
        return self.__id

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Customer):
            return self.__id == o.__id
        else:
            return super().__eq__(o)

    def __hash__(self) -> int:
        return hash(self.__id)









