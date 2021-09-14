from myRotateCanvas import MyRotateCanvas
from Sierpinski import Sierpinski


def main():
    canvas = MyRotateCanvas()
    dispObj = Sierpinski(3)
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
