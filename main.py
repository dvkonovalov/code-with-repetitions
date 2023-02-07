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
