import pyglet
from math import cos, sin, atan, pi
from pyglet.window import mouse
window = pyglet.window.Window()
window.height = 800
window.width = 800
uhel = 0

RYCHLOST_OTACENI = 1/10 #radianu za sekundu


def tik(t):
    global uhel
    uhel = uhel + t* RYCHLOST_OTACENI
    had.x = 330 + 300 * cos(uhel)
    had.y = 330 + 300 * sin(uhel)

def klik(x, y, b, mod):
    if b == mouse.LEFT:
        global uhel
        if x>=330:
            uhel = atan((y-330)/(x - 330))
        else:
            uhel = pi + atan((y - 330) / (x - 330))

def zpracuj_text(text):
    if text=='r':
        global uhel
        uhel = 0

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 1/2)

def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 1)

def vykresli():
    window.clear()
    had.draw()

obrazek = pyglet.image.load('had.png')
obrazek2 = pyglet.image.load('had2.png')
had = pyglet.sprite.Sprite(obrazek)

pyglet.clock.schedule_interval(tik, 1/30)
pyglet.clock.schedule_once(zmen, 1)

window.push_handlers(
    on_text = zpracuj_text,
    on_draw = vykresli,
    on_mouse_press = klik,
)

pyglet.app.run()