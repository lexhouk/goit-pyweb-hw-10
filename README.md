# Quotes

## Deployment

```bash
$ git clone https://github.com/lexhouk/goit-pyweb-hw-10.git
$ cd goit-pyweb-hw-10
$ docker compose up -d
$ poetry install
$ cd fpq
$ python manage.py migrate
$ python -m utils.migration
$ python manage.py createsuperuser
```

## Usage

```bash
$ docker compose up -d
$ poetry shell
$ cd fpq
$ python manage.py runserver
```

Go to http://localhost:8000.
