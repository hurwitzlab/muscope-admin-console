# muscope-admin-console
A Flask-Admin interface to the muSCOPE database.

## Requirements
A Python 3.6+ interpreter is required. Please, oh please, use a virtual environment, for example:

```
$ python3.6 -m venv ~/venv/mu
$ source ~/venv/mu/bin/activate
(mu) $
```

The following environment variables must be defined:

  + MUSCOPE_DB_URI=mysql+pymysql://imicrobe:{password}@127.0.0.1/muscope2
  + MUSCOPE_FLASK_CONFIG=production
  + MUSCOPE_ADMIN_CONSOLE_UN=muscope-admin
  + MUSCOPE_ADMIN_CONSOLE_PW={random strings are best}
  + MUSCOPE_ADMIN_CONSOLE_SESSION_SECRET_KEY={a UUID is a good choice}

## Install
Download or clone the repository and install with `pip`:
```
(mu) $ git clone git@github.com:hurwitzlab/muscope-admin-console.git
(mu) $ cd muscope-admin-console
(mu) $ pip install -r requirements.txt
(mu) $ python write_models.py
```

## Run
```
(mu) $ python manage.py runserver --port 5001 --host 0.0.0.0
```

I use `screen` to keep the server running.


## View
In development configuration the URL is 
```
https://localhost:8443/muscope/admin/
```

In production configuration the URL is
```
https://data.muscope.org/admin/
```

## Update after database changes
Stop the flask server with Ctrl-C. Run `write_models.py` and start the server again.

```bash
(mu) $ <Ctrl-C>
(mu) $ python write_models.py
(mu) $ python manage.py runserver --port 5001 --host 0.0.0.0
```
