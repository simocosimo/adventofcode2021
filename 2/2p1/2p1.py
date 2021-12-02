with open("../input.txt", "r") as f_input:
    h = 0
    d = 0

    for line in f_input:
        dir = line.split()
        if dir[0] == "forward":
            h += int(dir[1])
            continue
        if dir[0] == "down":
            d += int(dir[1])
            continue
        if dir[0] == "up":
            d -= int(dir[1])
            continue

    print(f"Result: {d*h}")