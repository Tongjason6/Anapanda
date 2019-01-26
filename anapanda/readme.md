Using pipenv.
Project started in Medellin on Tues May 15, 2018 by Jay Larson

#Ubuntu
```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3.6 python3.6-venv python3.6-dev

$ python3.6 -m venv ~/.venvs/anapanda
$ source ~/.venvs/anapanda/bin/activate

$ pip install -r requirements_dev.pip

$ cd commitments/settings
$ cp local_settings.py.example local_settings.py
$ cd ../..

$ python manage.py runserver

```

#Mac
```bash
$ brew install python3 #may work, if not, try upgrade below
$ brew upgrade python
$ python3.6 -m venv ~/.venvs/anapanda

$ source ~/.venvs/anapanda/bin/activate

$ pip install -r requirements_dev.pip

$ cd commitments/settings
$ cp local_settings.py.example local_settings.py
$ cd ../..

$ python manage.py runserver 

```