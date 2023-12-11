class Player:
    """A Player in the story telling Game "Work from home".

    Attributes:
        charisma     The charisma value of a player, an integer.
        strength     The strength value of a player, an integer.
        luck         The luck value of a player, an integer.
        fellowship   The fellowship value of a player, an integer.
        inventory    The inventory value of a player, an array.
    """

    #--- constructor ---#
    def __init__(self, charisma, strength, luck, fellowship, inventory):
        self.charisma = charisma
        self.strength = strength
        self.luck = luck
        self.fellowship = fellowship
        self.inventory = inventory

    #--- Getter functions ---#
    def get_charisma(self):
        return self.charisma

    def get_strength(self):
        return self.strength

    def get_luck(self):
        return self.luck

    def get_fellowship(self):
        return self.fellowship 

    def get_inventory(self):
        return self.inventory

    #--- Check inventory ---#
    def is_in_inventory(obj):
        """
        Returns true if given object is in the players inventory.
        Returns false if given objects is NOT in the players inventory.
        """
        if obj in self.inventory:
            return True
        else:
            return False

    #--- Setter functions --#
    def set_stats(self, charisma, strength, luck, fellowship):
        self.charisma = charisma
        self.strength = strength
        self.luck = luck 
        self.fellowship = fellowship

    def set_charisma(self, value):
        self.charisma = value

    def set_strength(self, value):
        self.strength = value

    def set_luck(self, value):
        self.luck = value

    def set_fellowship(self, value):
        self.fellowship = value

    def set_inventory(self, value):
        self.inventory = value

    #--- Update functions ---#
    def update_charisma(self, value):
        self.charisma += value

    def update_strength(self, value):
        self.strength += value

    def update_luck(self, value):
        self.luck += value

    def update_fellowship(self, value):
        self.fellowship += value

    def update_inventory(self, value):
        self.inventory.append(value)
