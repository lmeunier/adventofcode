with open("input", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]


class Packet:
    def __init__(self, version, type):
        self.version = version
        self.type = type


class Transmission:
    def __init__(self, hex_string=None, binary_string=None):
        if hex_string is not None:
            self.binary_string = ""
            for c in hex_string:
                self.binary_string += format(int(c, base=16), '04b')
        if binary_string is not None:
            self.binary_string = binary_string

    def extract_bits(self, n):
        extracted_bits = self.binary_string[:n]
        self.binary_string = self.binary_string[n:]
        return extracted_bits

    def next_packet(self):
        packet_version = int(self.extract_bits(3), base=2)
        packet_type = int(self.extract_bits(3), base=2)
        p = Packet(packet_version, packet_type)

        if p.type == 4:
            value = ""
            while True:
                group = self.extract_bits(5)
                value += group[1:]
                if group[0] == "0":
                    break
            p.value = int(value, base=2)
        else:
            p.lenght_type_id = int(self.extract_bits(1), base=2)

            if p.lenght_type_id == 0:
                p.sub_packets_length = int(self.extract_bits(15), base=2)
                sub_transmission = Transmission(binary_string=self.extract_bits(p.sub_packets_length))
                p.sub_packets = list(sub_transmission.all_packets())
            if p.lenght_type_id == 1:
                p.sub_packets_number = int(self.extract_bits(11), base=2)
                p.sub_packets = []
                for i in range(p.sub_packets_number):
                    p.sub_packets.append(self.next_packet())

        return p

    def has_next_packet(self):
        return "0" * len(self.binary_string) != self.binary_string

    def all_packets(self):
        while self.has_next_packet():
            p = self.next_packet()
            yield(p)


transmission = Transmission(hex_string=lines[0])
packets = list(transmission.all_packets())


def calculate(packet):
    if packet.type == 0:
        # sum
        result = 0
        for p in packet.sub_packets:
            result += calculate(p)
        return result

    if packet.type == 1:
        # product
        result = 1
        for p in packet.sub_packets:
            result *= calculate(p)
        return result

    if packet.type == 2:
        # min
        return min([calculate(p) for p in packet.sub_packets])

    if packet.type == 3:
        # max
        return max([calculate(p) for p in packet.sub_packets])

    if packet.type == 4:
        # value
        return packet.value

    if packet.type == 5:
        # greater than
        r0 = calculate(packet.sub_packets[0])
        r1 = calculate(packet.sub_packets[1])
        return 1 if r0 > r1 else 0

    if packet.type == 6:
        # less than
        r0 = calculate(packet.sub_packets[0])
        r1 = calculate(packet.sub_packets[1])
        return 1 if r0 < r1 else 0

    if packet.type == 7:
        # equal
        r0 = calculate(packet.sub_packets[0])
        r1 = calculate(packet.sub_packets[1])
        return 1 if r0 == r1 else 0


print(calculate(packets[0]))
