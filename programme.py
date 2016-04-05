import cflib.crtp, cflib.crazyflie, time
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

cflib.crtp.init_drivers()
c=cflib.crazyflie.Crazyflie()
c.open_link("radio://0/80/250K")

#sense.show_message(message)


d = (c, 255, 0) #droite
g = (255, 255, 0) #gauche
h = (0, 255, 0) #haut
b = (255, 255, 0) #bas
o = (0, 0, 0) #vide


ecran = [
    o, h, h, h, h, h, h, o,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    o, b, b, b, b, b, b, o
]

v = 30000


while 0 == 0:
    ecran = [
    o, h, h, h, h, h, h, o,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    g, o, o, o, o, o, o, d,
    o, b, b, b, b, b, b, o
    ]

    pitch, roll, yaw = sense.get_orientation().values()
    pitch = pitch/360*20000
    yaw = yaw/360*20000
    yaw = 65535
    print ("pitch", pitch, "roll", roll, "yaw", yaw)





    #roll va de 0 a 360
    if roll > 350 or roll < 10:
        roll = 0

    if roll < 180:
        roll = roll/180*65535


    if roll >= 180:
        roll = roll/180*65535




    if pitch > 350 or roll < 10:
        pitch = 0

    if pitch < 180:
        pitch = roll/180*65535


    if pitch >= 180:
        pitch = roll/180*65535








    print ("pitch", pitch, "roll mod", roll, "yaw", yaw)






    yaw = yaw/360*65535






    #sense.set_pixels(ecran)
    #d = (v, 255, 0)
    v = v + 20

    if v > 65535:
        v = 65535


    print ("puissance", v)


    c.commander.send_setpoint(0, 0, 0, 0)
    #time.sleep(0.1)
    c.commander.send_setpoint(0, 0, 0, v)
    time.sleep(0.1)
    c.commander.send_setpoint(0, 0, 0, 0)




#c.commander.send_setpoint(0, 0, 0, 20000)

