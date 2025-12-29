def double_hashing(table_size, keys): 
    table = [-1] * table_size 
 
    for key in keys: 
        h1 = key % table_size 
        h2 = 1 + (key % (table_size - 1)) 
        i = 0 
        while i < table_size: 
            index = (h1 + i * h2) % table_size 
            if table[index] == -1: 
                table[index] = key 
                break 
            else: 
                i += 1 
    return table 
T = int(input()) 
for _ in range(T): 
    table_size = int(input()) 
    n = int(input()) 
    keys = list(map(int, input().split())) 
    result = double_hashing(table_size, keys) 
    print(*result)