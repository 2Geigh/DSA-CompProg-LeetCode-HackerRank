###### PAGE 63 #####

# 4.2
# Write a recursive function to count the number of items in a list
def f2(list: list) -> int:
    if len(list) == 0:
        return 0
    
    return 1 + f2(list[1:])

# 4.3
# Write a recursive function to find the maximum number in a list
# INITIAL ATTEMPT
def f3(arr: list) -> int | None:
    if len(arr) < 1:
        return None
    
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] < arr[1]:
        return f3(arr[1:])
    
    if arr[0] > arr[1]:
        if len(arr) == 2:
            return arr[1]
        else:
            return f3(arr[0:1] + arr[2:])
# ATTEMPT AFTER READING SOLUTION
def f3assisted(arr: list) -> int | None:
    return

# 4.4
# Come up with a base case and a recursive case for the binary search algorithm
[] # Base case 1
[n] # Base case 2, where n is some integer
# Recursive case would be that the target is not equal to the average of the min
    # and max we're scanning over, and must adjust the min or max towards
    # mid accordingly
Acid = []