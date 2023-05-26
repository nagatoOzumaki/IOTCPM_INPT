# IaC-of-IoT-plateform

    Ce repo contient le code pour la mise en place du data pipeline en utilisant vagrant et ansible, Et le code qui contient les algorithme pour entrainer le modele et la prediction de la consommation de l'enrgie au sein de l'INPT.
 

 !!! Afin de comprendre la structure de ce repos et localiser les fichiers prière de lire ce qui suit --->

# Le fichier Vagrantfile

    Ce fichier est utilisé pour creer un environnement UBUNTU en utilisant l'outil Vagrant.

# Le repertoire iot-cloud-server-code 

    Ce repertoire contient les fichiers playbooks ansible pour installer et configurer docker, et mettre en place un data pipeline, un broker pour streamer les métriques , telegraf pour transformer les mesures en un protocole ensuite le redireger vers influxb et la visualisation par grafana .

    Le sous-repertoire 'templates' les fichier de configuration de telegraf et grafana pour connecter les serveurs automatiquement .

    Le sous-repertoire 'variables' contient les variables d'environnement, le token admin de influxdb et les informations de login de chaque serveur.

#  Le repertoire data

    Le ficher 'dataset' contient un dataset (dataset_sensors.csv) pour une la consommation d'énergie dans la durée entre 2021-05-13 et 2022-05-13.

    Le Script 'convertCsvToLineProtocol.py' est un script qui va convertir le données du format csv au format Line Protocol pour qu'on puisse l'insérer dans influxdb, le resultat sera stocké dans le fichier text 'convertedToLineProtocol.txt' (ce fichier doit avoir une taille < 10 MO, sinon on le reparti sous forme des fichier de taille < 10MG ).

    Le Notebook python 'predict energy consumption.ipynb' contient le code pour faire le training et la prediction de la consommation d'energie.

     Le Script EmetData est utilisé pour simuler des capteurs qui envoient les messures vers le broker chaque 5s, on l'a utilisé pour faire la demo .
