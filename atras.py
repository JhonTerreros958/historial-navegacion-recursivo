def retroceder(historial, pasos):

    #Caso base
    if pasos == 0 or len(historial) == 0:
        return historial

    ultima_pagina = historial[-1]

    #Si aparece un Error 404 se detiene el proceso
    if "Error 404" in ultima_pagina:
        print("Se encontró un Error 404. Retroceso detenido.")
        return historial

    print("Retrocediendo desde:", ultima_pagina)

    #Elimina la última página visitada
    historial.pop()

   
    return retroceder(historial, pasos - 1)


#Historial
historial = [
    "google.com",
    "uniminuto.edu",
    "Error 404: Campus Virtual",
    "github.com",
    "stackoverflow.com"
]

#Número de pasos a retroceder
pasos = 4

resultado = retroceder(historial, pasos)

print("Historial final:", resultado)
