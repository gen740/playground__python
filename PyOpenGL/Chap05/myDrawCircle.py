from myCanvas import MyCanvas
from vectorMatrix import norm


def pressed(event):
    global start, H, W
    start = canvas.point(event.x, event.y)


def dragged(event):
    global canvas, start, H, W
    canvas.clear()
    r = norm(start - canvas.point(event.x, event.y))
    canvas.drawCircle(start, r=r)
    canvas.drawCircle(start, r=r / 2)
    canvas.drawCircle(start, r=r * 3 / 2)


def main():
    global W, H, canvas
    canvas = MyCanvas()
    W, H = canvas.w, canvas.h
    canvas.bind('<Button-1>', pressed)
    canvas.bind('<B1-Motion>', dragged)
    canvas.mainloop()


if __name__ == '__main__':
    main()
