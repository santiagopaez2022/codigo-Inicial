# Ejercicio 2
# Simulación de MapReduce


########################################################
# Objetivo
########################################################
# Ejecutar un Reduce con agregación SUMA
########################################################


########################################################
# Reduce
########################################################
# El proceso Reduce debe realizar los siguientes pasos:
#   1. Abrir el fichero de datos
#   2. Agregar los valores de cada clave
#   3. Escribir una salida con el formato (clave,resultado)
########################################################


########################################################
# Definición de constantes
########################################################

strInputFile = 'C:\\Users\\Monica\\Desktop\\EAE Master\\Big Data Technology & Achitecture\\outputEcuelasDistrito.txt'
strReduceOutputFile = 'C:\\Users\\Monica\\Desktop\\EAE Master\\Big Data Technology & Achitecture\\outputResultado.txt'
chrInputSeparator = '\t'
chrMapSeparator = ','

########################################################
# Apertura de ficheros de entrada y salida
########################################################
# La función open() nos permite abrir un fichero
# El modo de apertura del fichero de datos de entrada debe ser "r" (lectura)
fileInput = open(strInputFile, 'r')
# El modo de apertura del fichero de datos de salida debe ser "w" (escritura)
fileOutput = open(strReduceOutputFile, 'w')


########################################################
# Generación del fichero de salida
########################################################
# Marcamos la primera fila a tratar como la primera (con lo cual, no imprimiremos una línea de resultado en la primera línea)
first_row = True
# Inicializamos el total acumulado a 0
result = 0
# Inicializamos la clave anterior a comparar con la nueva clave a una cadena vacía
clave_anterior=''

# Tratamos cada línea del fichero de entrada
for line in fileInput:
    # Separamos las columnas
    lstColumns = line.split(chrInputSeparator)
    # La primera columna es la clave
    clave_nueva = lstColumns[0]
    # La segundaa columna es el valor
    valor = lstColumns[1]
    # Comprobamos si hay un cambio de clave
    if clave_nueva != clave_anterior:
        # Al haber un cambio de clave, debemos escribir el valor acumulado en el fichero de salida (solamente cuando no estamos tratando la primera fila)
        if first_row == False:
            # En este caso, no estamos tratando la primera fila, con lo que escribimos el valor acumulado en la salida...
            fileOutput.write(clave_anterior + ',' + str(result) + '\n')
            # ... e inicializamos el acumulado a 0 para poder empezar a acumular la columna valor (esto se hace después del IF, para todas las filas)
            result = 0
        else:
            # Si entramos por aquí, es porque estamos tratando la primera fila
            # Cambiamos el valor de la variable para que, en la siguiente iteración, sepamos que ya no estamos tratando la primera fila
            first_row = False

    # Asignamos el valor de la clave nueva a la clave anterior
    clave_anterior = clave_nueva
    # Acumulamos el valor a la variable "result", que contiene el valor acumulado
    result = result + int(valor)

# Esta última escritura en el fichero escribe la última clave tratada y el valor acumulado hasta el momento
fileOutput.write(clave_anterior + ',' + str(result) + '\n') 



########################################################
# Cierre de los ficheros
########################################################
fileInput.close()
fileOutput.close()

