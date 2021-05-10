# Simple-processing
Script de ejemplo de pyspark streaming. El script muestra en consola el conteo de palabras recibidas a través de un socket.

#### Instalación:
     virtualenv -p python3 env
     source env/bin/activate
     pip install -r requirements.txt

### Ejecución del programa de envío de palabras a través del socket:
       python simple-streaming/senddata.py
### Ejecución del script conteo en pyspark:
     spark-submit simple-streaming/process.py localhost 9897   
