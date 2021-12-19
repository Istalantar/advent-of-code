import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402

tm = ''  # Transmition string


class Literal:
    def __init__(self):
        self.raw = ''
        self.version = None
        self.pid = None  # packet type ID
        self.length = 0
        self.value = None

    def __repr__(self):
        return self.raw


class Operator:
    def __init__(self):
        self.raw = ''
        self.version = None
        self.pid = None  # packet type ID
        self.length = 0
        self.value = None
        self.sub_packets = []

    def __repr__(self):
        return self.raw


def main():
    content = my_input_string("input.txt")

    print(part_one(content))
    print(part_two(content))
    print("(It's not '9533881890502')")


def part_one(content) -> int:
    global tm
    bit_len = len(content) * 4
    tm = bin(int(content, 16))[2:]
    if len(tm) < bit_len:  # fill with leading zeros
        tm = '0' * (4 - (len(tm) % 4)) + tm
    packets = []

    # get all packets
    while len(tm) >= 11:  # 11 bits is the minimum length for a package
        packets.append(get_packet())

    # calculate version sum
    v_sum = 0
    for packet in packets:
        v_sum += get_version_sum(packet)

    return v_sum


def part_two(content) -> int:
    global tm
    bit_len = len(content) * 4
    tm = bin(int(content, 16))[2:]
    if len(tm) < bit_len:  # fill with leading zeros
        tm = '0' * (4 - (len(tm) % 4)) + tm
    # if hex value starts with zero, four more zeros have to be added to binary,
    # because they get cut off in conversion
    if content[0] == '0':
        tm = '0' * 4 + tm
    packets = []

    # get all packets
    while len(tm) >= 11:  # 11 bits is the minimum length for a package
        packets.append(get_packet())

    return packets[0].value


def get_packet():
    global tm

    if len(tm) >= 11:
        pid = int(tm[3:6], 2)
        if pid == 4:
            return get_literal()
        else:
            return get_operator()


def get_literal() -> Literal:
    global tm
    literal = Literal()
    is_packet_end = False
    literal.version = int(tm[:3], 2)
    literal.pid = int(tm[3:6], 2)
    literal.raw = tm[:6]
    tm = tm[6:]
    literal.length = 6

    value = ''
    while not is_packet_end:
        if tm[0] == '1':  # not the last group
            value += tm[1:5]
            literal.raw += tm[0:5]
            tm = tm[5:]
            literal.length += 5
        elif tm[0] == '0':  # the last group
            value += tm[1:5]
            literal.raw += tm[0:5]
            tm = tm[5:]
            literal.length += 5

            # save literal value
            literal.value = int(value, 2)

            is_packet_end = True

    return literal


def get_operator() -> Operator:
    global tm
    operator = Operator()
    is_packet_end = False
    operator.version = int(tm[:3], 2)
    operator.pid = int(tm[3:6], 2)
    operator.raw = tm[:6]
    tm = tm[6:]
    operator.length = 6

    while not is_packet_end:
        if tm[0] == '0':  # length indicator
            is_sub_packet_end = False
            sub_length_max = int(tm[1:16], 2)
            sub_length_is = 0
            operator.raw += tm[:16]
            tm = tm[16:]
            operator.length += 16

            while not is_sub_packet_end:
                sub_packet = get_packet()
                operator.sub_packets.append(sub_packet)
                operator.raw += sub_packet.raw
                try:
                    operator.length += sub_packet.length
                except AttributeError:
                    print('bla')

                sub_length_is += sub_packet.length

                # find sub-packet end
                if sub_length_max == sub_length_is:  # all sub packets found
                    is_sub_packet_end = True
                elif (sub_length_max - sub_length_is) < 11:
                    # not enough space for another sub packet, but length does not meet the requirement
                    raise Exception('SubPacketLenghtError')
            is_packet_end = True
        elif tm[0] == '1':  # sub-packet indicator
            sub_packet_count_max = int(tm[1:12], 2)
            tm = tm[12:]
            operator.raw += tm[:12]
            operator.length += 12

            for i in range(sub_packet_count_max):
                sub_packet = get_packet()
                operator.sub_packets.append(sub_packet)
                operator.raw += sub_packet.raw
                operator.length += sub_packet.length

            is_packet_end = True

    # calculate value
    if operator.pid == 0:
        operator.value = get_sum(operator.sub_packets)
    elif operator.pid == 1:
        operator.value = get_product(operator.sub_packets)
    elif operator.pid == 2:
        operator.value = min(get_all_vals(operator.sub_packets))
    elif operator.pid == 3:
        operator.value = max(get_all_vals(operator.sub_packets))
    elif operator.pid == 5:
        operator.value = get_greater(operator)
    elif operator.pid == 6:
        operator.value = get_lesser(operator)
    elif operator.pid == 7:
        operator.value = get_equal(operator)
    
    return operator


def get_version_sum(packet) -> int:
    v_sum = 0

    v_sum += packet.version
    if isinstance(packet, Operator):
        for sub in packet.sub_packets:
            v_sum += get_version_sum(sub)

    return v_sum


def get_sum(packets) -> int:
    val_sum = 0

    for packet in packets:
        val_sum += packet.value

    return val_sum


def get_product(packets) -> int:
    val_prod = 1

    for packet in packets:
        val_prod *= packet.value

    return val_prod


def get_all_vals(packets):
    vals = []

    for packet in packets:
        vals.append(packet.value)
    
    return vals


def get_greater(packet) -> int:
    sub1 = packet.sub_packets[0]
    sub2 = packet.sub_packets[1]
    packet.value = 1 if sub1.value > sub2.value else 0

    return packet.value


def get_lesser(packet) -> int:
    sub1 = packet.sub_packets[0]
    sub2 = packet.sub_packets[1]
    packet.value = 1 if sub1.value < sub2.value else 0

    return packet.value


def get_equal(packet) -> int:
    sub1 = packet.sub_packets[0]
    sub2 = packet.sub_packets[1]
    packet.value = 1 if sub1.value == sub2.value else 0

    return packet.value


if __name__ == '__main__':
    main()
