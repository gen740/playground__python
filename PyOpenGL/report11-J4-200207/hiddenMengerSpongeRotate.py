from hiddenMengerSponge import MengerSponge
from myRotateCanvas import MyRotateCanvas


def main():
    canvas = MyRotateCanvas()
    dispObj = MengerSponge(3)
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
