#""""""EJERCICIO 6 """"""

import time
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print (f"{hora:02}:{minuto:02}:{segundo:02}")
            time.sleep(1)    