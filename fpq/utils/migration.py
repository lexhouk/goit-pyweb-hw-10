from os import environ

from django import setup
from dotenv import load_dotenv


load_dotenv()
setup()


from mongoengine import connect, Document
from mongoengine.connection import ConnectionFailure
from mongoengine.fields import DateField, ListField, ReferenceField, \
    StringField
from pymongo.errors import ConfigurationError

from fpq_author.models import Author as TargetAuthor
from fpq_quote.models import Quote as TargetQuote


class Author(Document):
    fullname = StringField(max_length=50, required=True)
    born_date = DateField(required=True)
    born_location = StringField(max_length=100, required=True)
    description = StringField(required=True)
    meta = {'collection': 'authors'}


class Quote(Document):
    tags = ListField(StringField(max_length=30), required=True)
    author = ReferenceField('Author', required=True)
    quote = StringField(required=True)
    meta = {'collection': 'quotes'}

try:
    connect(
        db=environ['MONGODB_DATABASE'],
        host=environ['MONGODB_URL'],
        tls=True,
        tlsAllowInvalidCertificates=True
    )
except (ConfigurationError, ConnectionFailure):
    raise Exception('Invalid credentials.')

authors = {}

for author in Author.objects():
    authors[author.id] = TargetAuthor.objects.get_or_create(
        name=author.fullname,
        born_date=author.born_date,
        born_location=author.born_location,
        bio=author.description,
    )[0]

for quote in Quote.objects():
    TargetQuote.objects.get_or_create(
        author=authors[quote.author.id],
        phrase=quote.quote,
    )
