import time
from upm import pyupm_buzzer as upmBuzzer

#Inicializa buzzer en 6
buzzer = upmBuzzer.Buzzer(6)
buzzer.stopSound()
buzzer.setVolume(0.05)

buzzer.playSound(upmBuzzer.BUZZER_RE,900000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.BUZZER_RE,130000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.BUZZER_SOL,130000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.BUZZER_RE,130000)
time.sleep(0.1)
buzzer.playSound(upmBuzzer.BUZZER_SI,500000)
time.sleep(0.1)



