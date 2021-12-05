with open("../input.txt") as f_input:
    map = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
    atleast_2 = 0

    for line in f_input:
        draw_mode = ''
        l = line.rstrip().split('->')
        point1 = [int(i) for i in l[0].split(',')]
        point2 = [int(i) for i in l[1].split(',')]

        if point1[0] != point2[0] and point1[1] != point2[1]: continue
        draw_mode = 'h' if point1[1] == point2[1] else 'v'
        diff = (point2[1] - point1[1]) if point1[0] == point2[0] else (point2[0] - point1[0])
        if diff > 0: diff += 1
        else: diff -= 1

        if diff > 0: r = list(range(0, diff))
        else: r = [x * -1 for x in list(range(0, -diff))]

        for i in r: 
            if draw_mode[0] == 'h':
                map[point1[1]][point1[0] + i] += 1
                if map[point1[1]][point1[0] + i] == 2: atleast_2 += 1
            else:
                map[point1[1] + i][point1[0]] += 1
                if map[point1[1] + i][point1[0]] == 2: atleast_2 += 1

    print(f"At least 2 number is: {atleast_2}")