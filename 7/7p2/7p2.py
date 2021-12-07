with open("../input.txt") as f_input:
    gauss = lambda v: int(v*(v+1)/2)
    hpos = list(map(int, f_input.readline().rstrip().split(',')))
    min_fuel = -1
    min_pos = 0

    for i in range(min(hpos), max(hpos)):
        f = 0
        for x in range(0, len(hpos)):
            f += gauss(abs(hpos[x] - i))
            if f > min_fuel and i != min(hpos): break
        if min_fuel == -1 or f < min_fuel: 
            min_fuel = f
            min_pos = i
            continue
    
    print(f"Min fuel is {min_fuel} when aligning at pos {min_pos}")