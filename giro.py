from pybricks.hubs import EV3Brick                 # Traigo de la carpeta pybricks el modulo de EV3
from pybricks.ev3devices import GyroSensor, Motor  # Traigo el sensor de giro y motor
from pybricks.parameters import Port, Color        # Traigo los puertos y colores       
from pybricks.robotics import DriveBase            # Traigo el DriveBase            
import time

# Defino mis ruedas con su respectivo puerto
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#Defino mi robot con sus caracteristicas
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

ev3 = EV3Brick()

def giro(ang):
    # Definir mi sensor de giro
    gyro = GyroSensor(Port.S2)
    gyro.reset_angle(0)
    # Ver si mi giro es positivo
    if ang > 0: 
        # Mientras en angulo del robot sea menor al angulo objetivo se mantenga moviendo
        while ang > gyro.angle()*-1: # Se multiplica por -1 para el sentido de giro como yo quiero
            robot.drive(0,100) # Defino Vel lineal en 0 y defino la velocidad de giro en 100
        robot.stop() # Detener movimiento
    else:
        while ang < gyro.angle()*-1: # Se multiplica por -1 para el sentido de giro como yo quiero
            robot.drive(0,-100) # Defino Vel lineal en 0 y defino la velocidad de giro en -100
        robot.stop() # Detener movimiento
    
    ev3.screen.draw_text(70, 50, str(gyro.angle()*-1), Color.BLACK, None)