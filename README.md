# 1. Simple-processing
Script de ejemplo de pyspark streaming. El script muestra en consola el conteo de palabras recibidas a través de un socket.

#### Instalación:
     virtualenv -p python3 env
     source env/bin/activate
     pip install -r requirements.txt

### Ejecución del programa de envío de palabras a través del socket:
       python simple-streaming/senddata.py
       
### Ejecución del script de conteo en pyspark:
     spark-submit simple-streaming/process.py localhost 9897

# 2. PySpark streaming to backend
Programa de ejemplo de envío de datos desde pyspark a un backend en Flask
#### Instalación:
     virtualenv -p python3 env
     source env/bin/activate
     pip install -r requirements.txt

### Arranque del servidor de Flask:
       python streaming-to-backend/python server.py

### Ejecución del programa de envío de palabras a través del socket:
       python streaming-to-backend/senddata.py
       ...
       Introduzca dato: sensor1,2
       Introduzca dato: sensor2,3
       
alternativa en linux:

        nc -tkl 9898
        sensor1,2
        sensor2,3
        
### Ejecución del script de conteo en pyspark:
     spark-submit streaming-to-backend/process.py localhost 9898
