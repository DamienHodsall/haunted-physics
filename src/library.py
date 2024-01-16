import numpy as np
import wavio
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler

periods = 250
order = 750
t = np.linspace(0, 1, order)

images = {
        'pumpkin':'share/jackOlantern2.svg',
        'ghost':'share/halloween-ghost-svgrepo-com.svg',
        'grave':'share/grave-illustration-3-svgrepo-com.svg',
        'skeleton':'share/skeleton-svgrepo-com.svg',
        'cat':'share/cat-solid-svgrepo-com.svg',
        'bat':'share/halloween-winged-monster-with-horns-and-fangs-svgrepo-com.svg',
        'atom':'share/physics-science-svgrepo-com.svg',
        'planet':'share/planet-svgrepo-com.svg',
        'spider':'share/spider-and-web-outlined-halloween-animal-svgrepo-com.svg',
        'fangs':'share/VampFangs.svg',
        'cauldron':'share/witch-cauldron-of-halloween-svgrepo-com.svg',
        'witch':'share/witch-typical-halloween-character-svgrepo-com.svg',
        'pacman':'share/pacman-svgrepo-com.svg',
        'misfits':'share/misfits-logo-high-resolution-5.svg'
        }

# cat, witch, lightning,
for name, image in images.items():

    print(name)
    points = np.tile(SVG_Handler(image).get_point(t), periods)
    maxamp = max(abs(points))
    data = np.array([-points.real,points.imag]).T / maxamp
    wavio.write(f"share/sound_library/{name}.wav", data, 44800, sampwidth=2)
