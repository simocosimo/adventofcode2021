def foldUp(yvalss, yfold):
    for i in range(0, len(yvalss)):
        if yvalss[i] > yfold: yvalss[i] = (2 * yfold) - yvalss[i]

def foldLeft(xvalss, xfold):
    for i in range(0, len(xvalss)):
        if xvalss[i] > xfold: xvalss[i] = (2 * xfold) - xvalss[i]

with open("../input.txt") as f_input:
    xvals, yvals = [], []
    folds = []
    points = []
    for l in f_input:
        if l.rstrip() == '': break
        xvals.append(int(l.rstrip().split(',')[0]))
        yvals.append(int(l.rstrip().split(',')[1]))

    for l in f_input:
        if 'x' in l: folds.append(('x', int(l.rstrip().split('=')[1])))
        if 'y' in l: folds.append(('y', int(l.rstrip().split('=')[1])))

    for f in folds:
        if f[0] == 'x': foldLeft(xvals, f[1])
        if f[0] == 'y': foldUp(yvals, f[1])
    
    for i in range(0, len(yvals)):
        points.append((xvals[i], yvals[i]))
    
    mat = [[' ' if (x, y) not in points else '#' for x in range(0, max(xvals)+1)] for y in range(0, max(yvals)+1)]

    for l in mat:
        for c in l: print(c, end='')
        print("")