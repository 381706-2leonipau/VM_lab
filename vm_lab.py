import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
plt.rcParams['axes.facecolor'] = '#ebf4fa'
plt.rcParams['figure.facecolor'] = '#85ceff'

def x_func(x, y, a, c):
    value = float((a - c * y) * x)
    return value


def y_func(x, y, b, d):
    value = float((-b + d * x) * y)
    return value

#runge kutta 4th order
def Runge_Kutt(x0,y0,n,h):
    x.append(x0)
    y.append(y0)
    t0 = 0.
    i = 0
    yt = 0
    xt = 0
    while(t0 < n):
        k1_y = h * y_func(x[i], y[i], b, d)
        kx = x[i] + h / 2
        y1 = y[i] + k1_y / 2
        k2_y = h * y_func(kx, y1, b, d)
        y1 = y[i] + k2_y / 2
        k3_y = h * y_func(kx, y1, b, d)
        kx = kx + h / 2
        y1 = y[i] + k3_y
        k4_y = h * y_func(kx, y1, b, d)
        yt = y[i] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        y.append(yt)

        k1_x = h * x_func(x[i], y[i], a, c)
        kx = x[i] + h / 2
        y1 = y[i] + k1_x / 2
        k2_x = h * x_func(kx, y1, a, c)
        y1 = y[i] + k2_x / 2
        k3_x = h * x_func(kx, y1, a, c)
        kx = kx + h / 2
        y1 = y[i] + k3_x
        k4_x = h * x_func(kx, y1, a, c)
        xt = x[i] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        x.append(xt)
        t0+=h
        i+=1

def addGraphPhase(graph_axes, x, y):
     graph_axes.plot(x, y)
     plt.draw()

if __name__ == '__main__':
    x = list()
    y = list()

    def onButtonAddClicked(event):
        global graph_axes, x, y
        global a, c
        global b, d
        global x0, y0, n, h
        Runge_Kutt(x0,y0,n,h)
        addGraphPhase(graph_axes, x, y)
        x = []
        y = []


    def onButtonClearClicked(event):
        global graph_axes 
        graph_axes.clear()
        graph_axes.grid()
        plt.draw()

    def submitA(text):
        global a
        try:
            a = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")            
            
    def submitC(text):
        global c
        try:
            c = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitH(text):
        global h
        try:
            h = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitX0(text):
        global x0
        try:
            x0 = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitY0(text):
        global y0
        try:
            y0 = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitN(text):
        global n
        try:
            n = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")

    def submitB(text):
        global b
        try:
            b = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            
            
    def submitD(text):
        global d
        try:
            d = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")


    fig, graph_axes = plt.subplots()
    graph_axes.grid()
    fig.subplots_adjust(left=0.06, right=0.98, top=0.65, bottom=0.065)
	
    axbox = plt.axes([0.2, 0.92, 0.12, 0.065])
    a_box = TextBox(axbox, 'Параметры:  a =', initial= "0.7")
    a = 0.7
    a_box.on_submit(submitA)

    axbox = plt.axes([0.39, 0.92, 0.12, 0.065])
    b_box = TextBox(axbox, 'b =', initial= "0.8")
    b = 0.8
    b_box.on_submit(submitB)

    axbox = plt.axes([0.58, 0.92, 0.12, 0.065])
    c_box = TextBox(axbox, 'c =', initial= "0.5")
    c = 0.5
    c_box.on_submit(submitC)

    axbox = plt.axes([0.78, 0.92, 0.12, 0.065])
    d_box = TextBox(axbox, 'd =', initial= "3")
    d = 3
    d_box.on_submit(submitD)
	
    axes_button_add = plt.axes([0.78, 0.74, 0.15, 0.075])
    button_add = Button(axes_button_add, 'Добавить')
    button_add.on_clicked(onButtonAddClicked)

    axes_button_clear = plt.axes([0.58, 0.74, 0.15, 0.075])
    button_clear = Button(axes_button_clear, 'Очистить')
    button_clear.on_clicked(onButtonClearClicked)

    axbox = plt.axes([0.2, 0.83, 0.12, 0.065])
    h_box = TextBox(axbox, 'Шаг =', initial="0.01")
    h = 0.01
    h_box.on_submit(submitH)

    axbox = plt.axes([0.39, 0.83, 0.12, 0.065])
    x0_box = TextBox(axbox, 'x0 =', initial="0.1")
    x0 = 0.1
    x0_box.on_submit(submitX0)

    axbox = plt.axes([0.39, 0.74, 0.12, 0.065])
    y0_box = TextBox(axbox, 'y0 =', initial= "0.1")
    y0 = 0.1
    y0_box.on_submit(submitY0)

    axbox = plt.axes([0.2, 0.74, 0.12, 0.065])
    n_box = TextBox(axbox, 'n =', initial="100")
    n = 100.0
    n_box.on_submit(submitN)

    plt.show()
