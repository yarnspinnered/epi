def find_duplicate_elements(arr):
    i = 0
    while i < len(arr):
        x = arr[i]
        if arr[x] == x and x != i: #destination is good and im not trying to swap with myself
            return "Has duplicates"
        elif arr[x] != x: # destination is bad
            arr[x], arr[i] = arr[i], arr[x]
        else: # destination is good and im trying to swap with myself
            i += 1
    return "No duplicates"
