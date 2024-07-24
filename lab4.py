import tkinter as tk
from tkinter.messagebox import showerror

test = [(0, 0, 1),  
        (1, 1, 1),  
        (-1, 1, 1),
        (-1, -1, 0),
        (2, 2, 0),
        (-5, 0, 4),
        (3, 2, 1),
        (-5, -6, 3),
        (9, 1, -9),
        (2, -7, -6)] 

tuple_len = 3

def get_dist(elem, w):
    return sum(elem[i] * w[i] for i in range(tuple_len))

def dec(w, x, c):
    return tuple(w[i] - c * x[i] for i in range(tuple_len))

def inc(w, x, c):
    return tuple(w[i] + c * x[i] for i in range(tuple_len))

def norm(vector):
    hypot = sum(x ** 2 for x in vector) ** 0.5
    if hypot == 0:
        return 0
    return tuple(x / hypot for x in vector)



print("Начальные классы:")
for i in range(len(test)):
    print(test[i])
print("\n")

def get_data():
    global ent_mat
    try:
        n = int(ent_mat.get())
    except:
        n = 0
        raise ValueError
    return n

def show_result(w, need_to_break):
    global result
    result.delete("1.0", tk.END)
    if need_to_break:
        res = "Вычисления сошлись\n"
    else:
        res = "Вычисления не сошлись\n"

    result.insert("1.0", res)

    text = ""
    
    for t in range(len(w)):
        res_text = [f"{w[t][i]}x{i+1}" for i in range(len(w[t]))]
        res_text = " + ".join(res_text)
        text += res_text + "\n"
    
    result.insert("2.0", text)

def algorythm():
    try:
        classes_len = get_data()
    except:
        return

    max_iter = 1000

    w = [([0] * tuple_len)] * classes_len
    c = 1

    for _ in range(max_iter):
        need_to_break = True
        for i in range(classes_len):
            dist = [get_dist(test[i], w[j]) for j in range(classes_len)]
            curr_dist = dist[i]
            need_to_inc = False
            for j in range(classes_len):
                if i != j:
                    if dist[j] >= curr_dist:
                        need_to_inc = True
                        need_to_break = False
                        w[j] = dec(w[j], test[i], c)
            if need_to_inc:
                w[i] = inc(w[i], test[i], c)
        if need_to_break:
            break


    show_result(w, need_to_break)

    print("Конечные веса:")
    for i in range(len(w)):
        print(w[i])



if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("500x600")
    frame1 = tk.Frame(window, height=500, width=500)
    frame1.pack()
    result = tk.Text(frame1, height=15, width=40, font=(None, 15))
    result.pack()

    frame2 = tk.Frame(window, height=50, width=500)
    frame2.pack()
    lbl_mat = tk.Label(frame2, width=30, text="Количество классов (max 10):", font=(None, 15))
    lbl_mat.pack(side=tk.LEFT)
    ent_mat = tk.Entry(frame2, width=10, font=(None, 15))
    ent_mat.pack(side=tk.LEFT)

    frame2 = tk.Frame(window, height=50, width=500)
    frame2.pack()

    btn_draw = tk.Button(window, width=15, text="Рассчитать", font=(None, 15), command=algorythm)
    btn_draw.pack()
    window.mainloop()


