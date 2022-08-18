# flask_wrf_map

The flask based WRF map was created to replace the static wrf map hosted on the firelab website. The new version of the WRF map has the ability to be dynamically changed and updated without having to touch the source code or directory files. It can be done through the edit page. The new WRF map also includes Remote Automatic Weather Station (RAWS) locations. The flask background also allows this service to be hosted as a microservice so errors, updates and changes on the WRF map or the rest of the web directory will not have adverse effects on each other. 

Running WRF map with Docker 
* With docker installed on your machine or server, running 'sh build.sh' will build the docker image
* running 'sh run.sh' will deploy the docker container 
- The ports and ip can be changed in the last line of app.py where it says 'host=' and 'port=' and in the run.sh file (The default is http://0.0.0.0:5000) 

Running WRF map without Docker 
* You must first install all the dependencies by running 'pip install -r requirements.txt'
* Then to start the web app run 'python3 run.py' (this file starts the flask app and automatic RAWS location collection)
