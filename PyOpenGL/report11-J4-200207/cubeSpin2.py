from mySpinCanvas2 import MySpinCanvas
from cube import Cube


def main():
    canvas = MySpinCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
