# GARDEN
App for management of garden 

## Configuration
### seting vitual enviroment
0. create virtual environment eg. `virtualenv -p python3.10 env` or `python3 -m venv env` and activate it `. env/bin/activate`
1. run `pip install -r requirement.txt` to download necessary libraries

### starting the project
1. run `python manage.py migrate` to create database
2. run `python manage.py populategarden` to add some prepared subjects
3. You probably want also create superuser `python manage.py createsuperuser`


## Info for testing after populate
For testing i created example supervisor and employee user 
(default password for every user from populate is 'garden2023')

supervisor - login sup.sup@garden.com
employee - login emp.emp@garden.com

You are ready to enjoy
