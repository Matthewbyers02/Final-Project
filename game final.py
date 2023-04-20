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
            herd = ran.randint(1,3)
            print("You were no match for the power of this herd, your health has decreased by {herd}.") 
            self.health = self.health - herd
        else:
            self.health = self.health + buffaloDict[health]
            print("You feasted! You're health has increased")
            #how can we turn this type of process into a magic metod?
    else:
        self.health = self.health - 1 #idk if I did this right, but it should decrease current animals hunger
                                      #We should decrease health by 1 to account for hunger. MB
        print("You move on, looking for the next meal. You are hungry and lose health.")
    print(f"""Your stats are currently:\n 
          Health: {self.health}\n
          Attack: {self.attack}\n
          Speed: {self.speed}\n
          Armor: {self.armor} """)
        
def sit2(self):
    
    act2 = input("""You're super thirsty and come across a murky watering whole where 
                 an agressive hippo is known to rest. \nDo you drink from it? (y/n)""")
    if act2 != "y" or "n":
        print("Please enter either y or n")
    if act2 == "y":
        isHome = ran.randint(0, 1)
        if isHome == 0:
            print("Drink up! Looks like the hippo wasn't home.")
            self.health + 2
        if isHome == 1:
            print("The hippo was home and angry, the hippo attacked")
            self.health - ran.randint(2,4)
    else:
        (self.health - 2 if self.speed > 6 
         else self.health - 2 & print("You may not get to another watering hole for a while")) 
        #satisfied the condional expr req here^
    print(f"""Your stats are currently:\n 
          Health: {self.health}\n
          Attack: {self.attack}\n
          Speed: {self.speed}\n
          Armor: {self.armor} """)
        
def sit3(self):

    food = {"boar", "monkey", "impala", "wolf", "snake", "hyena", "zebra", "ostrich"} #says food isnt access in fstring
    spoiled = {"monkey", "impala", "ostritch"}
    userOption = {}
    #to ask 3 times 
    print("""You come across an assortment of carcasses in an abondoned cave.\n{food}""")
    i = 3
    while i > 0 :
        act3 = input("""Choose one to eat! You have {i} pick(s) left: """)
        #updates initalized set
        userOption.append(act3)
        i -= 1
    #checks to see if any chosen food is spoiled and updates health accordinly 
    overlap = bool(userOption & spoiled)
    if overlap == False:
        self.health += 3
        print("You chose your food wisely. Your health is now {self.health}")
    else:
        self.health -= 3
        print("Some of the food you ate was spoiled! You health is now {self.health}")

    print(f"""Your stats are currently:\n 
        Health: {self.health}\n
        Attack: {self.attack}\n
        Speed: {self.speed}\n
        Armor: {self.armor} """)
        
#def sit4(self):
#    act4 = input("""You spot a hunger lining up a shot!\n
#                Do you charge or do you hide? (r/h):""")
#    odds = choice(range(1,5)) #idk if this is right, I want to pick 1-5
#    if act4 == "r":
#        if odds < 2:
            
        
    
    

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

def animalDicts():
    alligatorDict = {"name":"Alligator", "attack":8, "speed":2, "armor":9, "health":7}
    cheetaDict = {"name":"Cheeta", "attack":10, "speed":10, "armor":3, "health":3}
    elephantDict = {"name":"Elephant", "attack":6, "speed":4, "armor":7, "health":6}
    buffaloDict = {"name":"Buffalo", "attack":2, "speed":2, "armor":4, "health":4}
    return alligatorDict, cheetaDict, elephantDict, buffaloDict

def startingAnimal():
    alligatorDict, cheetaDict, elephantDict, buffaloDict = animalDicts()
    print(alligatorDict)
    print(cheetaDict)
    print(elephantDict)
    print(buffaloDict)

    PAnimal = input("From the list above, which animal would you like to use?\n")
    if PAnimal.upper() == "ALLIGATOR":
        PAnimal = Traits(alligatorDict["name"], alligatorDict["attack"], alligatorDict["speed"], alligatorDict["armor"], alligatorDict["health"])
    elif PAnimal.upper() == "CHEETA":
        PAnimal = Traits(cheetaDict["name"], cheetaDict["attack"], cheetaDict["speed"], cheetaDict["armor"], cheetaDict["health"])
    elif PAnimal.upper() == "ELEPHANT":
        PAnimal = Traits(elephantDict["name"], elephantDict["attack"], elephantDict["speed"], elephantDict["armor"], elephantDict["health"])
    elif PAnimal.upper() == "BUFFALO":
        PAnimal = Traits(buffaloDict["name"], buffaloDict["attack"], buffaloDict["speed"], buffaloDict["armor"], buffaloDict["health"])

    return PAnimal

    

def main():
    PAnimal = startingAnimal()
    sit1(PAnimal)
    sit2(PAnimal)
    sit3(PAnimal)

if __name__ == "__main__":
    main()
