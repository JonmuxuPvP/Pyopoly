
class Bank:

    def __init__(self):
        self.properties = [] # Array holding all the properties

    def buyProperty(self, player):
        # Removes the property from the bank array and adds it to the player's dictionary of properties. It also removes money from said player.
        raise NotImplementedError
    
    def sellProperty(self, player):
        # Removes the property from the player array and adds it to the bank's dictionary of properties. It also gives money to said player.
        raise NotImplementedError

    def mortageProperty(self, player):
        # Gives money to player without removing ownership.
        raise NotImplementedError
    
    def getMoney(self, player):
        # Remove money from player.
        raise NotImplementedError
    
    def giveMoney(self, player):
        # Give money to player.
        raise NotImplementedError