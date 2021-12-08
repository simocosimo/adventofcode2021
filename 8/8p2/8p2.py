def findInString(string, tofind):
    s = list(string)
    t = list(tofind)
    for x in t:
        if x not in s: return False
    return True

findByVal = lambda mydict, v: list(mydict.keys())[list(mydict.values()).index(v)]

with open("../input.txt") as f_input:

    res = 0
    for l in f_input:
        dictN = {}
        r = ''
        val = l.rstrip().split('|')[1].split()
        val = [''.join(sorted(val[i])) for i in range(0, len(val))]
        conn = l.rstrip().split('|')[0].split()
        conn = [''.join(sorted(conn[i])) for i in range(0, len(conn))]
        for x in conn:
            if len(x) == 2: dictN[1] = x
            if len(x) == 4: dictN[4] = x
            if len(x) == 3: dictN[7] = x
            if len(x) == 7: dictN[8] = x
        conn = [conn[i] for i in range(0, len(conn)) if len(conn[i]) == 5 or len(conn[i]) == 6]
        conn.sort(key=len)
       
        for i in range(0, 3):
            c = 0
            for x in range(3, len(conn)):
                if findInString(conn[x], conn[i]): c += 1
            if c == 2: dictN[5] = conn[i]
            if c == 1: dictN[3] = conn[i]
            if c == 0: dictN[2] = conn[i]

        for i in range(3, len(conn)):
            if findInString(conn[i], dictN[3]):
                dictN[9] = conn.pop(i)
                break

        for i in range(3, len(conn)):
            if findInString(conn[i], dictN[5]):
                dictN[6] = conn.pop(i)
                break
            i += 1
        
        dictN[0] = conn[3]
        
        for x in val:
            r += str(findByVal(dictN, x))
        res += int(r)
    print(f"Result is {res}")
    
    
        