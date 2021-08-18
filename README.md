# Tweet application.

### Local Dev Setup

### Steps to install and run tweets
* Run `$ pip install virtualenv` command to install virtual environment
* Run `$ virtualenv env -p python3.8` command to Create Virtual environment
* Run `$ source env/bin/activate` command to activate virtual environment
* Run `$ cd tweets` command for move into the project directory
* Run `$ pip install -r requirements.txt` command to Install project requirement
* Run `$ python manage.py migrate` command to apply migrations on your local.
* Run `$ python manage.py runserver 8001` command to run project on your local machine