import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from math import inf

SIZE = 4

distances = [
    [0,   5,   0.5, 2],
    [5,   0,   1,   0.6],
    [0.5, 1,   0,   2.5],
    [2,   0.6,   2.5, 0]
]

max_s = True

if (max_s):
    for i in range(4):
        for j in range(4):
            if distances[i][j] != 0:
                distances[i][j] = 1 / distances[i][j]

groups = []

def find_min():
    min_1 = 0
    min_2 = 0
    minvalue = inf
    for i in range(0, SIZE):
        for j in range(i+1, SIZE):
            if distances[i][j] < minvalue:
                minvalue = distances[i][j]
                min_1 = i
                min_2 = j
    return min_1, min_2, minvalue

def new_value(indexes, ind):
    mins = []
    for i in indexes:
        mins.append(distances[i][ind])
    return min(mins)


def is_continue():
    count = 0
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if distances[i][j] != inf:
                count += 1
                if count > 1:
                    return True
    return False

index = 1
while is_continue():
    min_i, min_j, min_v = find_min()
    temp = []
    new_grp = [min_i, min_j, float(min_v), index]
    index += 1
    groups.append(new_grp)
    t3 = []
    for i in range(SIZE):
        t1 = []
        for j in range(SIZE):
            if j == min_i or j == min_j or i == min_i or i == min_j:
                t1.append(inf)
            else:
                t1.append(distances[i][j])
        if i == min_i or i == min_j:
            t1.append(inf)
        else:
            t1.append(new_value([min_i, min_j], i))
        t3.append(t1[-1])
        temp.append(t1)
    t3.append(0)
    temp.append(t3)
    SIZE += 1
    distances = temp

plt.figure(figsize=(5, 5))
plt.title('Результирующее иерархическое дерево')
plt.xlabel('Индекс x')
plt.ylabel('Расстояние')
dendrogram(groups)
plt.show()