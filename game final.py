class Traits:
    
    def __init__(self, name, attack, speed, armor, health):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.armor = armor
        self.health = health
    
#situations as methods?
#if hunger = 0, the game ends (you die)
    
def sit1(self):
    
    act1 = input("""You come across a herd of buffalo bathing in the mud.\n
          Do you choose to attack or leave them be? (a/l):""")
    if act1 == "a":
        if self.armor < 5 | self.attack < 5:
            print("you were overpowered and died") 
            self.health = 0
        else:
            self = self + buffalo
            print(f"You feasted! You're health is now {self.health}")
            #how can we turn this type of process into a magic metod?
    else:
        self = self - buffalo #idk if I did this right, but it should decrease current animals hunger
        print(f"You move on, looking for the next meal. You're health is now: {self.health}")
        
def sit2(self):
    
    act2 = input("""You're super thirsty and come across a murky watering whole where 
                 an agressive hippo is known to rest. \nDo you drink from it? (y/n)""")
    if act2 == "y":
        print("Drink up! Looks like the hippo wasn't home.")
        self.health + 3
    else:
        (self.health - 2 if self.speed > 6 
         else self.health - 5 & print("You may not get to another watering hole for a while")) 
        #satisfied the condional expr req here^

#magic methods
def __add__(self, other): 
    if isinstance(other, Traits):
        return Traits(
            self.attack + other.attack,
            self.hunger + other.hunger
        )
        
def __sub__(self, other):
    if isinstance(other, Traits):
        return Traits(
            self.attack - other.attack,
            self.hunger - other.hunger
        )

       
    
    
#initalized animals
alligator = Traits("Alligator", 8, 2, 9, 7)
cheeta = Traits("Cheeta", 4, 10, 3, 3)
elephant = Traits("Elephant", 6, 4, 7, 5)
#"food" animals?
buffalo = Traits("Buffalo", 1, 1, 2, 3)


