# Quotes

## Deployment

```bash
$ git clone https://github.com/lexhouk/goit-pyweb-hw-10.git
$ cd goit-pyweb-hw-10
$ echo 'your database user password' > .secret
$ docker run --name lexhouk-hw-10 -p 5432:5432 -e "POSTGRES_PASSWORD=$(cat .secret)" -d postgres
$ poetry install
$ cd fpq
$ python manage.py migrate
```

## Usage

```bash
$ docker run --name lexhouk-hw-10 -p 5432:5432 -e "POSTGRES_PASSWORD=$(cat .secret)" -d postgres
$ poetry shell
$ cd fpq
$ python manage.py runserver
```

Go to http://localhost:8000.
