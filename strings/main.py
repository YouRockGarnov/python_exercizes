import string

# 9 13 32 126

def strings(filename, min_str_len=2):
    strings = []

    with open(filename, 'rb') as file:
        for line in file:
            norm_line = str()

            count = 0
            for norm_char in line:

                #print(char)
                #norm_char = int.from_bytes(char, byteorder='big')

                if norm_char >= 9 and norm_char <= 13 or norm_char >= 32 and norm_char <= 126:
                    norm_line += chr(norm_char)

                    count += 1
                else:
                    if norm_line != '' and count > min_str_len:
                        yield norm_line

                    norm_line = ''
                    count = 0

        if norm_line != '' and count > min_str_len:
            # strings.append(norm_line)
            yield norm_line

        return strings


print(strings('scoring_network_dump.bin'))