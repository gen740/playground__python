from myCanvas import MyCanvas
from vectorMatrix import norm


def pressed(event):
    global canvas, start
    start = canvas.point(event.x, event.y)


def dragged(event):
    global canvas, start
    # 大域変数 canvas, start
    canvas.clear()  # canvas の背景クリア
    canvas.drawPolyline((start, canvas.point(event.x, event.y)))  # 線分の描画


def main():  # main 関数
    global canvas  # 大域変数 canvas
    canvas = MyCanvas(width=400, height=400)  # canvas の作成
    canvas.bind('<Button-1>', pressed)
    canvas.bind('<B1-Motion>', dragged)
    canvas.mainloop()


if __name__ == '__main__':
    main()
