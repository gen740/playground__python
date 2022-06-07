import numpy as np
import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()

a = 150


def calc_r(r, theta, phi):
    beta = - theta + phi
    if a ** 2 + (np.cos(beta) ** 2 - 1) * r**2 <= 0:
        return None
    A = np.sqrt(a ** 2 + (np.cos(beta) ** 2 - 1) * r**2)
    return r * np.cos(beta) - A + random.gauss(0, 8)


theta = np.linspace(-np.pi / 2, np.pi/2, 721)
d = []

BH_r = 2000
BH_theta = 0

# for i in theta:
#     if calc_r(BH_r, BH_theta, i) != None:
#         print(calc_r(BH_r, BH_theta, i))
#         d.append(calc_r(BH_r, BH_theta, i))
# else:
#     d.append(5000)

point = []
for x in theta:
    if calc_r(BH_r, BH_theta, x) != None:
        point.append([calc_r(BH_r, BH_theta, x) * np.cos(x),
                      calc_r(BH_r, BH_theta, x) * np.sin(x)])
    else:
        point.append([5000 * np.cos(x), 5000 * np.sin(x)])

for i in point:
    ax.plot(i[0], i[1], "k.")

result = np.array(point)
print(result)
np.savetxt("result.txt", result, fmt="%.18f")

plt.show()


# for i in x:
#
