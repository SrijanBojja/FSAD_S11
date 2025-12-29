def quadratic_probing(size, keys): 
    table = [-1] * size 
 
    for key in keys: 
        index = key % size 
 
        if table[index] == -1: 
            table[index] = key 
        else: 
            i = 1 
            while i < size: 
                new_index = (index + i * i) % size 
                if table[new_index] == -1: 
                    table[new_index] = key 
                    break 
                i += 1 
    return table 
T = int(input()) 
for _ in range(T): 
    size = int(input()) 
    N = int(input()) 
    keys = list(map(int, input().split())) 
 
    result = quadratic_probing(size, keys) 
    print(*result)