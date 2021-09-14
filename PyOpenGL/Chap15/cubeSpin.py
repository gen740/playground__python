from mySpinCanvas import MySpinCanvas
from cube import Cube
from Sierpinski import Sierpinski
from mengerSponge import MengerSponge


def main():
    canvas = MySpinCanvas()
    dispObj = Cube()
    # dispObj = Sierpinski(3)
    # dispObj = MengerSponge(3)
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
