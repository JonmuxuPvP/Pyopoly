
class Player:

    def __init__(self, name, startingMoney):
        self.name = name
        self.money = startingMoney
        self.pos = 0 # To avoid looping through the board
        self.properties = {}
        self.diceCount = 0
        self.jailCount = 0
    
    def calcTotal(self):
        # Sum money variable with total of properties money (using for loop in self.properties)
        raise NotImplementedError