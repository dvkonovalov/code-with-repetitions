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
    answer = ''
    summa = 0
    for i in y:
        summa += p
        if (summa-1.0<0.001):
            answer += i
        else:
            summa -= 1
            answer += str((int(i) + 1) % 2)
    return answer


c = repeat_encoding('10101', 5)
print(c)
c = binary_channel(0.34, c)
print(c)
c = repeat_decoding(c, 5)
print(c)