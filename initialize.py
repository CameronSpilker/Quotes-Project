#!/usr/bin/env python3

from django.core import management
from django.db import connection
import datetime
import os, os.path, sys, json


# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'QuotesProject.settings'
import django
django.setup()

# imports (after setup)
from homepage import models as hmod
from django.conf import settings


# load the data from disk
with open(os.path.join(settings.BASE_DIR, 'quotes.json')) as f:
    quotes_data = json.load(f)

# delete all objects in the db
hmod.QuoteTag.objects.all().delete()
hmod.Tag.objects.all().delete()
hmod.Author.objects.all().delete()
hmod.Quote.objects.all().delete()

# create the objects
print('Creating objects:')
for quote_data_i, quote_data in enumerate(quotes_data['quotes']):
    print('\t{}/{}: {}...'.format(quote_data_i + 1, len(quotes_data['quotes']), quote_data['text'][:30]))
    author, created = hmod.Author.objects.get_or_create(first_name=quote_data['author']['first_name'], last_name=quote_data['author']['last_name'])
    quote, created = hmod.Quote.objects.get_or_create(text=quote_data['text'], author=author)
    for text in quote_data['tags']:
        tag, created = hmod.Tag.objects.get_or_create(text=text)
        quotetag, created = hmod.QuoteTag.objects.get_or_create(tag=tag, quote=quote)

# summary status
print('Finished:')
print('\t{} quotes'.format(hmod.Quote.objects.all().count()))
print('\t{} authors'.format(hmod.Author.objects.all().count()))
print('\t{} tags'.format(hmod.Tag.objects.all().count()))
