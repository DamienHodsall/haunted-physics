import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler

plotOrder = 500
t = np.linspace(0, 1, plotOrder)
images = {
        'bat':'share/BatlineArt.svg',
        'ellipse':'share/ellipse.svg',
        'pumpkin':'share/JackOlanternLines.svg',
        'ghost':'share/ghost-ish.svg'
        }

handler = SVG_Handler(images['ghost'])

c = fft(handler.get_point(t))
# do some stuff with c
p = ifft(c,plotOrder)

plt.plot(p.real,-p.imag) # (-) because it gets flipped for some reason
plt.show()
