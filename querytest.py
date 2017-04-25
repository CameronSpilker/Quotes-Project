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
from django.conf import settings
from homepage import models as hmod
from django.contrib.postgres.search import SearchVector
from django.db.models import Q

# runs a query and prints the results
def run(num, qry):
    results = list(qry.all())
    print("Learning Query {}: {} results".format(num, len(results)))
    for quote in results:
        print("{}".format(quote))
    print()


# Example query - your queries will be more complex than this, but hopefully
# this gives you a format to follow.
# I used almost the exact same code in Queries 1-6, with only the search term
# changing each time.  If you can work towards this, your logic in the actual program
# will be a lot simpler.
# Expected results: 4 Quotes
qry = hmod.Quote.objects.filter(text__contains="best")
run(0, qry)


# LEARNING QUERY 1
# Create a single query that includes annotations containing one ore more SearchVectors to query
# Quote objects with "programmer" somewhere in the quote text, author first/last, or tag.
# Be sure each quote is only listed once in the results.  Do not use __contains (use SearchVector).
# Expected results: 13 Quotes

qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(search='programmer').distinct('id')
run(1, qry)


# LEARNING QUERY 2
# Create a single query that includes annotations containing one ore more SearchVectors to query
# Quote objects with the word "Torvalds" somewhere in the quote text, author first/last, or tag.
# Be sure each quote is only listed once in the results.  Do not use __contains (use SearchVector).
# Expected results: 1 Quote

qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(search='Torvalds').distinct('id')
run(2, qry)


# LEARNING QUERY 3
# Create a single query that includes annotations containing one ore more SearchVectors to query
# Quote objects with the word "CONSTRUCT" somewhere in the quote text, author first/last, or tag.
# Be sure each quote is only listed once in the results.  Do not use __contains (use SearchVector).
# Note that even though you are searching for all uppercase, SearchVectors will automatically look
# for lowercase as well as forms of the word (construction, constructing, etc.).
# Expected results: 1 Quote

qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(search='CONSTRUCT').distinct('id')
run(3, qry)


# LEARNING QUERY 4
# Create a single query that includes annotations containing one ore more SearchVectors to query
# Quote objects with the words "write" AND "software" somewhere in the quote text, author first/last, or tag.
# Be sure each quote is only listed once in the results.  Do not use __contains (use SearchVector).
# Note that even though you are searching for all uppercase, SearchVectors will automatically look
# for lowercase as well as forms of the word (construction, constructing, etc.).
# Expected results: 2 Quotes

search = 'write software'

string = search.split()
print(string)
qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(Q(search=str(string[0])) & Q(search=string[1])).distinct('id')
run(4, qry)


# LEARNING QUERY 5
# Create a single query that includes annotations containing one ore more SearchVectors to query
# Quote objects with the words "construct" OR "anonymous" somewhere in the quote text, author first/last, or tag.
# Be sure each quote is only listed once in the results.  Do not use __contains (use SearchVector).
# Expected results: 7 Quotes


qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(Q(search='anonymous') | Q(search='construct')).distinct('id')
run(5, qry)


# LEARNING QUERY 6
# Create a single query that includes annotations containing one ore more SearchVectors to query
# Quote objects with the word "Rick Cook" somewhere in the quote text, author first/last, or tag.
# You SHOULD NOT split to "Rick" and "Cook" but search as a single string, "Rick Cook".  Try to
# combine the author first and last name dynamically within the query so you can search the full
# author name with that "virtual" field.
# Be sure each quote is only listed once in the results.  Do not use __contains (use SearchVector).
# Expected results: 1 Quote

qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(search='Rick Cook').distinct('id')
run(6, qry)