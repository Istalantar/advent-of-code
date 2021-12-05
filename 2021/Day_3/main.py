from myFunctions import my_input_list


def main():
    content = my_input_list("input.txt")

    part_one(content)
    part_two(content)


def part_one(content):
    bit_0 = [str]  # LSB
    bit_1 = [str]
    bit_2 = [str]
    bit_3 = [str]
    bit_4 = [str] 
    bit_5 = [str]
    bit_6 = [str]
    bit_7 = [str]
    bit_8 = [str]
    bit_9 = [str]
    bit_10 = [str]
    bit_11 = [str]  # MSB

    for report in content:
        bit_0.append(report[11])
        bit_1.append(report[10])
        bit_2.append(report[9])
        bit_3.append(report[8])
        bit_4.append(report[7])
        bit_5.append(report[6])
        bit_6.append(report[5])
        bit_7.append(report[4])
        bit_8.append(report[3])
        bit_9.append(report[2])
        bit_10.append(report[1])
        bit_11.append(report[0])

    gamma = '0' if bit_11.count('0') > bit_11.count('1') else '1'
    gamma += '0' if bit_10.count('0') > bit_10.count('1') else '1'
    gamma += '0' if bit_9.count('0') > bit_9.count('1') else '1'
    gamma += '0' if bit_8.count('0') > bit_8.count('1') else '1'
    gamma += '0' if bit_7.count('0') > bit_7.count('1') else '1'
    gamma += '0' if bit_6.count('0') > bit_6.count('1') else '1'
    gamma += '0' if bit_5.count('0') > bit_5.count('1') else '1'
    gamma += '0' if bit_4.count('0') > bit_4.count('1') else '1'
    gamma += '0' if bit_3.count('0') > bit_3.count('1') else '1'
    gamma += '0' if bit_2.count('0') > bit_2.count('1') else '1'
    gamma += '0' if bit_1.count('0') > bit_1.count('1') else '1'
    gamma += '0' if bit_0.count('0') > bit_0.count('1') else '1'

    epsilon = '0' if bit_11.count('0') < bit_11.count('1') else '1'
    epsilon += '0' if bit_10.count('0') < bit_10.count('1') else '1'
    epsilon += '0' if bit_9.count('0') < bit_9.count('1') else '1'
    epsilon += '0' if bit_8.count('0') < bit_8.count('1') else '1'
    epsilon += '0' if bit_7.count('0') < bit_7.count('1') else '1'
    epsilon += '0' if bit_6.count('0') < bit_6.count('1') else '1'
    epsilon += '0' if bit_5.count('0') < bit_5.count('1') else '1'
    epsilon += '0' if bit_4.count('0') < bit_4.count('1') else '1'
    epsilon += '0' if bit_3.count('0') < bit_3.count('1') else '1'
    epsilon += '0' if bit_2.count('0') < bit_2.count('1') else '1'
    epsilon += '0' if bit_1.count('0') < bit_1.count('1') else '1'
    epsilon += '0' if bit_0.count('0') < bit_0.count('1') else '1'

    print(int(gamma, 2) * int(epsilon, 2))


def part_two(content):
    oxy_bits = [str]
    co2_bits = [str]
    oxygen = content.copy()
    co2 = content.copy()

    num_bits = 12
    for i in range(num_bits):
        for report in oxygen:
            oxy_bits.append(report[i])            
        for report in co2:
            co2_bits.append(report[i])

        if oxy_bits.count('1') > oxy_bits.count('0') or oxy_bits.count('1') == oxy_bits.count('0'):
            oxygen = get_numbers(oxygen, i, '1') if len(oxygen) > 1 else oxygen
        else:
            oxygen = get_numbers(oxygen, i, '0') if len(oxygen) > 1 else oxygen

        if co2_bits.count('0') < co2_bits.count('1') or co2_bits.count('1') == co2_bits.count('0'):
            co2 = get_numbers(co2, i, '0') if len(co2) > 1 else co2
        else:
            co2 = get_numbers(co2, i, '1') if len(co2) > 1 else co2

        oxy_bits.clear()
        co2_bits.clear()

    print(int(oxygen[0], 2) * int(co2[0], 2))
        

def get_numbers(my_list, my_index, my_number) -> [str]:
    res_list = []
    
    for number in my_list:
        if number[my_index] == my_number:
            res_list.append(number)        
    
    return res_list


if __name__ == '__main__':
    main()
