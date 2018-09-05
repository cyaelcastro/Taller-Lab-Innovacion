import time
import pyupm_buzzer as upmBuzzer

#Inicializa buzzer en 6
buzzer = upmBuzzer.Buzzer(6)
buzzer.stopSound()
buzzer.setVolume(0.05)

buzzer.playSound(upmBuzzer.RE,900000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.RE,130000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.SOL,130000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.RE,130000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.SI,500000)
time.sleep(0.1)



