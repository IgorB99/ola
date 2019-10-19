from machine import Pin
from time import sleep

def muda(v):
  global cont
  cont += 1
  led.value(cont)
  if cont == 0:
    led.value(1)
  else:
    led.value(0)
    sleep(0.5)
    led.value(1)
    sleep(0.5)

led = Pin(4, Pin.OUT)
botao = Pin(5, Pin.IN, Pin.PULL_UP)
botao.irq(trigger = Pin.IRQ_FALLING, handler = muda)

while True:
  pass
