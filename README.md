# Demo-Bike-Rental
==============================

Los sistemas de bicicletas compartidas son una nueva generación de alquileres de bicicletas tradicionales en los que todo el proceso, desde la membresía, el alquiler y la devolución, se ha vuelto automático. A través de estos sistemas, el usuario puede alquilar fácilmente una bicicleta desde una posición particular y regresar a otra posición. Actualmente, hay alrededor de 500 programas de bicicletas compartidas en todo el mundo, que se componen de más de 500 mil bicicletas. Hoy en día, existe un gran interés en estos sistemas debido a su importante papel en el tráfico, el medio ambiente y la salud.

Aparte de las interesantes aplicaciones del mundo real de los sistemas de bicicletas compartidas, las características de los datos que generan estos sistemas los hacen atractivos para la investigación. A diferencia de otros servicios de transporte como autobús o metro, la duración del viaje, la posición de salida y llegada se registran explícitamente en estos sistemas. Esta función convierte el sistema de bicicletas compartidas en una red de sensores virtuales que se puede utilizar para detectar la movilidad en la ciudad. Por lo tanto, se espera que la mayoría de los eventos importantes en la ciudad puedan detectarse mediante el seguimiento de estos datos.


### Pakages


```
pip install -r requirements.txt

```

## Entrenamiento

Usa la aplicación de línea de comando modelling/app.py para realizar los procesos de busqueda de parametros y entrenamiento del modelo

### Pruebas : Ejemplos

El archivo config.yml contiene los parametros e instancias que se pueden modificar para el entrenamiento y busqueda de parametros 

```
python modellin/app.py train config.yml #Comando entrenamiento
python modellin/app.py find-hyperparams config.yml #Busqueda de parametros
python modellin/app.py eval config.yml <path model> #Evaluación de modelo

```

# Fast API Demo

Demo de despliegue usando Fast API

## Fats API Demo:Pasos

Realisar referencia al modelo
```
SET/EXPORT serialized_model_path = <path model.joblib>
SET/EXPORT model_lib_dir = <path modelling>

```
Run

```
uvicorn app:app --reload

```




