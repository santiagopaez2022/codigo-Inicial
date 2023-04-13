# Ejercicio-2-Escuelas-por-distrito-Map.py
# Simulación de MapReduce


########################################################
# Objetivo
########################################################
# Obtener el número de escuelas por distrito
########################################################


########################################################
# Map
########################################################
# El proceso Map debe realizar los siguientes pasos:
#   1. Abrir el fichero de datos
#   2. Tratar los datos según los requerimientos del proceso
#   3. Escribir una salida con el formato (clave,valor)
########################################################


########################################################
# Definición de constantes
########################################################

# Definición de rutas de ficheros
# Fichero entrada = EscuelasBarcelona.txt
strInputFile = 'C:\\Users\\Monica\\Desktop\\EAE Master\\Big Data Technology & Achitecture\\EscuelasBarcelona.txt'
strMapOutputFile = 'C:\\Users\\Monica\\Desktop\\EAE Master\\Big Data Technology & Achitecture\\outputEcuelasDistrito.txt'

# Definición de separadores de los ficheros de entrada y salida
chrInputSeparator = ';'
chrMapOutputSeparator = '\t'

########################################################
# Apertura de ficheros de entrada y salida
########################################################
fileInput = open(strInputFile, 'r', encoding='utf-8')
fileOutput = open(strMapOutputFile, 'w')

########################################################
# Omisión de la primera fila
########################################################
fileInput.readline()


########################################################
# Generación del fichero de salida
########################################################
# Creamos la lista de salida vacía
lstMapOutput = []

# Iteración sobre las líneas del fichero
for line in fileInput:
    lstColumns = line.split(chrInputSeparator)
    strDistrito = lstColumns[10].strip("\n")
    # Añadimos un elemento al fichero
    lstMapOutput.append(strDistrito)
    

lstMapOutput.sort()
    

# Para cada elemento de la lista de salida previamente ordenada, escribimos (clave, valor) en el fichero de salida
for strDistrito in lstMapOutput:
    fileOutput.write (strDistrito + chrMapOutputSeparator + "1" + "\n")


########################################################
# Cierre de los ficheros
########################################################
fileInput.close()
fileOutput.close()

