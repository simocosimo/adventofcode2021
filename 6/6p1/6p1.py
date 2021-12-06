with open("../input.txt") as f_input:
    delays = list(map(int, f_input.readline().rstrip().split(',')))
    
    for x in range(0, 130):
        for i in range(0, len(delays)):
            if delays[i] == 0:
                delays[i] = 6
                delays.append(8)
                continue
            delays[i] -= 1
        
    print(f"Number of fishes after 80 days: {len(delays)}")