import os
from time import sleep

tempo = int(input('Quantos minutos até a suspensão? '))

sleep(tempo * 60)
os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
