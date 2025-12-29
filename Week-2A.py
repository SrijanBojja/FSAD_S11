def linear_probing_hash(): 
    T = int(input()) 
 
    for _ in range(T): 
        N = int(input()) 
        keys = list(map(int, input().split())) 
 
        table = [-1] * N 
 
        for key in keys: 
            idx = key % N 
 
            # Linear probing 
            start = idx 
            while table[idx] != -1: 
                idx = (idx + 1) % N 
                if idx == start: 
                    break 
 
            if table[idx] == -1: 
                table[idx] = key 
 
        print(*table) 
 
# Run the program 
linear_probing_hash()