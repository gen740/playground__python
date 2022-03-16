import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Hiragino Maru Gothic Pro"

temp = np.array([50, 60, 70, 80, 90, 100, 110, 120])
racio = np.array([38.32, 34.14, 29.56, 22.74, 16.51, 15.35, 13.33, 10.49])
delta = 50
temp_y = np.exp(-temp/delta)

base = temp_y[0]
temp_y = 10*np.log10(temp_y/base)

print(temp_y)

fig, ax = plt.subplots(figsize=(10, 6))

line1, = ax.plot(temp, temp_y, "k:",label=r"$y=exp(\frac{-T}{\Delta})$/dB")
ax2 = ax.twinx()
line2, = ax2.plot(temp, racio, "k--", label="反発係数/%")

ax.legend(handles=[line1, line2])
ax.set_xlabel("温度/K")
ax.set_ylabel(r"$y=exp(\frac{-T}{\Delta})$/dB")
ax2.set_ylabel("反発係数/%")

plt.show()
