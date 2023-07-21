from pakuri import Pakuri
class Pakudex:

    # creates paku instance w attr capacity, obj list, and obj count

    def __init__(self, capacity=20):
        self.cap = capacity
        self.list = [None] * capacity
        self.count = 0

    def get_size(self):
        return self.count

    def get_capacity(self):
        return self.cap
    
    #gets names from obj in obj list using pakuri methods
    def get_species_array(self):
        if self.count == 0:
            return None
        species = [None] * self.count
        for i in range(self.count):
            species[i] = Pakuri.get_species(self.list[i])
        return species

        
    #gets stats of specific obj from list using pakuri methods
    def get_stats(self, species):
        paku = Pakuri(species)
        index = False
        for i in range(self.count):
            if Pakuri.get_species(self.list[i]).lower() == Pakuri.get_species(paku).lower():
                index = True

        if index:
            stats = [Pakuri.get_attack(paku), Pakuri.get_defense(paku), Pakuri.get_speed(paku)]
            return stats
        else:
            return None


    #sorts pakuri alphabetic order
    def sort_pakuri(self):
        for i in range(self.count - 1):
            for j in range(i + 1, self.count):
                if  Pakuri.get_species(self.list[i]).lower() > Pakuri.get_species(self.list[j]).lower():
                    self.list[i], self.list[j] = self.list[j], self.list[i]
                   
    #checks if pakuri name is duplicate and if not adds to obj list and interates count
    def add_pakuri(self, species):
        paku = Pakuri(species)
        copy = False
        if self.count == self.cap:
            return False
        for i in range(self.count):
            if Pakuri.get_species(self.list[i]).lower() == Pakuri.get_species(paku).lower():
                copy = True
        if not copy:
            self.list[self.count] = paku
            self.count += 1
            return True
        else:
            return False


            
    #uses evolve method on specific pakuri
    def evolve_species(self, species):
        lookPakuri = None

        if self.count <= 0:
            return False
        
        for i in range(self.count):
            if self.list[i] is not None:
                exists = Pakuri.get_species(self.list[i])
                
                if exists == species:
                    lookPakuri = self.list[i]

        if lookPakuri is None:
            return False

        Pakuri.evolve(lookPakuri)
        return True




    

