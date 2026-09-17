#10-09-26
#Code by Anvidha

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1.5, 500)
y = np.exp(x) - 2    #given equation to plot

plt.plot(x, y, label=r'$e^x-2$')
plt.axhline(0, linewidth=1)
plt.axvline(np.log(2), linestyle='--', label=r'Root = $\ln(2)$')

#giving x-axis, y-axis names
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton-Raphson: $e^x - 2 = 0$')
plt.grid()
plt.legend()

plt.savefig('bt33.pdf', dpi=300, bbox_inches='tight')
