Bookstore API
=============

# Local development

Make sure you have python (3) installed, then setup up a virtual environment:

```bash
$ python -m venv env
```

Activate the virtual environment:

```bash
$ . env/bin/activate
```

Install the dependencies with `pip`:

```bash
$ pip install -r requirements.txt
```

## Run the app

You can run the app either via the `wsgi.py` as Flask app, or set the create_app config yourself.

With wsgi.py:

```bash
$ export APP_ENV=Dev
$ export FLASK_APP=wsgi.py
$ export FLASK_ENV=Development
$ flask run
```

or, directly:

```bash
$ export FLASK_APP='app:create_app("app.config.Dev")'
$ flask run
```

