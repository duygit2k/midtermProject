class Item:

    itemId = 1

    def __init__(self, id, name, brand, price) -> None:
        self.setId(id)
        self.setName(name)
        self.setBrand(brand)
        self.setPrice(price)

    def setItemId(newId):
        Item.itemId = newId

    def fixId(self):
        self.__id = Item.itemId
        Item.itemId += 1

    def setId(self, id):
        if len(id) > 0:
            self.__id = int(id)
        else:
            self.__id = ""

    def setName(self, name):
        if len(name) > 0:
            self.__name = name

    def setBrand(self, brand):
        if len(brand) > 0:
            self.__brand = brand

    def setPrice(self, price):
        if len(price) > 0:
            self.__price = int(price)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getBrand(self):
        return self.__brand

    def getPrice(self):
        return self.__price

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Item):
            if self.__id != "":
                return self.__id == o.__id
            else:
                return self.__name == o.__name and self.__brand == o.__brand
        return False


    def __hash__(self) -> int:
        if self.__id != "":
            return hash(self.__id)
        else:
            return hash((self.__name, self.__brand))

