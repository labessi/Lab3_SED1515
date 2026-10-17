
from machine import Pin
import time

led = Pin(16, Pin.OUT)                 # LED1
bouton = Pin(10, Pin.IN, Pin.PULL_DOWN)  # SW1 (appuyer = 1)

DELAI_REBOND_MS = 30   # duree pendant laquelle le button reste stable

led.off()              # LED off au demarrage
etat_stable = bouton.value()   # dernier etat
dernier_brut = etat_stable     # derniere lecture
dernier_changement = time.ticks_ms()

while True:
    brut = bouton.value()

    # signal = demarrage chrono
    if brut != dernier_brut:
        dernier_brut = brut
        dernier_changement = time.ticks_ms()

    # Le signal est identique pendant longtemps = changement
    if (time.ticks_diff(time.ticks_ms(), dernier_changement) > DELAI_REBOND_MS
            and brut != etat_stable):
        etat_stable = brut
        if etat_stable == 1:   # front montant = nouvelle pression 
            led.toggle()       

    time.sleep_ms(1)
