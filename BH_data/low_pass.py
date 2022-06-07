import numpy as np
import random
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = [i * 0.1 for i in range(1000)]

y = []

for i in x:
    y.append(i * i / 10 + random.gauss(0, 1))
x_mu = 0.1
mu = 0.1

ly = []
ldy = []
lddy = []

i_prev = 0
for i in y:
    if len(ly) == 0:
        ly.append(i)
        ldy.append(0)
    else:
        ly.append(x_mu * i + (1 - x_mu) * ly[-1])
        ldy.append(mu * (ly[-1] - ly[-2]) + (1 - mu) * ldy[-1])


ax.plot(x, y, "r-")
ax.plot(x, ly, "b-")
# ax.plot(x, ldy, "b-")

plt.show()
