import re


def digits(text):
    match = re.findall('\d*, \d*, \d*', text)

    if text.count(',') != 2 or len(match) == 0:
        raise Exception

    match = [s.replace(' ', '') for s in text.split(',')]

    for num in match:
        if int(num) > 255 or int(num) < 0:
            raise Exception

    print(' '.join(match))


def hex_rgb(text):
    match = re.findall('#\w{6}', text)

    text = text.replace('#', '')
    text_list = list(text)

    length = len(text_list)
    text_list = [[text_list[i], text_list[i+1]] for i in range(0, length, 2)]

    for pair in text_list:
        pair = ''.join(pair)

        print(int(pair, 16), end=' ')


priority_of_colors = ['r', 'g', 'b']


def rgb(text):
    match = re.findall(r'\w{3}\(\d*, \d*, \d*\)', text)

    s = set(text[:3])
    if 'r' not in s or 'g' not in s or 'b' not in s or len(match) == 0:
        raise Exception

    match = re.findall('\d', text)

    result = str()
    for char in priority_of_colors:
        result += match[text.find(char)] + ' '

    result = result[:-1]
    print(result)


def rgb_perc(text):
    if text.count('%') != 3:
        raise Exception

    checking = re.findall('\(\d*%, \d*%, \d*%\)', text)

    if len(checking) == 0:
        raise Exception

    match = re.findall('\d', text)

    length = len(match)
    match = [int(match[i] + match[i + 1]) for i in range(0, length, 2)]

    result = str()
    for char in priority_of_colors:
        perc = int(match[text.find(char)])

        if perc > 100 or perc < 0:
            raise Exception

        result += str(int(perc * 255 / 100)) + ' '

    result = result[:-1]
    print(result)


def rgb_main(text):
    if '#' in text:
        return hex_rgb(text)
    elif '%' in text:
        return rgb_perc(text)
    elif '(' in text:
        return rgb(text)
    else:
        return digits(text)


def main():
    text = input()

    try:
        rgb_main(text)
    except Exception as e:
        print('ERROR')


main()
