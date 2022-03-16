# pyrigt: strict
# This is main python file if you want to make library only please remove this file

from typing import List, Tuple

# ユークリッドの互除法
def Euclid(a: int, b: int, __r:List[int] = []) -> Tuple[int, int, int]:
    if a % b == 0:
        x, y = ([1, 0], [0, -1])
        for i in __r:
            x.append(x[-2] + i * x[-1])
            y.append(y[-2] + i * y[-1])
        return (x[-1] * (-1) * (1 - len(__r) % 2 * 2), y[-1] * (-1) * (1 -len(__r) % 2 * 2), b)
    __r.append(a // b)
    a, b = b, a % b
    print(__r)
    return(Euclid(a, b, __r))

def test(a:int, b:int):
    x, y, r = Euclid(a, b)
    print(x, y, r)
    print(f"{a * x + b * y =}")


def main():
    test(113, 47)

if __name__ == "__main__":
    main()
