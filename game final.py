import random as ran

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
          Do you choose to attack or run? (a/r): """)
    if act1 == "a":
        if self.armor < 5 | self.attack < 5:
            print("you were overpowered and died") 
            self.health = 0
        else:
            self.health = self.health + buffalo
            print(f"You feasted! You're health is now {self.health}")
            #how can we turn this type of process into a magic metod?
    else:
        self.health = self.health - 1 #idk if I did this right, but it should decrease current animals hunger
                                      #We should decrease health by 1 to account for hunger. MB
        print(f"You move on, looking for the next meal. You are hungry and lose health, your health is now: {self.health}")
        
def sit2(self):
    
    act2 = input("""You're super thirsty and come across a murky watering whole where 
                 an agressive hippo is known to rest. \nDo you drink from it? (y/n)""")
    if act2 is not "y" or "n":
        print("Please enter either y or n")
    if act2 == "y":
        isHome = ran.randint(0, 1)
        if isHome == 0:
            print("Drink up! Looks like the hippo wasn't home.")
            self.health + 2
        if isHome == 1:
            print("The hippo was home and angry, the hippo attacked")
            self.health - 3
    else:
        (self.health - 2 if self.speed > 6 
         else self.health - 2 & print("You may not get to another watering hole for a while")) 
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


