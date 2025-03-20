# from collections import queue

import math


class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)

def of_personality_type(townies, personality_type):
    if not townies:
        return []
    
    result = []
    
    for villager in townies:
        if villager.personality == personality_type:
            result.append(villager.name)
            
    return result

def message_received(start_villager, target_villager):
    # Use DFS
    # Travel through graph
    # If current villager == target_villager
    visited = set()
    # q = queue([start_villager])
    
    current = start_villager
    
    while current:
        if current in visited:
            break
        
        if current == target_villager:
            return True
        else:
            visited.add(current)
            
        current = current.neighbor
        
    return False
    
    
    
        
# apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# # isabelle => tom => kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# print_linked_list(kk_slider)

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next
        
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

# def catch_fish(head):
#     # If head is None print better luck next time
#     if head is None:
#         print("Aw! Better luck next time!")
#         return
    
#     print(f"I caught a {head.fish_name}")

#     new_head = head.next
    
#     return new_head

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# # iterate through linked 

# print_linked_list(fish_list)
# fish_list = catch_fish(fish_list)
# print_linked_list(fish_list)
# fish_list = catch_fish(fish_list)
# print_linked_list(fish_list)
# fish_list = catch_fish(fish_list)
# print_linked_list(fish_list)
# fish_list = catch_fish(fish_list)
# print_linked_list(fish_list)

# print(catch_fish(empty_list))

def fish_chances(head, fish_name):
    # iterate through list
    # find matching fishes
    # Count list size
    # probability = math.floor() * 100 matching / size
    
    ptr = head
    count = 0
    total_size = 0
    
    while ptr:
        total_size += 1
        
        if ptr.fish_name == fish_name:
            count += 1
    
        ptr = ptr.next
        
    
    rounded_probability = math.floor((count / total_size) * 100) / 100
    
    return rounded_probability

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

def restock(head, new_fish):
    new_node = Node(new_fish)
    
    if head is None:
        return new_node
    
    ptr = head
    
    while ptr.next is not None:
        ptr = ptr.next
    
    ptr.next = new_node
    
    return head
        
    

fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print_linked_list(restock(fish_list, "Rainbow Trout"))