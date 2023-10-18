import numpy as np
import matplotlib.pyplot as plt
from svg_handler import SVG_Handler

plotOrder = 1000
t = np.linspace(0, 1, plotOrder)
order = 10

handler = SVG_Handler('share/BatlineArt.svg')

# plagiarism 101
def get_fourier_coeff(func, T=[0, 1], N=4):
    indizes = np.arange(-N, N+1)
    coeff = np.empty(indizes.shape, dtype=complex)

    period = T[1] - T[0]
    for k, ind in enumerate(indizes):
        solver = IS(lambda t: func(t)*np.exp(2j*np.pi*ind/period * t), T)
        coeff[k] = solver.get_approximation(200, n_gauss_param=6)

    return indizes, coeff

def fourier(t,C):

    return np.sum([np.exp(c*(n+1)*np.pi*2j*t) for n,c in enumerate(C)],0)

def constants(A,P):

    return [a*np.exp(p*np.pi*1j/180) for a,p in zip(A,P)]

A = [((i+1)%2)/((i+1)*((-1)**(((i+1)//2)%2))) for i in range(order)]
P = order*[0]

#c = fourier(t,constants([1,2,6,3,8],[0,30,60,90,120]))
#plt.plot(c.real,c.imag)
#plt.plot(t,c.real)
#plt.show()

values = [108+0j, 110+25j, 112+50j, 113.5+75j, 115+100j, 116+125j, 117.5+150j, 125+150j, 150+150j, 175+150j, 200+150j, 225+150j, 225+175j, 225+200j, 225+220j, 200+220j, 175+220j, 150+220j, 125+220j, 100+220j, 75+220j, 50+220j, 25+220j, 0+219.5j, -25+219j, -50+217j, -75+215j, -100+212j, -125+209j, -150+203j, -158+200j, -175+190j, -190+175j, -203+150j, -211+125j, -220+100j, -225+85j, -209+85j, -200+100j, -182+125j, -175+132j, -150+145j, -125+150j, -100+150j, -87+150j, -87.5+125j, -89+100j, -92+75j, -95+50j, -100+25j, -105+0j, -113+-25j, -122+-50j, -136+-75j, -152+-100j, -170+-125j, -186+-150j, -189+-175j, -178+-200j, -175+-205j, -150+-220j, -125+-220j, -100+-202j, -85+-175j, -77+-150j, -73+-125j, -70+-100j, -67.5+-75j, -65+-50j, -62+-25j, -60+0j, -57+25j, -54.5+50j, -51.5+75j, -49+100j, -47+125j, -45+150j, -25+150j, 0+150j, 25+150j, 50+150j, 58+150j, 55+125j, 53+100j, 51+75j, 49+50j, 47+25j, 44.5+0j, 42+-25j, 40+-50j, 38.5+-75j, 37.5+-100j, 37+-125j, 37.5+-150j, 43+-175j, 49+-185j, 66+-200j, 75+-205j, 100+-215j, 125+-218j, 150+-214j, 175+-203j, 179+-200j, 201.5+-175j, 213+-150j, 221+-125j, 226.5+-100j, 227.5+-88j, 210+-88j, 209+-100j, 200+-123j, 197+-125j, 175+-141j, 150+-144j, 125+-134j, 117+-125j, 109+-100j, 106+-75j, 106+-50j, 106.5+-25j]

#c = fourier(t,np.fft.fft(values))
reals = [val.real for val in values]
imags = [val.imag for val in values]
c = np.fft.fft(values,plotOrder)
p = np.fft.ifft(c,plotOrder)

#_, coeff = get_fourier_coeff(lambda t: handler.get_point(t), T=[0,1],N=order)
#c = fourier(t,constants(coeff.real, coeff.imag))

c = np.fft.fft(handler.get_point(t))
# do some stuff with c
p = np.fft.ifft(c,plotOrder)

#plt.plot(t,c.real)
#plt.plot(t,c.imag)
plt.plot(-p.real,-p.imag)
#plt.scatter(reals, imags)
plt.show()
