Bookstore API
=============

# Local development

Make sure you have python (3) installed, then setup up a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment:

```bash
. env/bin/activate
```

Install the dependencies with `pip`:

```bash
pip install -r requirements.txt
```

## Run the app

You can run the app either via the `wsgy.py` as Flask app, or set the create_app config yourself.

With wsgy.py:

```bash
export APP_ENV=dev
export FLASK_APP=wsgy.py
flask run
```

or, directly:

```bash
export FLASK_APP='app:create_app("app.config.Dev")'
flask run
```

