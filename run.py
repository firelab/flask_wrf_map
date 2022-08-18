import subprocess

# Run.py was created as the simple run script for the project
# it is used to run both the flask app and RAWS data collection at the same time 
subprocess.run("python3 app.py & python3 raws_collection.py", shell=True)