import numpy as np
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler
from matplotlib.widgets import Button

handler = SVG_Handler('share/BatlineArt.svg')

t = np.linspace(0,1,5000)

p = handler.get_point(t)

fig, ax = plt.subplots()
plot3d = plt.subplot(projection='3d')

plot3d.plot(p.real,-p.imag,t)
#plot3d.view_init(90,0,'x') # yt
#plot3d.view_init(90,-90,'y') # xt
#plot3d.view_init(90,-90,'z') # xy
plot3d.set(xlabel='x', ylabel='y',zlabel='t')

views = {
        0: (90, -90, 'y'),
        1: (90, 0, 'x'),
        2: (90, -90, 'z')
        }
currentview = 0

# buttons for views
nextax = fig.add_axes([0.8,0.025,0.1,0.04])
nextbutton = Button(nextax, 'Next', hovercolor='0.95')
prevax = fig.add_axes([0.7,0.025,0.1,0.04])
prevbutton = Button(prevax, 'Prev', hovercolor='0.95')

def nextview(event):
    global currentview
    currentview = (currentview + 1) % 3
    plot3d.view_init(*views[currentview])

def prevview(event):
    global currentview
    currentview = (currentview - 1) % 3
    plot3d.view_init(*views[currentview])

nextbutton.on_clicked(nextview)
prevbutton.on_clicked(prevview)

plot3d.view_init(*views[currentview])
plt.show()
