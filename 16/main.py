from functools import reduce


class Parser:
    def __init__(self, data):
        self.data = bin(int("1"+data, 16))[3:].rstrip("0")
        self.versions = 0
        self.pos = 0

        self.OPS = {
            0: lambda a: sum(a),
            1: lambda a: reduce(lambda b, c: b*c, a),
            2: lambda a: a[0] if len(a) == 1 else min(*a),
            3: lambda a: a[0] if len(a) == 1 else max(*a),
            5: lambda a: 1 if a[0] > a[1] else 0,
            6: lambda a: 1 if a[0] < a[1] else 0,
            7: lambda a: 1 if a[0] == a[1] else 0,
        }

    def read_packet(self):
        self.versions += self.read(3)
        tid = self.read(3)

        if tid == 4:
            value = ""
            while True:
                end = self.read(1)
                value += self.read(4, False)
                if end == 0:
                    return int(value, 2)
        else:
            subpkt = []
            if self.read(1) == 0:
                n = self.read(15)
                limit = self.pos+n

                while self.pos < limit:
                    subpkt.append(self.read_packet())
            else:
                for i in range(self.read(11)):
                    subpkt.append(self.read_packet())
            print(subpkt)
            return self.OPS[tid](subpkt)

    def read(self, n, convert=True):
        ret = self.data[self.pos:self.pos+n]
        self.pos += n
        return int(ret, 2) if convert else ret


with open("input.txt") as f:
    s = 0
    for line in f.read().split("\n"):
        p = Parser(line)
        s += p.read_packet()
    print(s)
