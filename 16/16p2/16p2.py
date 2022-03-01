from functools import reduce
from treelib import Tree

class Packet:

    staticID = 0

    def __init__(self, binary) -> None:
        self.binarypacket = binary
        self.subpackets_number = 0
        self.subpackets_len = 0
        self.value = -1
        self.length = -1
        # 0 = next 15 bits are lenght of sub packets
        # 1 = next 11 bits are number of sub packets contained
        self.optype = 0
        self.operation = '+'
        Packet.staticID += 1
        self.res = 0;
        self.innerValues = []

        self.version = int(self.binarypacket[0:3], 2)
        self.id = int(self.binarypacket[3:6], 2)
        self.optype = int(self.binarypacket[6], 2)
        if self.id == 4: self.type = "literate"
        else: self.type = "operator"
        self.stringTag = self.type + str(Packet.staticID)

        if self.optype == 1: self.subpackets_number = int(self.binarypacket[7:7+11], 2)
        else: self.subpackets_len = int(self.binarypacket[7:7+15], 2)

        if self.type == "literate": self.literateParsing()

    def literateParsing(self):
        exit = False
        i = 7
        part = ""
        while not exit:
            part += self.binarypacket[i:i+4]
            if self.binarypacket[i-1] == '0': exit = True
            else: i += 5
        self.value = int(part, 2)
        self.length = i + 4
                
def getBinaryPacket(string, dictionary):
    binarypacket = ""
    for b in string: binarypacket += dictionary[b]
    return binarypacket

def treeBuilding(binarypacket, tree, parent='') -> int:
    packet = Packet(binarypacket)
    llen = packet.subpackets_len
    if parent == '': tree.create_node(tag=packet.stringTag, identifier=packet.stringTag, data=packet)
    else: tree.create_node(tag=packet.stringTag, identifier=packet.stringTag, data=packet, parent=parent)
    if packet.type == "literate":
        if parent != '': tree.get_node(parent).data.innerValues.append(packet.value)
        return packet.length
    if packet.optype == 1:
        localLen = 18
        for _ in range(packet.subpackets_number): localLen += treeBuilding(binarypacket[localLen:], tree, parent=packet.stringTag)
    elif packet.optype == 0:
        localLen = 22
        while llen > 0:
            l = treeBuilding(binarypacket[localLen:], tree, parent=packet.stringTag)
            localLen += l
            llen -= l

    if packet.id == 0: packet.res = sum(packet.innerValues)
    elif packet.id == 1: packet.res = reduce((lambda x, y: x * y), packet.innerValues)
    elif packet.id == 2: packet.res = min(packet.innerValues)
    elif packet.id == 3: packet.res = max(packet.innerValues)
    elif packet.id == 5: packet.res = (packet.innerValues[0] > packet.innerValues[1])
    elif packet.id == 6: packet.res = (packet.innerValues[0] < packet.innerValues[1])
    else: packet.res = (packet.innerValues[0] == packet.innerValues[1])
    if parent != '': tree.get_node(parent).data.innerValues.append(packet.res)
    return localLen

with open("../input.txt", "r") as f_input:
    packetstring = f_input.readline().rstrip()
    f_input.readline()
    translation = {}
    tree = Tree()

    for l in f_input.readlines():
        o, t = l.rstrip().split(" = ")
        translation[o] = t

    treeBuilding(getBinaryPacket(packetstring, translation), tree)
    tree.show()
    print(int(tree.get_node('operator1').data.res))