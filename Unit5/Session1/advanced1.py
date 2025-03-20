class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent

def get_place(my_player):
    place = 0
    
    tmp = my_player
    
    while tmp:
        tmp = tmp.ahead
        place += 1
    
    return place
        

def print_results(race_results):
    print('\n'.join(f'{i + 1}. {c.character}' for i, c in enumerate(race_results)))

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
player2_rank = get_place(peach)
player3_rank = get_place(mario)

print(player1_rank)
print(player2_rank)
print(player3_rank)
