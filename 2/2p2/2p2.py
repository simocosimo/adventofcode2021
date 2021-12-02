with open("../input.txt", "r") as f_input:
    h = 0
    d = 0
    a = 0

    for line in f_input:
        dir = line.split()
        if dir[0] == "forward":
            h += int(dir[1])
            d += a * int(dir[1])
            continue
        if dir[0] == "down":
            a += int(dir[1])
            continue
        if dir[0] == "up":
            a -= int(dir[1])
            continue

    print(f"Result: {d*h}")