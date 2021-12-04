def skiprows(actual_row) -> int:
    diff = 5 - actual_row - 1
    for _ in range(0, diff): f_input.readline()
    return diff

with open("../input.txt", "r") as f_input:
    extraction = f_input.readline()
    #f_input.readline()
    cur = f_input.tell()
    len_f = sum(1 for line in f_input)
    f_input.seek(cur)

    rows = []
    cols = []
    cursor_better = cur
    better_turn = 0
    better_row = 0
    local_line = 0
    turn = 0
    row = 0

    for i in range(0, len_f):
        if i == 0 or i % 6 == 0: 
            f_input.readline()
            rows = [0 for _ in range(0, 5)]
            cols = [0 for _ in range(0, 5)]
            local_line = 0
            turn = -1
            row = -1
            continue
        
        being_analized = f_input.tell()
        line = f_input.readline()
        row += 1
        if row > better_row: 
            i += skiprows(row)
        for ex in extraction:
            turn += 1
            try:
                index = line.index(ex)
                rows[i] |= (1 << 5 - 1 - index)
                if rows[i] == 31: 
                    print("BINGO!")
                    if better_turn == 0 or turn < better_turn:
                        better_turn = turn
                        cursor_better = being_analized
                        i += skiprows(row)
                        break
                cols[index] |= (1 << i)
                if cols[index] == 31: 
                    print("BINGO!")
                    if better_turn == 0 or turn < better_turn:
                        better_turn = turn
                        cursor_better = being_analized
                        break
            except ValueError as ve:
                break;

        
