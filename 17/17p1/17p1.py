from functools import reduce
import math

def sumOfNumbers(n): return math.floor(n * (n + 1) / 2)

def checkLanding(x_constraints, y_constraints, vel):
    global steps
    max_x = sumOfNumbers(vel[0])

    def functRed(x, y):
        global steps
        if x != deltaX: steps += 1
        return (x + y) if x != deltaX else (x)

    if max_x < x_constraints[0]: return False
    for deltaX in range(x_constraints[0], x_constraints[1] + 1):
        steps = 1
        if (reduce(functRed, range(vel[0], 0, -1)) == deltaX):
            y = sumOfNumbers(vel[1]) - sumOfNumbers(abs(vel[1] - steps + 1))
            if y >= y_constraints[0] and y <= y_constraints[1]: return True

            if deltaX == max_x:
                while y >= y_constraints[0]: 
                    steps += 1
                    y = sumOfNumbers(vel[1]) - sumOfNumbers(abs(vel[1] - steps + 1))
                    if y <= y_constraints[1] and y >= y_constraints[0]: return True
    return False

with open("../input.txt", "r") as f_input:
    info = f_input.readline().rstrip()
    x_constraints = list(map(int, info.split('x=')[1].split(', y=')[0].split('..')))
    y_constraints = list(map(int, info.split('x=')[1].split(', y=')[1].split('..')))
    maxY = max(abs(y_constraints[0]), abs(y_constraints[1]))
    high_vel = ()
    steps = 1
    res = 0

    for i in range(1, x_constraints[1] + 1):
        for x in range(-maxY, maxY + 1):
            if checkLanding(x_constraints, y_constraints, (i, x)) and sumOfNumbers(x) > res:
                res = sumOfNumbers(x)
                high_vel = (i, x)

    print(high_vel, res)