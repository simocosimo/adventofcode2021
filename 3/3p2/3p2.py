from copy import deepcopy
import math

def bitReturn(mode, rev=False) -> str:
    if mode == '>': return '1' if not rev else '0'
    else: return '0' if not rev else '1'

def comm(target, i, mode) -> str:
        th = math.floor(sum(1 for _ in target) / 2) + 1
        z, o = 0, 0
        for x in range(0, len(target)):
            if target[x][i] == '0': z += 1
            else: o += 1
            if z >= th: return bitReturn(mode, True)
            if o >= th: return bitReturn(mode)
        return bitReturn(mode)

with open("../input.txt", "r") as f_input:
    op = ['>', '<']
    op_res = []
    f = [l.rstrip() for l in f_input.readlines()]
    n_bits = len(f[0])

    for o in op:
        copy = deepcopy(f)
        for b in range(0, n_bits):
            actual = comm(copy, b, o)
            copy = [n for n in copy if n[b] == actual]
            if len(copy) == 1: break
        op_res.append(copy[0])

    print(op_res)  
    print(f"Result: {int(op_res[0], 2) * int(op_res[1], 2)}")