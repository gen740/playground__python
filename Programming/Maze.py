from defaultlist import defaultlist
from MazeData import Node66

"""

方針

┌────┬────┬────┬────┬────┬────┬────┐
│  0 │  1 │  2 │  3 │  4 │  5 │  6 │
├────┼────┼────┼────┼────┼────┼────┤
│  7 │  8 │  9 │ 10 │ 11 │ 12 │ 13 │
├────┼────┼────┼────┼────┼────┼────┤
│ 14 │ 15 │ 16 │ 17 │ 18 │ 19 │ 20 │
├────┼────┼────┼────┼────┼────┼────┤
│ 21 │ 22 │ 23 │ 24 │ 25 │ 26 │ 27 │
├────┼────┼────┼────┼────┼────┼────┤
│ 28 │ 29 │ 30 │ 31 │ 32 │ 33 │ 34 │
├────┼────┼────┼────┼────┼────┼────┤
│ 35 │ 36 │ 37 │ 38 │ 39 │ 40 │ 41 │
├────┼────┼────┼────┼────┼────┼────┤
│ 42 │ 43 │ 44 │ 45 │ 46 │ 47 │ 48 │
└────┴────┴────┴────┴────┴────┴────┘
のように頂点の番号をつけ、各頂点がどの頂点に接続されているかを書き下す。

　66のグラフは有向グラフとして、データを作る(MazeData.py)
それを用いて幅優先探索によって、答えを求める。

そして答えを求めると

[24, 6, 41, 17, 35, 0, 7, 12, 33, 29, 8, 14, 30, 37, 13, 5, 11, 27, 26, 44, 45]

となる。

"""


class Queue:
    def __init__(self):
        self.queue = []

    def enq(self, x):
        self.queue.append(x)

    def deq(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0


class Graph:
    def __init__(self, g):  # Nodeをstringで渡さなくて済むようにする。
        self.list = defaultlist(lambda: [])
        for i in g:
            self.connect(i[0], i[1])

    def connect(self, x, y):
        self.list[x].append(y)

    def __str__(self):
        s = ""
        for i in range(len(self.list)):
            for j in self.list[i]:
                s += str(i) + " " + str(j) + "\n"
        return s

    def trav(self, frm, to):
        self.prev = defaultlist()
        self.travx(frm, frm, to)

    def trav2(self, frm, to):
        self.prev = defaultlist()
        q = Queue()
        d = frm
        while d is not None and d != to:
            for u in self.list[d]:
                if self.prev[u] is None:
                    self.prev[u] = d
                    q.enq(u)
            d = q.deq()
        if d == to:
            self.trace(to, frm)

    def travx(self, frm, d, to):
        if d == to:
            self.trace(to, frm)
            return
        for u in self.list[d]:
            if u != frm:
                if self.prev[u] is None:
                    self.prev[u] = d
                    self.travx(frm, u, to)
                    self.prev[u] = None

    def trace(self, frm, to):
        path = []
        while frm != to:
            path.append(frm)
            frm = self.prev[frm]
        path.append(to)
        print(path)


def main():
    g = Graph(Node66)
    print(g)
    g.trav2(45, 24)


if __name__ == "__main__":
    main()
