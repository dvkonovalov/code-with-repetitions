from random import randint
from collections import Counter
import matplotlib.pyplot as plt


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
        place = randint(0,len(y)-1)
        while (place in errors):
            place = randint(0, len(y) - 1)
        errors.append(place)
        y = y[:place] + str((int(y[place])+1)%2) + y[place+1:]
    return y


def first_grafic(count):
    x = []
    y = []
    stroka = ''
    for i in range(count):
        stroka += str(randint(0,1))
        send_stroka = repeat_decoding(binary_channel(0.3, repeat_encoding(stroka, 3)), 3)
        summa = 0
        for j in range(i+1):
            if (stroka[j]!=send_stroka[j]):
                summa += 1
        if (summa!=0):
            y.append(summa)
            x.append(i + 1)
    plt.plot(x, y)
    plt.title('График 1')
    plt.ylabel('Количество ошибок')
    plt.xlabel('Количество символов в строке')
    plt.show()


def second_grafic(shag):
    p = 0
    x = []
    y = []
    stroka = ''
    for i in range(100):
        stroka += str(randint(0,1))
    while (p<1.0):
        send_stroka = repeat_decoding(binary_channel(p, repeat_encoding(stroka, 5)), 5)
        summa = 0
        for i in range(100):
            if (stroka[i]!=send_stroka[i]):
                summa += 1
        if (summa!=0):
            y.append(summa)
            x.append(p)
        p += shag
    plt.plot(x, y)
    plt.title('График 2')
    plt.ylabel('Количество ошибок')
    plt.xlabel('Вероятность ошибки')
    plt.show()

def third_grafic(maximum):
    x = []
    y = []
    stroka = ''
    for i in range(100):
        stroka += str(randint(0,1))
    for s in range(1, maximum+1):
        send_stroka = repeat_decoding(binary_channel(0.3, repeat_encoding(stroka, s)), s)
        summa = 0
        for i in range(100):
            if (stroka[i]!=send_stroka[i]):
                summa += 1
        if (summa!=0):
            y.append(summa)
            x.append(s)
    plt.plot(x, y)
    plt.title('График 3')
    plt.ylabel('Количество ошибок')
    plt.xlabel('Количество повторений')
    plt.show()



c = repeat_encoding('10110', 5)
print(c)
c = binary_channel(0.05, c)
print(c)
c = repeat_decoding(c, 5)
print(c)
first_grafic(100)
second_grafic(0.05)
third_grafic(100)