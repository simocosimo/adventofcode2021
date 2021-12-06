from collections import Counter

def explore(val, actual_depth, target_depth):
    cumulative_son = 1
    #print(f"Called explore() - cum_son: {cumulative_son}")
    while actual_depth < target_depth:
        #print(f"val {val}, actual_depth {actual_depth}, target {target_depth}")
        val -= 1
        actual_depth += 1
        local_depth = actual_depth
        if val < 0: 
            val = 6
            #print("Found a son!")
            cumulative_son += explore(8, actual_depth, target_depth)
            #print(f"returned - cum_son: {cumulative_son}")
            actual_depth = local_depth
    return cumulative_son;
    
with open("../input.txt") as f_input:
    delays = list(map(int, f_input.readline().rstrip().split(',')))
    c = Counter(delays)
    delays = list(set(delays))
    print(delays, c)
    target_days = 200
    tot, n = 0, 0
    
    print(f"Unique len: {len(delays)}")
    for i in range(0, len(delays)):
        n = explore(delays[i], 0, target_days)
        n *= c[delays[i]]
        tot += n
        print(f"Finished counting for value #{i}")

    print(f"Number of fishes after {target_days} days: {tot}")