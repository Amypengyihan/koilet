import os
import time
import RPi.GPIO as GPIO


GPIO40.setmode(GPIO.BCM)
GPIO120.setmode(GPIO.BCM)
GPIO_OUT40 = 23
GPIO_OUT120 = 22
led = 21
motor.action = False #是否下降
motor.lowstate = False #是否处于低位
#设置引脚为输入输出
GPIO40.setwarnings(False)
GPIO120.setwarnings(False)
#设置23针脚，24针脚为输入，接到红外线的out传感器模块的out引脚
GPIO40.setup(GPIO_OUT,GPIO.IN)
GPIO120.setup(GPIO_OUT,GPIO.IN)

def warn1():
    GPIO40.output(led,GPIO.HIGH)
    time.sleep(0.05)
    GPIO40.output(led,GPIO.LOW)
    time.sleep(0.05)
    moter.action = False
def warn2():
    GPIO120.output(led,GPIO.HIGH)
    time.sleep(0.05)
    GPIO120.output(led,GPIO.LOW)
    time.sleep(0.05)
    motor.action = True

if motor.action = False and motor.lowstate = False:
    continue
else:
    motor.raise()

while GPIO40.setwarnings=True and GPIO40.setwarnings=True:
    if GPIO40.input(GPIO_OUT)==0 and GPIO120.input(GPIO_OUT)==0:#大于120cm的
        warn1()
    if GPIO40.input(GPIO_OUT)==0 and GPIO120.input(GPIO_OUT)==1:#小于120cm的
        warn2()

GPIO.cleanup()
