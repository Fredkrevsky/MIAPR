import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from math import sqrt, inf
from random import randint

start_x = 0
start_y = 0
lines = []
rounds = []
triangles = []
rectangles = []

draw_round = False

def dist(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)    

def on_press(event):
    global start_point
    r = 50
    x = event.x
    y = event.y

    if draw_round:
        canvas.create_oval(x - r, y - r, x + r, y + r, width=3)
        rounds.append((x, y))
    else:
        start_point = (event.x, event.y)

def on_release(event):
    if not draw_round:
        end_point = (event.x, event.y)
        if dist(start_point, end_point) > 10:
            canvas.create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill="black", width=3)
            lines.append([start_point, end_point])

def clr():
    global canvas
    global lines
    global rounds
    global triangles
    global rectangles
    canvas.delete('all')
    lines = []
    triangles = []
    rounds = []
    rectangles = []

def set_round():
    global draw_round
    draw_round = not draw_round

def isTriangle(line1, line2, line3):
    tlines = [line2, line3]

    to_check = line1[0]
    dist1 = [dist(to_check, dot) for line in tlines for dot in line]
    min_dist = min(dist1)
    if min_dist > 10:
        return False
    
    min_index1 = dist1.index(min_dist)

    to_check = line1[1]
    dist2 = [dist(to_check, dot) for dot in tlines[1 - min_index1 // 2]]
    min_dist = min(dist2)
    if min_dist > 10:
        return False
    
    min_index2 = dist2.index(min_dist)
    ind1 = 0
    if (min_index1 == 0) or (min_index2 == 0):
        ind1 = 1
    ind2 = 0
    if (min_index1 == 2) or (min_index2 == 2):
        ind2 = 1
    return dist(tlines[0][ind1], tlines[1][ind2]) <= 10

def get_center(tlines):
    x = [dot[0] for line in tlines for dot in line]
    y = [dot[1] for line in tlines for dot in line]
    n = 2 * len(tlines)
    return (sum(x) / n, sum(y) / n)

def check_triangles():
    global lines
    global triangles
    for i in range(len(lines) - 2):
        for j in range(i + 1, len(lines) - 1):
            for k in range(j + 1, len(lines)):
                if isTriangle(lines[i].copy(), lines[j].copy(), lines[k].copy()):
                    triangles.append(get_center([lines[i], lines[j], lines[k]]))

def is_rect(line1, line2, line3, line4):
    tlines = [line1, line2, line3, line4]
    horiz = []
    vert = []
    
    for line in tlines:
        if abs(line[0][0] - line[1][0]) < 50:
            vert.append(line)
        elif abs(line[0][1] - line[1][1]) < 50:
            horiz.append(line)
        
    if (len(vert) != 2) or (len(horiz) != 2):
        return False
    if abs(abs(horiz[0][0][0] - horiz[0][1][0]) - abs(horiz[1][0][0] - horiz[1][1][0])) > 50:
        return False
    if abs(abs(vert[0][0][1] - vert[0][1][1]) - abs(vert[1][0][1] - vert[1][1][1])) > 50:
        return False
    return True

def check_rects():
    global lines
    global rectangles
    for i in range(len(lines) - 3):
        for j in range(i + 1, len(lines) - 2):
            for k in range(j + 1, len(lines) - 1):
                for l in range(k + 1, len(lines)):
                    if is_rect(lines[i].copy(), lines[j].copy(), lines[k].copy(), lines[l].copy()):
                        rectangles.append(get_center([lines[i], lines[j], lines[k], lines[l]]))



def israel():
    def rect1():
        global rectangles
        for rect in rectangles:
            if (abs(rect[0] - 450) < 50) and (abs(rect[1] - 50) < 50):
                return True
        return False

    def rect2():
        global rectangles
        for rect in rectangles:
            if (abs(rect[0] - 450) < 50) and (abs(rect[1] - 600) < 200):
                return True
        return False

    def triang():
        global triangles
        first = False
        second = False
        for elem in triangles:
            if (abs(elem[0] - 450) < 50) and (abs(elem[1] - 400) < 50):
                if not first:
                    first = True
                else:
                    second = True
        return first and second
    return rect1() and triang() and rect2()

def icecream():
    global rounds
    print(rounds)
    def ball1():
        global rounds
        for elem in rounds:
            if (abs(elem[0] - 400) < 25) and (abs(elem[1] - 250) < 25):
                return True
        return False

    def ball2():
        global rounds
        for elem in rounds:
            if (abs(elem[0] - 500) < 50) and (abs(elem[1] - 250) < 50):
                return True
        return False

    def ball3():
        global rounds
        for elem in rounds:
            if (abs(elem[0] - 450) < 50) and (abs(elem[1] - 200) < 50):
                return True
        return False

    def rozhok():
        global triangles
        for elem in triangles:
            if (abs(elem[0] - 450) < 50) and (abs(elem[1] - 360) < 50):
                return True
        return False
    
    if not ball1():
        showerror(title="Ошибка", message="Не найден левый шар")
        return False
    if not ball2():
        showerror(title="Ошибка", message="Не найден правый шар")
        return False
    if not ball3():
        showerror(title="Ошибка", message="Не найден верхний шар")
        return False
    if not rozhok():
        showerror(title="Ошибка", message="Не найден рожок")
        return False
    return True

def gen_ice():
    def ball1():
        global rounds
        r = 50
        dx = randint(0, 50) - 25
        dy = randint(0, 50) - 25
        x = 400 + dx
        y = 250 + dy
        canvas.create_oval(x - r, y - r, x + r, y + r, width=3)
        rounds.append((x, y))
        
    def ball2():
        global rounds
        r = 50
        dx = randint(0, 50) - 25
        dy = randint(0, 50) - 25
        x = 500 + dx
        y = 250 + dy
        canvas.create_oval(x - r, y - r, x + r, y + r, width=3)
        rounds.append((x, y))

    def ball3():
        global rounds
        r = 50
        dx = randint(0, 50) - 25
        dy = randint(0, 50) - 25
        x = 450 + dx
        y = 200 + dy
        canvas.create_oval(x - r, y - r, x + r, y + r, width=3)
        rounds.append((x, y))

    def rozhok():
        global triangles

        start_point = (350 + randint(0, 6) - 3, 300 + randint(0, 6) - 3)
        end_point = (450 + randint(0, 6) - 3, 550 + randint(0, 6) - 3)
        canvas.create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill="black", width=3)
        lines.append([start_point, end_point])
        
        start_point = (450 + randint(0, 6) - 3, 550 + randint(0, 6) - 3)
        end_point = (525 + randint(0, 6) - 3, 300 + randint(0, 6) - 3)
        canvas.create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill="black", width=3)
        lines.append([start_point, end_point])

        start_point = (525 + randint(0, 6) - 3, 300 + randint(0, 6) - 3)
        end_point = (350 + randint(0, 6) - 3, 300 + randint(0, 6) - 3)
        canvas.create_line(start_point[0], start_point[1], end_point[0], end_point[1], fill="black", width=3)
        lines.append([start_point, end_point])

    ball1()
    ball2()
    ball3()
    rozhok()

def gen_israel():
    return

def check():
    global lines
    #check_rects()
    check_triangles()

    #if israel():
        #showinfo(title="Успех", message="Это флаг Израиля")
    if icecream():
        showinfo(title="Успех", message="Это мороженое")
    else:
        showerror(title="Ошибка", message="Не удалось определить")
    

root = tk.Tk()
root.title("Рисование прямой на канвасе")
frame1 = tk.Frame(root)
frame1.pack()
btn_clr = tk.Button(frame1, width=20, text="Очистить canvas", command=clr)
btn_clr.pack(side=tk.LEFT)

btn_chk = tk.Button(frame1, width=20, text="Проверить", command=check)
btn_chk.pack(side=tk.LEFT)

btn_chk = tk.Button(frame1, width=20, text="Поменять режим", command=set_round)
btn_chk.pack(side=tk.LEFT)
btn_mor = tk.Button(frame1, width=30, text="Сгенерировать мороженное", command=gen_ice)
btn_mor.pack(side=tk.LEFT)
#btn_mor = tk.Button(frame1, width=30, text="Сгенерировать флаг Израиля", command=gen_israel)
#btn_mor.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=900, height=600)
canvas.pack()

canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<ButtonRelease-1>", on_release)

root.mainloop()

