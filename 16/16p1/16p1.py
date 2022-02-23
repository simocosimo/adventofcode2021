class Packet:

    def __init__(self, dictionary, packetString='', binary='') -> None:
        self.packetstring = packetString
        self.binarypacket = ""
        self.subpackets = []
        self.value = -1
        # 0 = next 15 bits are lenght of sub packets
        # 1 = next 11 bits are number of sub packets contained
        self.optype = 0

        for b in self.packetstring: self.binarypacket += dictionary[b]
        self.version = int(self.binarypacket[0:3], 2)
        self.id = int(self.binarypacket[3:6], 2)
        self.optype = int(self.binarypacket[6], 2)
        if self.id == 4: self.type = "literate"
        else: self.type = "operator"

        # parsing if literate value
        if self.type == "literate": self.literateParsing()
    
        if self.type == "operator":
            if self.optype == 1:
                subpn = int(self.binarypacket[7:7+11], 2)
                

    def literateParsing(self):
        exit = False
        i = 7
        part = ""
        while not exit:
            part += self.binarypacket[i:i+4]
            if self.binarypacket[i-1] == '0': exit = True
            else: i += 5
        self.value = int(part, 2)
                


with open("../test.txt", "r") as f_input:
    packetstring = f_input.readline().rstrip()
    f_input.readline()
    translation = {}

    for l in f_input.readlines():
        o, t = l.rstrip().split(" = ")
        translation[o] = t

    packetstring = "D2FE28"
    p = Packet(translation, packetString=packetstring)
    print(f"Packet string is {p.packetstring}")
    print(f"Packet binary is {p.binarypacket}")
    print(f"Packet type: {p.type} - Version: {p.version} - ID: {p.id}")
    print(f"Packet value is {p.value if p.value != -1 else 'not a literate packet'}")
    
    