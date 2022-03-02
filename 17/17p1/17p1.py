from functools import reduce

def checkLanding(x_constraints, y_constraints, vel):
    global steps
    checkX = False
    checkY = False
    breaked = False
    max_x = sum(range(vel[0], 0, -1))

    def functRed(x, y):
        global steps
        if x != deltaX: steps += 1
        return (x + y) if x != deltaX else (x)

    for deltaX in range(x_constraints[0], x_constraints[1] + 1):
        checkX = (reduce(functRed, range(vel[0], 0, -1)) == deltaX)
        if checkX:
            y = sum(range(vel[1], vel[1] - steps, -1))
            if y >= y_constraints[0] and y <= y_constraints[1]:
                #print(f"Breaked with {deltaX} and {y}")
                checkY = True
                break

            if deltaX == max_x:
                while y >= y_constraints[0]: 
                    steps += 1
                    y = sum(range(vel[1], vel[1] - steps, -1))
                    if y <= y_constraints[1] and y >= y_constraints[0]:
                        #print(f"Breaked with {deltaX} and {y} - steps {steps}")
                        breaked = True
                        checkY = True
                        break
                
            if breaked: 
                breaked = False
                break

        steps = 1
    return (checkX and checkY)

with open("../input.txt", "r") as f_input:
    info = f_input.readline().rstrip()
    x_constraints = list(map(int, info.split('x=')[1].split(', y=')[0].split('..')))
    y_constraints = list(map(int, info.split('x=')[1].split(', y=')[1].split('..')))

    # f(step) = sum(range(vel_x, vel_x - step, -1)) = deltaX
    # f(deltaX) = sum(range(0, vel_x + 1))

    steps = 1
    maxY = 0
    high_vel = ()
    for i in range(1, x_constraints[1] + 1):
        for x in range(0, 150):
            vel = (i, x)
            isLanded = checkLanding(x_constraints, y_constraints, vel)
            if isLanded:
                if sum(range(x, 0, -1)) > maxY:
                    maxY = sum(range(x, 0, -1))
                    high_vel = vel

    print(high_vel, maxY)