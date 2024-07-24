import tkinter as tk
from math import exp, sqrt, pi
from tkinter.messagebox import showerror

mean1 = 150
std1 = 80
mean2 = 300
std2 = 50

def p(x, mean, std, prob):
    return 1 / (std * sqrt(2 * pi)) * exp(-0.5 * ((x - mean) / std)**2) * prob

def get_input():
    try:
        p1 = float(ent_mat.get())
        p2 = float(ent_sig.get())
    except:
        showerror(title="Error", text="Введите числа")
        return 
    draw_dots(p1, p2)

def get_x(p1, p2):
    x = 250
    n = 2
    for _ in range(30):
        if p(x, mean1, std1, p1) > p(x, mean2, std2, p2):
            x = x + 250 / n
        else:
            x = x - 250 / n
        n = n * 2
    return x

def integrate(mean, std, a, b, prob):
    n = 100
    dx = (b - a) / n
    return sum(p(a + i * dx, mean, std, prob) for i in range(n)) * dx

def draw_dots(p1, p2):
    global ent_mat
    global ent_sig
    global canvas
    global ent_LT
    global ent_PO
    global ent_SO

    canvas.delete("all")

    bigX = get_x(p1, p2)

    x0 = 0
    y0 = 500
    for i in range(500):
        x = i
        y = -40000 * p(i, mean1, std1, p1) + 300
        canvas.create_line(x0, y0, x, y, fill="blue", width=3)
        x0 = x
        y0 = y

    x0 = 0
    y0 = 500
    for i in range(500):
        x = i
        y = -40000 * p(i, mean2, std2, p2) + 300
        canvas.create_line(x0, y0, x, y, fill="green", width=3)
        x0 = x
        y0 = y

    canvas.create_line(bigX, 50, bigX, 450, fill="red", width=3)
    temp1 = integrate(mean2, std2, 0, bigX, p2)
    temp2 = integrate(mean1, std1, bigX, 500, p1)

    ent_LT.config(state="normal")
    ent_PO.config(state="normal")
    ent_SO.config(state="normal")
    ent_LT.delete(0, tk.END)
    ent_PO.delete(0, tk.END)
    ent_SO.delete(0, tk.END)
    ent_LT.insert(0, str(temp1)[:7])
    ent_PO.insert(0, str(temp2)[:7])
    ent_SO.insert(0, str(temp1 + temp2)[:7])
    ent_LT.config(state="readonly")
    ent_PO.config(state="readonly")
    ent_SO.config(state="readonly")

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("500x800")
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()

    frame1 = tk.Frame(window, height=50, width=500)
    frame1.pack()
    lbl_mat = tk.Label(frame1, width=20, text="Вероятность №1:", font=(None, 15))
    lbl_mat.pack(side=tk.LEFT)
    ent_mat = tk.Entry(frame1, width=10, font=(None, 15))
    ent_mat.pack(side=tk.LEFT)

    frame2 = tk.Frame(window, height=50, width=500)
    frame2.pack()
    lbl_sig = tk.Label(frame2, width=20, text="Вероятность №2:", font=(None, 15))
    lbl_sig.pack(side=tk.LEFT)
    ent_sig = tk.Entry(frame2, width=10, font=(None, 15))
    ent_sig.pack(side=tk.LEFT)

    frame3 = tk.Frame(window, height=50, width=500)
    frame3.pack()
    lbl_LT = tk.Label(frame3, width=20, text="Ложная тревога", font=(None, 15))
    lbl_LT.pack(side=tk.LEFT)
    ent_LT = tk.Entry(frame3, width=10, font=(None, 15))
    ent_LT.config(state="readonly")
    ent_LT.pack(side=tk.LEFT)

    frame4 = tk.Frame(window, height=50, width=500)
    frame4.pack()
    lbl_PO = tk.Label(frame4, width=20, text="Пропуск обнаружения", font=(None, 15))
    lbl_PO.pack(side=tk.LEFT)
    ent_PO = tk.Entry(frame4, width=10, font=(None, 15))
    ent_PO.config(state="readonly")
    ent_PO.pack(side=tk.LEFT)

    frame5 = tk.Frame(window, height=50, width=500)
    frame5.pack()
    lbl_SO = tk.Label(frame5, width=20, text="Суммарная ошибка", font=(None, 15))
    lbl_SO.pack(side=tk.LEFT)
    ent_SO = tk.Entry(frame5, width=10, font=(None, 15))
    ent_SO.config(state="readonly")
    ent_SO.pack(side=tk.LEFT)

    btn_draw = tk.Button(window, width=15, text="Рассчитать", font=(None, 15), command=get_input)
    btn_draw.pack()
    window.mainloop()