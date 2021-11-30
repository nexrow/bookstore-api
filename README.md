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

First copy `.env.sample` to a new `.env` file.

You can run the app either via the `wsgi.py` as Flask app, or set the create_app config yourself in your .env file

With wsgi.py:

Set the `FLASK_APP` to `wsgi.py` in your `.env` file if its not set and do:

```bash
$ flask run
```

or, set the `FLASK_APP` environment variable to `'app:create_app("app.config.Dev")'` to set create_app config directly, and then do:

```bash
$ flask run
```
