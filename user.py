


class User:
    name = None
    email = None
    age = 0
    address = None

    def __init__(self, namev, emailv, agev, addressv) -> None:
        self.name = namev
        self.email = emailv
        self.age = agev
        self.address = addressv

    def talk(self):
        return f"Hello, I am  {self.name}"
    
    def saysAddress(self):
        return f"Sree is from {self.address} It is in India"

    
    
        
