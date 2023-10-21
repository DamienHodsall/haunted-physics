import numpy as np
import wavio
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler

periods = 250
order = 800
t = np.linspace(0, 1, order)

images = {
        'pumpkin':'share/jackOlantern2.svg',
        'ghost':'share/halloween-ghost-svgrepo-com.svg',
        'grave':'share/grave-illustration-3-svgrepo-com.svg',
        'skeleton':'share/skeleton-svgrepo-com.svg'
        }

# cat, witch, lightning, 
for name, image in images.items():

    points = np.tile(SVG_Handler(image).get_point(t), periods)
    maxamp = max(abs(points))
    data = np.array([-points.real,points.imag]).T / maxamp
    wavio.write(f"share/sound_library/{name}.wav", data, 44800, sampwidth=2)
