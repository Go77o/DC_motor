#from sympy import *
import numpy as np
import matplotlib.pyplot as plt
#init_printing()
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
plt.ylabel('Torque [N.m]')
plt.xlabel('Velocidade [rad/s]')
#Dados:
ean = 221.7383 #armadura
ra = 0.153  #resistência de armadura
v =  np.arange(200, 0, -10) #voltagem inicial
print("Alteração da voltagem: ", v)
vo=0
vf = 200
k = 0.9278
ic = 0.6521
delta_f = 10
ifr = (ean-v)/ra
#print(ifr)
print("=================================================================================")
print("Alteração da corrente de frenagem: ", ifr)
en = v -(ra*ifr)
w = en/k*ic
ts = 31.608
tint = (0.0029*w) + ts
#var = -tin -ts
print("=================================================================================")
print("Velocidade angular: ", w)
print("=================================================================================")
print("Torque permanece constante: ", tint)
l, = plt.plot(v, ifr, label='Corrente de frenagem', lw=2, color='red')
t, = plt.plot(ifr, en, label='Armadura', lw=2, color='blue')
c, = plt.plot(w, tint, label='Torque x velocidade', lw=2, color='black')
plt.axis([0, 500, 0, 1500])
plt.legend()

axcolor = 'GhostWhite'
axvol = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
#axifr = axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

svolt = Slider(axvol, 'Volt', 0.1, 230, valinit=vo, valstep=delta_f)
#sifr = Slider(axvol, 'ifr', 0.1, 230, valinit= valstep=delta_f)

def update(val):
    volt = svolt.val
    l.set_ydata((ean-volt)/ra)
    fig.canvas.draw_idle()
svolt.on_changed(update)
svolt.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    svolt.reset()
button.on_clicked(reset)
    

    
plt.show()

