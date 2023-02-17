############################
A = 5. # mm
mu1 = 10.*1000 # kg/m
mu2 = 90000.*1000 # kg/m
S = 4. # N
w = 10*3.14 # 1/s
#############################
dt = 0.002 # s
tmax = 1 # s
xmin = -10 # mm
xmax = 10 # mm
#############################

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

B = A*(mu2**.5 - mu1**.5)/(mu2**.5 + mu1**.5)
C = A*2*mu1**.5/(mu2**.5 + mu1**.5)
k = w/(S/mu1)**.5

x1 = np.linspace(xmin/1000., 0, 1000)
x2 = np.linspace(0, xmax/1000., 1000)

def init():
    streng1.set_data([], [])
    streng2.set_data([], [])
    streng1.set_data([], [])
    bolge_inn.set_data([], [])
    bolge_ref.set_data([], [])
    tid_tekst.set_text(r"$t = 0$ s")
    return streng1, streng2, tid_tekst, bolge_inn, bolge_ref

def animate(i):
    t = i * dt
    yi = A*np.sin(k*x1 - w*t)
    yr = B*np.sin(k*x1 + w*t)
    yt = C*np.sin(k*x2 - w*t)
    streng1.set_data(x1*1000, yi + yr)
    bolge_inn.set_data(x1*1000, yi)
    bolge_ref.set_data(x1*1000, yr)
    streng2.set_data(x2*1000, yt)
    tid_tekst.set_text(r"$t = %.2f$ s"%(t))
    return streng1, streng2, tid_tekst, bolge_inn, bolge_ref

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(xmin, xmax)
plt.ylim(-2*A, 2*A)
plt.xlabel(r"Posisjon, $x$ [mm]")
plt.ylabel(r"Utslag, $y$ [mm]")
streng1, = plt.plot([], [], label="Inkommende og reflektert")
streng2, = plt.plot([], [], label="Transmitert bølge")
bolge_inn, = plt.plot([], [], "--", label=r"$y_i$")
bolge_ref, = plt.plot([], [], "--", label=r"$y_r$")
plt.legend()
tid_tekst = plt.text(.1, .9, r"$t = 0$ s", fontsize=20, transform=ax.transAxes)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(tmax/dt), interval=20, blit=True)
#anim.save('anim.mp4', fps=30)
plt.show()
