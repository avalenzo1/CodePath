class Villager:
    def __init__(self, name, species, personality, catchphrase,  neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
        

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        if all(x.isalpha() or x.isspace() for x in new_catchphrase) and len(new_catchphrase) < 20:
            print("Catchphrase Updated!")
            self.catchphrase = new_catchphrase
            return True
        
        print("Invalid catchphrase")
        return False
    
    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)
    
    def print_inventory(self):
        furniture_dict = {}
        
        for item in self.furniture:
            furniture_dict[item] = furniture_dict.get(item, 0) + 1
        
        if furniture_dict:
            print(', '.join('%s : %s' % (k,furniture_dict[k]) for k in furniture_dict.keys()))
        else:
            print("Inventory empty")
   
def of_personality_type(townies, personality_type):
    # Filter
    return [townie.name for townie in townies if townie.personality == personality_type]


def message_received(start_villager, target_villager):
    pass

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))