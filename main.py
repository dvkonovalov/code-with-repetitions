import random
from collections import Counter


def repeat_encoding(x, s):
    answer = ''
    for i in x:
        answer += i * s
    return answer


def repeat_decoding(y, s):
    answer = ''
    y = str(y)
    for i in range(len(y) // s):
        fragment = Counter(y[i * s:(i + 1) * s])
        answer += fragment.most_common(1)[0][0]
    return answer


def binary_channel(p, y):
    errors = []
    for i in range(round(p*len(y))):
        place = random.randint(0,len(y)-1)
        while (place in errors):
            place = random.randint(0, len(y) - 1)
        errors.append(place)
        y = y[:place] + str((int(y[place])+1)%2) + y[place+1:]
    return y


c = repeat_encoding('10110', 5)
print(c)
c = binary_channel(0.05, c)
print(c)
c = repeat_decoding(c, 5)
print(c)