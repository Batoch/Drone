import cflib.crtp, cflib.crazyflie, time
from sense_hat import SenseHat
import threading, stick


sense = SenseHat()

sense.clear()

cflib.crtp.init_drivers()
c=cflib.crazyflie.Crazyflie()
c.open_link("radio://0/80/250K")

stick = stick.SenseStick()

pitch = 0
roll = 0
yaw = 0
puissance = 000

def joystick():
    global puissance
    while True:
        stick.wait() # block until an event is available
        #print ("char=",stick.read().key)
        joystick = stick.read().key


        if joystick == 103: #haut
            puissance = puissance + 1000



        if joystick == 108: #bas
            puissance = puissance - 1000

        
        if puissance > 60000:
            puissance = 60000




        



def getpos():
    global pitch
    global roll
    global yaw

    pitch, roll, yaw = sense.get_orientation().values()

    p = (pitch + 360) % 360
    print ("pitch=",p)


#    if pitch < 165:
        #pitch = (pitch - 165) + 360
#        p = (p + 360) % 360
#        print ("pitch=",p)
#    if pitch > 165:
#        pitch = pitch - 165
    print ("pitch", pitch, "roll", roll, "yaw", yaw)


    #yaw = yaw/360*65535

    #roll va de 0 a 360
#    if roll > 350 or roll < 10:
#        roll = 0

#    if roll < 180:
#        roll = (roll-10)/170*65535


#    if roll >= 180:
#        roll = -((360-roll)/170*65535)




#    if pitch > 350 or pitch < 10:
#        pitch = 0

#    if pitch < 180:
#        pitch = (pitch-10)/170*65535


#    if pitch >= 180:
#        pitch = -((360-pitch)/170*65535)




    if 0 < roll < 180:
        roll = roll / 4


    if 180 <= roll < 360:
        roll = (roll - 360) / 4








    if 0 < pitch < 180:
        pitch = pitch / 4


    if 180 <= pitch < 360:
        pitch = (pitch - 360) / 4












    yaw = yaw/360*65535



#pitch = pitch/4 #roll va de 0 a 12000 
#roll = roll/4





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



threading.Thread(target = joystick).start()




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



    threading.Thread(target = getpos).start()

    #print ("pitch", pitch, "roll mod", roll, "yaw", yaw)





    #sense.set_pixels(ecran)
    #d = (v, 255, 0)


    if puissance > 65534:
        puissance = 65534


    print ("puissance", puissance)


    print ("donnee envoye: pitch", pitch, "roll", roll, "puissance", puissance)


    c.commander.send_setpoint(0, 0, 0, 0)
    #time.sleep(0.1)
    c.commander.send_setpoint(pitch, roll, 0, puissance)
    time.sleep(0.1)
    c.commander.send_setpoint(0, 0, 0, 0)



#c.commander.send_setpoint(0, 0, 0, 20000)
