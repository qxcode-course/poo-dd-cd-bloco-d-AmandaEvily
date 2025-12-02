class Phone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    

class Contact: 
    def __init__(self, name: str) -> None:
        self.__name: str = name 
        self.__phone = Phone
        self.__isFavorite: bool

    def getName(self):
        return self.__name
    
    
