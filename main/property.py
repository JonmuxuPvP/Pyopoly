import player

class Property:

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.owner = None
        self.houses = 0
        self.hotels = 0
        self.price = 0
        self.isMortgaged = False
    
    # Calculates the total amount of money the player owes the owner
    def payRent(self, player):
        total = 0
        if player.money >= total:
            self.owner.money += total
            player.money -= total
        elif player.calcTotal > total:
            pass # Force the player to start selling
        else:
            pass # Bankrupt hehe
            
            

        


