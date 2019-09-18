import numpy as np

data = [[2, 79], [3, 85], [4, 97], [5, 92]]

x = [i[0] for i in data]
y = [i[1] for i in data]

mx = np.mean(x)
my = np.mean(y)


def bottom():
    b = sum([(mx - i) ** 2 for i in x])
    return b
    """for j in range(len(x)):
        SUM = SUM + (x[j] - mx) ** 2
    return SUM"""


def top():
    s = 0
    for i in range(len(x)):
        s = s + ((x[i] - mx) * (y[i] - my))
    return s


bottom = bottom()
top = top()
print("분자 : ", top)
print("분모 : ", bottom)


a = top / bottom
b = my - (mx * a)
print("기울기 : ", a)
print("y 절편 : ", b)
