import numpy as np
import matplotlib.pyplot as plt

# Cuadrante 1
x = np.linspace(0, 8, 400)
y1 = 8 - x
y2 = 18 - 3 * x

plt.figure()
plt.plot(x, y1, label='x1 + x2 <= 8')
plt.plot(x, y2, label='3x1 + x2 <= 18')
plt.fill_between(x, 0, y1, where=(x >= 0) & (x <= 8), color='gray', alpha=0.5, label='Área factible')
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Área Factible - Cuadrante 1')
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Cuadrante 2
x = np.linspace(-8, 0, 400)
y1 = 8 + x
y2 = 18 + 3 * x

plt.figure()
plt.plot(x, y1, label='x1 + x2 <= 8')
plt.plot(x, y2, label='3x1 + x2 <= 18')
plt.fill_between(x, 0, y1, where=(x <= 0) & (x >= -8), color='gray', alpha=0.5, label='Área factible')
plt.xlim(-8, 0)
plt.ylim(0, 8)
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Área Factible - Cuadrante 2')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Cuadrante 3
x = np.linspace(-8, 0, 400)
y1 = 8 + x
y2 = 18 + 3 * x

plt.figure()
plt.plot(x, y1, label='x1 + x2 <= 8')
plt.plot(x, y2, label='3x1 + x2 <= 18')
plt.fill_between(x, 0, y1, where=(x <= 0) & (x >= -8), color='gray', alpha=0.5, label='Área factible')
plt.xlim(-8, 0)
plt.ylim(0, 8)
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Área Factible - Cuadrante 3')
plt.show()

