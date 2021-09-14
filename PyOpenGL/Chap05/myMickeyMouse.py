import numpy as np
from myCanvas import MyCanvas
from vectorMatrix import norm


def pressed(event):
    global start, H, W
    start = canvas.point(event.x, event.y)


def dragged(event):
    global canvas, start, H, W
    canvas.clear()
    r = norm(start - canvas.point(event.x, event.y))
    canvas.drawCircle(start, r=r, fill="#ff0000")
    canvas.drawCircle(start + np.array([-r, r * 5 / 4]), r=r * 2 / 3, fill="#ff0000")
    canvas.drawCircle(start + np.array([r, r * 5 / 4]), r=r * 2 / 3, fill="#ff0000")


def main():
    global W, H, canvas
    canvas = MyCanvas()
    W, H = canvas.w, canvas.h
    canvas.bind('<Button-1>', pressed)
    canvas.bind('<B1-Motion>', dragged)
    canvas.mainloop()


if __name__ == '__main__':
    main()
