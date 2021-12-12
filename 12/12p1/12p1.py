from copy import deepcopy

class Node:
    name = ''
    visited = 0
    sons = []

    def __init__(self, name) -> None: 
        self.name = name
        self.sons = []
        self.visited = 0
    
    def addSon(self, son) -> None: 
        if son not in self.sons and son.name != 'start': 
            self.sons.append(son)
    def getSons(self) -> list: return self.sons
    def isEqual(self, target) -> bool: return (self.name == target.name)

def exploreGraph(start, end, actualPath, pathslist):
    if start.isEqual(end) and actualPath not in pathslist:
        print(actualPath)
        pathslist.append(deepcopy(actualPath))
        return
    if not start.name.isupper() and start.visited == 1:
        return
    start.visited += 1
    for s in start.getSons():
        actualPath.append(s.name)
        exploreGraph(s, end, actualPath, pathslist)
        actualPath.pop()
    start.visited -= 1

with open("../input.txt") as f_input:
    nodes = {}
    for line in f_input:
        line = line.rstrip().split('-')
        if line[0] not in nodes: nodes[line[0]] = Node(line[0])
        if line[1] not in nodes: nodes[line[1]] = Node(line[1])
        nodes[line[0]].addSon(nodes[line[1]])
        nodes[line[1]].addSon(nodes[line[0]])

    pathlist = []
    exploreGraph(nodes['start'], nodes['end'], [], pathlist)
    print(len(pathlist))