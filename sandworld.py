class SandCastle:
    '''
    '''
    # Klassenattribute
    castle_count = 0
    castle_names = []
    wavy_seperator = "~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"
    
    # Konstruktor
    # Hier werden die Attribute definiert
    def __init__(self, name="Sand Castle", geometry=4, tiers=2):
        self.geometry = geometry
        self.tiers = tiers
        self.name = name

        SandCastle.castle_count += 1
        SandCastle.castle_names.append(self.name)
        
    def __str__(self):
        return f"SandCastle: “{self.name}“"
        
        
    # Methoden
    def wash_away(self):
        print(SandCastle.wavy_seperator)
        print(f"\n The tide comes and washes away “{self.name}“ \n")

        SandCastle.castle_count -= 1
        SandCastle.castle_names.remove(self.name)
        
        SandCastle.total()

    def total():
        print(SandCastle.wavy_seperator)
        print(f"There is a total of {SandCastle.castle_count} Sand Castles on the beach")
        for castle in SandCastle.castle_names:
            print(f" --> {castle}")
        


sand_castle = SandCastle()
print('sand_castle: ', sand_castle)

my_castle = SandCastle(name="Ston'inshoo")
not_my_castle = SandCastle(name="Quartzdust")
third_castle = SandCastle(name="Big Hole")


SandCastle.total()

third_castle.wash_away()

SandCastle.total()