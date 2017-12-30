# Archivo: audio.py
# Autor: Javier Garcia Algarra 
# Fecha: 24 de diciembre de 2017
# Descripción: Producimos sonidos

import winsound
do = 262
re = 294
mi = 330
fa = 349
sol = 393
la = 440
si = 494
do_5 = 523
duration = 800  # millisecond

winsound.Beep(do, duration)
winsound.Beep(re, duration)
winsound.Beep(mi, duration)
winsound.Beep(fa, duration)
winsound.Beep(sol, duration)
winsound.Beep(la, duration)
winsound.Beep(si, duration)
winsound.Beep(do_5, duration)
winsound.Beep(si, duration)
winsound.Beep(la, duration)
winsound.Beep(sol, duration)
winsound.Beep(fa, duration)
winsound.Beep(mi, duration)
winsound.Beep(re, duration)
winsound.Beep(do, duration)


dummy = input("Cuando pulses cualquier tecla escucharás una melodía conocida")

winsound.Beep(do, 2*duration)
winsound.Beep(sol,2* duration)
winsound.Beep(fa, int(duration/2))
winsound.Beep(mi, int(duration/2))
winsound.Beep(re, int(duration/2))
winsound.Beep(do_5, 2*duration)
winsound.Beep(sol, 2*duration)
winsound.Beep(fa, int(duration/2))
winsound.Beep(mi, int(duration/2))
winsound.Beep(re, int(duration/2))
winsound.Beep(do_5, 2*duration)
winsound.Beep(sol, 2*duration)
winsound.Beep(fa, int(duration/2))
winsound.Beep(mi, int(duration/2))
winsound.Beep(fa, int(duration/2))
winsound.Beep(re, 2*duration)

