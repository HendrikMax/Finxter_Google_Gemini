# .env-Datei erstellen
#  bei Installation pipenv wird requirements.txt-Datei beachtet!!!
#  ggf. pipenv -rm bei Ordner-Änderung
pipenv install
pipenv install -r requirements.txt
#To activate this project's virtualenv, run pipenv shell.
#Alternatively, run a command inside the virtualenv with pipenv run
# to deactivate, run exit

# Pfad auf Virtuelle Umgebung anzeigen
echo $VIRTUAL_ENV