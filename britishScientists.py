import re
import random

def old(text, letters_to_shuffle_nm):
    # match = re.split(r'\W(?!\s)', 'my brother is lol and my mam too')
    # print(match)

    words = text.split()

    result_text = []
    for word in words:
        first_char = word[0]
        second_char = word[-1]

        if len(word) <= 1:
            second_char = ''

        centre = [x for x in word[1:-1]]
        random.shuffle(centre[-letters_to_shuffle_nm])
        if centre == None: centre=''

        res = first_char + ''.join(centre) + second_char
        result_text.append(res)

    return ' '.join(result_text)

def shuffle(word, letters_to_shuffle_nm):
    first_char = word[0]
    second_char = word[-1]

    if len(word) <= 1:
        second_char = ''

    centre = [x for x in word[1:-1]]
    for_shuffle = centre[-letters_to_shuffle_nm:]
    random.shuffle(for_shuffle)

    centre[-letters_to_shuffle_nm:] = for_shuffle

    if centre == None: centre = ''

    res = first_char + ''.join(centre) + second_char
    return res

def prepare_line(line, letters_to_shuffle_nm):
    match = re.findall(r'\S+', line)
    # print(match)

    result = []
    for expr in match:
        word = re.findall(r'\w+', expr)

        if len(word) == 0:
            result.append(expr)
        else:
            word = word[0]
            shuffled_word = shuffle(word, letters_to_shuffle_nm)

            line = line.replace(word, shuffled_word)

            #result.append(re.sub(r'\w+', word, expr))

    return line

def prepare_to_british_scientists(text, letters_to_shuffle_nm):
    if letters_to_shuffle_nm == 0:
        return text

    text = text.split('\n')

    result = list()
    for line in text:
        result.append(prepare_line(line, letters_to_shuffle_nm))

    return '\n'.join(result)


# text = list()
#
# try:
#     while True:
#         line = input()
#         text.append(line)
#
# except EOFError as e:
#     print ('\n'.join(text))

text = '''The Zen of Python, by Tim Peters

Прекрасное лучше уродливого.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

print(prepare_to_british_scientists(text, 3))