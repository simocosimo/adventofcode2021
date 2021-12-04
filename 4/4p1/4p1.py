with open("../input.txt", "r") as f_input:
    extraction = f_input.readline()
    f_input.readline()
    cur = f_input.tell()
    len_f = sum(1 for line in f_input)
    f_input.seek(cur)

    rows = [0 for _ in range(0, 5)]
    cols = [0 for _ in range(0, 5)]

    for i in range(0, len_f):
        if i != 0 and i % 6 == 0: 
            f_input.readline()
            break
        
        line = f_input.readline()  #empty line
