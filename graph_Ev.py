import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

plt.rcParams["font.family"] = "Hiragino Maru Gothic Pro"
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(0, 42, 2)
print(x)
data_40 = np.array([1.0, 1.0, 0.9, 0.8, 0.7,
                    0.5, 0.3, 0.1, -0.1, - 0.4,
                    -0.7, -1.0, -1.3, -1.7, -2.0,
                    -2.3, -2.5, -2.8, -2.9, -3.0, -3.1])
data_35 = np.array([1.3, 1.3, 1.3, 1.1, 1.0,
                    0.8, 0.6, 0.3, 0.0, -0.4,
                    -0.8, -1.2, -1.6, -2.0, -2.3,
                    - 2.6, -2.8, -2.9, -3.0, -3.1, -3.2])
data_30 = np.array([1.7, 1.7, 1.6, 1.4, 1.2,
                    0.8, 0.5, 0.1, -0.3, -0.8,
                    -1.4, -1.8, -2.2, -2.5, -2.7,
                    -2.9, -3.2, -3.4, -3.6, -3.7, -3.8])


def ideal_(x, a, b, c):
    return a * np.log(b/(c + x ** 2))


slice_1 = 17
slice_2 = 15
slice_3 = 13
# slice_1 = 21
# slice_2 = 21
# slice_3 = 21

param = opt.curve_fit(
    ideal_, x[0:slice_1].tolist(),  data_40[0:slice_1].tolist())
param2 = opt.curve_fit(
    ideal_, x[0:slice_2].tolist(),  data_35[0:slice_2].tolist())
param3 = opt.curve_fit(
    ideal_, x[0:slice_3].tolist(),  data_30[0:slice_3].tolist())
print(param)
print(np.sqrt(np.diag(param[1])))
print(param2)
print(np.sqrt(np.diag(param2[1])))
print(param3)
print(np.sqrt(np.diag(param3[1])))


# ax.legend(handles=[line1, line2, line3])


# line1, = ax.plot(x[0:slice_1], data_40[0:slice_1], "k--", label="h=40cm")
# ideal1, = ax.plot(x[0:slice_1], ideal_(x[0:slice_1], param[0][0],
#                                       param[0][1], param[0][2]),
#                  "k-", label="最小二乗フィッティング")
# ax.legend(handles=[line1, ideal1])
# line2, = ax.plot(x[0:slice_2], data_35[0:slice_2], "k--", label="h=35cm")
# ideal2, = ax.plot(x[0:slice_2], ideal_(x[0:slice_2], param2[0][0],
#                                       param2[0][1], param2[0][2]),"k-", label="最小二乗フィッティング")
# ax.legend(handles=[line2, ideal2])
line3, = ax.plot(x[0:slice_3], data_30[0:slice_3], "k--", label="h=30cm")
ideal3, = ax.plot(x[0:slice_3], ideal_(x[0:slice_3], param3[0][0],
                                      param3[0][1], param3[0][2]),"k-", label="最小二乗フィッティング")
ax.legend(handles=[line3, ideal3])

ax.set_xlabel("水平距離/cm")
ax.set_ylabel("光の強度/EV")

plt.show()
