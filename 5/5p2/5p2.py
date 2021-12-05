setIncrement = lambda n, i, x, str: n + i if str[1 if x == True else 2] == '+' else n - i

with open("../input.txt") as f_input:
    map = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
    atleast_2 = 0

    for line in f_input:
        draw_mode = ''
        l = line.rstrip().split('->')
        point1 = [int(i) for i in l[0].split(',')]
        point2 = [int(i) for i in l[1].split(',')]

        if point1[1] == point2[1]: draw_mode = 'h' 
        elif point1[0] == point2[0]: draw_mode = 'v'
        else:
            draw_mode = 'd'
            draw_mode += '+' if point2[0] > point1[0] else '-'
            draw_mode += '+' if point2[1] > point1[1] else '-'

        if draw_mode[0] == 'd': diff = max(abs(point2[0] - point1[0]), abs(point2[1] - point1[1]))
        else: diff = (point2[1] - point1[1]) if point1[0] == point2[0] else (point2[0] - point1[0])

        if diff > 0: r = list(range(0, diff + 1))
        else: r = [-x for x in list(range(0, -(diff - 1)))]

        for i in r: 
            if draw_mode[0] == 'h':
                map[point1[1]][point1[0] + i] += 1
                if map[point1[1]][point1[0] + i] == 2: atleast_2 += 1
            elif draw_mode == 'v':
                map[point1[1] + i][point1[0]] += 1
                if map[point1[1] + i][point1[0]] == 2: atleast_2 += 1
            else:
                x = setIncrement(point1[0], i, True, draw_mode)
                y = setIncrement(point1[1], i, False, draw_mode)
                map[y][x] += 1
                if map[y][x] == 2: atleast_2 += 1

    print(f"At least 2 number is: {atleast_2}")