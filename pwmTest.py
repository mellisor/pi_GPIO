import PWM
from time import sleep

p = PWM.PWM(18,blocking=True)

p.set_duty_cycle(.005)
p.set_frequency(261.6)

p.runFor(1)
p.set_frequency(500.0)
p.runFor(2)