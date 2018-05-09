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

  + MUSCOPE_DB_URI=mysql+pymysql://imicrobe:password@127.0.0.1/muscope2
  + MUSCOPE_FLASK_CONFIG=production
  + MUSCOPE_ADMIN_CONSOLE_UN=muscope-admin
  + MUSCOPE_ADMIN_CONSOLE_PW=
  + MUSCOPE_ADMIN_CONSOLE_SESSION_SECRET_KEY=

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
