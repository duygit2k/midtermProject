
class Person:

    def __init__(self, fullName, address, phoneNumber) -> None:
        self.setFullName(fullName)
        self.setAddress(address)
        self.setPhoneNumber(phoneNumber)

    def setFullName(self, fullName):
        if len(fullName) > 0:
            self.__fullName = fullName

    def setAddress(self, address):
        if len(address) > 0:
            self.__address = address

    def setPhoneNumber(self, phoneNumber):
        if len(phoneNumber) > 0:
            self.__phoneNumber = phoneNumber

    def getFullName(self):
        return self.__fullName

    def getAddress(self):
        return self.__address

    def getPhoneNumber(self):
        return self.__phoneNumber

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Person):
            return self.__phoneNumber == o.__phoneNumber


    def __hash__(self) -> int:
        return hash(self.__phoneNumber)



