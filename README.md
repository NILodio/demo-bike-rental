# Demo-Bike-Rental
==============================

Los sistemas de bicicletas compartidas son una nueva generación de alquileres de bicicletas tradicionales en los que todo el proceso, desde la membresía, el alquiler y la devolución, se ha vuelto automático. A través de estos sistemas, el usuario puede alquilar fácilmente una bicicleta desde una posición particular y regresar a otra posición. Actualmente, hay alrededor de 500 programas de bicicletas compartidas en todo el mundo, que se componen de más de 500 mil bicicletas. Hoy en día, existe un gran interés en estos sistemas debido a su importante papel en el tráfico, el medio ambiente y la salud.

Aparte de las interesantes aplicaciones del mundo real de los sistemas de bicicletas compartidas, las características de los datos que generan estos sistemas los hacen atractivos para la investigación. A diferencia de otros servicios de transporte como autobús o metro, la duración del viaje, la posición de salida y llegada se registran explícitamente en estos sistemas. Esta función convierte el sistema de bicicletas compartidas en una red de sensores virtuales que se puede utilizar para detectar la movilidad en la ciudad. Por lo tanto, se espera que la mayoría de los eventos importantes en la ciudad puedan detectarse mediante el seguimiento de estos datos.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Pakages


```
pip install -r requirements.txt

```

## Entrenamiento

Usa la aplicación de línea de comando modelling/app.py para realizar los procesos de busqueda de parametros y entrenamiento del modelo

### Pruebas : Ejemplos

El archivo config.yml contiene los parametros e instancias que se pueden modificar para el entrenamiento y busqueda de parametros 

```
python modellin/app.py train config.yml #

```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

