import numpy as np
import wavio
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler

"""
This script makes an audio output from an svg. The left and right channels of the output
are the x and y of the image. Pass these channels into an oscilloscope and put it into xy
mode to show the image on the oscilloscope. plt is used for testing and a rough preview of
the oscilloscope. demo.py can be paired with this script to explain the concept of
paremetric equations with a 3d plot of the bat image.
"""

# this can be changed to alter the frequency of the output sound
# it seems like ω α 1/plotOrder
plotOrder = 800
t = np.linspace(0, 1, plotOrder)

# this just makes it easier to change images during testing
images = {
        'bat':'share/BatlineArt.svg',
        'pumpkin1':'share/JackOlanternLines.svg',
        'pumpkin2':'share/pumpkinmaybenotahunted.svg',
        'pumpkin3':'share/jackOlantern2.svg',
        'ghost':'share/halloween-ghost-svgrepo-com.svg',
        'lightning':'share/cloud-bolt-svgrepo-com.svg',
        'skeleton':'share/skeleton-svgrepo-com.svg',
        'grave1':'share/grave-illustration-3-svgrepo-com.svg',
        'sad':'share/sad-face-svgrepo-com.svg'
        }

# SVG_Handler.get_points takes all the paths of the svg and makes them into a function
# with domain [0,1) (so use np.linspace(0,1))
# takes a single float or a list/array
# returns an array
handler = SVG_Handler(images['bat'])
p = handler.get_point(t)

# signal must be <= 1 so divide by the largest magnitude to normalize (maybe not the most efficient but was quick to implement)
maxamp = max(abs(p))
data = np.array([p.real,p.imag]).T / maxamp

# output to file, from data, with some stuff (don't mess with it and you'll be fine)
wavio.write("share/output.wav", data, 44800, sampwidth=2)

plt.plot(p.real,-p.imag) # (-) because it gets flipped for some reason
plt.show()
