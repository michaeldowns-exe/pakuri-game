class Pakuri:
    #initialize
    def __init__(self, species):
        self.species = str(species)
        self.attack = int((len(self.species) * 7) + 9)
        self.defense = int((len(self.species)* 5) + 17)
        self.speed = int((len(self.species)* 6) + 13)
        

    def get_species(self):
        return self.species
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_speed(self):
        return self.speed
    
    def set_attack(self,new_attack):
        self.attack = new_attack

    #used in evolve species in pakudex
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    