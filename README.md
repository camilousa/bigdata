# Simple-processing
#### Instalación:
     virtualenv -p python3 env
     source env/bin/activate
     pip install -r requirements.txt

### Ejecución del programa de envío:
       python simple-streaming/senddata.py
### Ejecución de ejecución del script en pyspark:
     spark-submit simple-streaming/process.py localhost 9897   

