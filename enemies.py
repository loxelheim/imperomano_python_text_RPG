class Enemy:
    def __init__(self, name="", hp=100, mp=100, sp=100, abilities=[]):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.sp = sp
        self.abilities = abilities

    def print_stats(self):
        header = f"“{self.name}“ Status:"
        print(header)
        print("-" * len(header))
        print(f"Health: {self.hp}")
        print(f"Mana: {self.mp}")
        print(f"Stamina: {self.sp}")
        print("-" * len(header))
        print(f"Common Abilities:")
        for ability in self.abilities:
            print(f"- “{ability}“")

        print("-" * len(header), "\n")



class Skeleton(Enemy):
    def __init__(self, name="Raised Skeleton", hp=50, mp=50, sp=300,
                abilities=["Reconstruct", "Bone Toss", "Menacing Rattle"]):
        super().__init__(name, hp, mp, sp, abilities)


        
class Goblin(Enemy):
    def __init__(self, name="Gobblin Grunt", hp=20, mp=20, sp=20, 
                abilities=["Screech", "Claw"]):
        super().__init__(name, hp, mp, sp, abilities)
        

skeleton = Skeleton()
goblin = Goblin()

# print("Skelli Abilities:", skeleton.abilities)
# print("Gobbo Abilities:", goblin.abilities)
skeleton.print_stats()
goblin.print_stats()