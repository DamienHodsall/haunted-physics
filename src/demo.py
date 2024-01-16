import numpy as np
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler
from matplotlib.widgets import Button

"""
This script is a 3d demonstration for parametric equations.

Just run it and click through the different views and move the view around.
I set it up to show xt then yt and finaly xy. When looking at xy, mention that it's
how parametric equations work.
"""

# read the image and make it into a list of points
handler = SVG_Handler('share/BatlineArt.svg')
t = np.linspace(0,2,1000) # change the second number for more or fewer periods
p = handler.get_point(t%1)

# initialize graphing stuff
plt.style.use('dark_background')
fig, ax = plt.subplots()
plot3d = plt.subplot(projection='3d')

# actual plotting of data
plot3d.plot(p.real,-p.imag,t, color='red')
plot3d.set(xlabel='x', ylabel='y',zlabel='t')

# these views are xt yt xy
views = {
        0: (90, -90, 'y'),
        1: (90, 0, 'x'),
        2: (90, -90, 'z')
        }
currentview = 0

# buttons for views
nextax = fig.add_axes([0.55,0.025,0.1,0.04])
nextbutton = Button(nextax, 'Next', color='black', hovercolor='0.15')

resetax = fig.add_axes([0.45,0.025,0.1,0.04])
resetbutton = Button(resetax, 'Reset', color='black', hovercolor='0.15')

prevax = fig.add_axes([0.35,0.025,0.1,0.04])
prevbutton = Button(prevax, 'Prev', color='black', hovercolor='0.15')

# functions to switch/reset views
def nextview(event):
    global currentview
    currentview = (currentview + 1) % 3
    plot3d.view_init(*views[currentview])

def resetview(event):
    global currentview
    plot3d.view_init(*views[currentview])

def prevview(event):
    global currentview
    currentview = (currentview - 1) % 3
    plot3d.view_init(*views[currentview])

# uhhhh yeah. this kinda explains itself... read the python matplotlib widgets if you don't get it
nextbutton.on_clicked(nextview)
resetbutton.on_clicked(resetview)
prevbutton.on_clicked(prevview)

plt.show()
