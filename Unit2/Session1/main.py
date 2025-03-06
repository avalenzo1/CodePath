# PROBLEM 1

# def total_treasure(treasure_map):
#     total_treasures = 0
    
#     # O(N)
    
#     for value in treasure_map.values():
#         total_treasures += value
    
#     return total_treasures

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasure(treasure_map1)) 
# print(total_treasure(treasure_map2)) 

# PROBLEM 2

import string

def can_trust_message(message):
    characters = set()
    alphabet = set()
    
    for letter in string.ascii_lowercase:
        alphabet.add(letter)
    
    for char in message:
        characters.add(char)
    
    return alphabet.intersection(characters) == alphabet

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

# PROBLEM 5

# from collections import defaultdict

# def find_treasure_indices(gold_amounts, target):
#     # Do hash set to set if
#     hashMap = defaultdict(list)
    
#     for index, gold in enumerate(gold_amounts):
#         hashMap[gold].append(index)

#     for gold in gold_amounts:
#         if len(hashMap[target - gold]) > 0:
#             return [hashMap[gold][0], hashMap[target - gold][0]]
        
#         # if index == each other, dont return
    
#     return False

# gold_amounts1 = [2, 7, 11, 15]
# target1 = 9

# gold_amounts2 = [3, 2, 4]
# target2 = 6

# gold_amounts3 = [3, 3]
# target3 = 6

# print(find_treasure_indices(gold_amounts1, target1))  
# print(find_treasure_indices(gold_amounts2, target2))  
# print(find_treasure_indices(gold_amounts3, target3))  