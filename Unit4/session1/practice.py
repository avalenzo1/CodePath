# def find_task_pair(task_times, available_time):
#     times = set()
    
#     left = 0

#     while left <= len(task_times) - 1:
#         remainder = available_time - task_times[left]
        
#         if remainder in times:
#             return True
        
#         times.add(task_times[left])
#         left += 1

#     return False

# # Space + Time = O(N)


# task_times = [30, 45, 60, 90, 120]
# available_time = 105
# print(find_task_pair(task_times, available_time))

# task_times_2 = [15, 25, 35, 45, 55]
# available_time = 100
# print(find_task_pair(task_times_2, available_time))

# task_times_3 = [20, 30, 50, 70]
# available_time = 60
# print(find_task_pair(task_times_3, available_time))

# # !Don't have any time slots
# # !Available is less than or equal to 0

# def find_smallest_gap(work_sessions):
#     mininum = float('inf')
    
#     for i in range(len(work_sessions) - 1):
#         # print("index",i)
#         curr_meeting = work_sessions[i]
#         next_meeting = work_sessions[i + 1]
        
#         gap = next_meeting[0] - curr_meeting[1]
        
#         mininum = min(mininum, gap)
        
#     if mininum > 120:
#         mininum = int((mininum - 80) / 2)
        
#     elif mininum > 60:
#         mininum = mininum - 40
            
#     return mininum

# # O(N) - Time 
# # O(1) - Space
        
# work_sessions = [(900, 1100), (1300, 1330), (1600, 1800)]
# print(find_smallest_gap(work_sessions))
# # expected 

# work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
# print(find_smallest_gap(work_sessions_2))

# work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
# print(find_smallest_gap(work_sessions_3))

def calculate_expenses(expenses):
    hashmap = {}
    
    minimum = 0
    max_key = ""
    
    for t in expenses:
        hashmap[t[0]] = hashmap.get(t[0], 0) + t[1]
        
        if 
        minimum = max(hashmap.get(t[0]), minimum)
        
        
    return hashmap, minimum
    
expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

# ({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
# ({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
# ({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')