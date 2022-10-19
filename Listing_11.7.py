import numpy as np
import matplotlib.pyplot as plt
from math import tau

x = np.linspace(0, tau, 100)

fig, ax = plt.subplots()

ax.set_xticks([0, tau/4, tau/2, 3*tau/4, tau])
ax.set_yticks([-1, -1/2, 0, 1/2, 1])
plt.grid(True)

ax.set_xticklabels([r"$0$", r"$\tau/4$", r"$\tau/2$", r"$3\tau/4$", r"$\tau$"])
ax.set_yticklabels([r"$-1$", r"$-1/2$", r"$0$", r"$1/2$", r"$1$"])

ax.set_title("One period of cosine and sine", fontsize=16)
ax.set_xlabel(r"$\theta$", fontsize=16)
ax.set_ylabel(r"$f(\theta)$", fontsize=16)

ax.annotate(r"$\cos\theta$", xy=(1.75, -0.3), xytext=(0.5, -0.75),
            arrowprops={"facecolor": "black", "width": 1}, fontsize=16)
ax.annotate(r"$\sin\theta$", xy=(2.75, 0.5), xytext=(3.5, 0.75),
            arrowprops={"facecolor": "black", "width": 1}, fontsize=16)

fig.set_dpi(150)

ax.plot(x, np.cos(x), color="red", linestyle="dashed")
ax.plot(x, np.sin(x), color="blue", linestyle="dotted")
plt.show()
