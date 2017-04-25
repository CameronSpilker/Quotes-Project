from django.conf import settings
from django import forms
from django_mako_plus import view_function
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
import csv

from homepage import models as hmod
from .. import dmp_render, dmp_render_to_string

@view_function
def process_request(request):
    '''Shows the quotes, processing the search form if submitted.'''
    # render the context
    qry = hmod.Quote.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print('IS VALID')
            s = form.cleaned_data.get('search')
            choice = form.cleaned_data.get('choice')
            print(choice)
            if not s:
                print('empty string')
                qry = hmod.Quote.objects.all()
            else:
                if choice == 'and':
                    qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(Q(search=str(s))).distinct('id')
                # else:
                #     print('in the else', s)
                #     qry = hmod.Quote.objects.annotate(search=SearchVector('author__first_name', 'author__last_name') + SearchVector('quote_tags__quote__text') + SearchVector('quote_tags__tag__text')).filter(Q(search=str(s[0])) | Q(search=str(s[1]))).distinct('id')
                #     print('here is the results', qry)
        else:
            print('NOT VALID')
        context = {'form': form,
                    'qry': qry,}
        return dmp_render(request, 'index.html', context)
    else:
        form = SearchForm()



    context = {'form': form,
                'qry': qry}
    return dmp_render(request, 'index.html', context)


class SearchForm(forms.Form):

    search = forms.CharField(label="Enter search terms, seperated by spaces", required=False)
    choice = forms.ChoiceField(choices=[['and', 'AND (all terms)'], ['or', 'OR (any term)']], initial='or')

    def clean_search(self):
        print('in the CLEANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
        s = self.cleaned_data.get('search')
        print('search resutls here:', s)
        # search = s.split()
        # print(search)
        if s.find('"'):
            for l in csv.reader([s], delimiter=' ', quotechar='"'):
                print(l)
                search = l
                print(search)
        else:
            search = s.split()
            print(search)

        return search



class QuotesTable(list):
    '''
    A simple class to create an HTML table.
    This inherits from list, so add to it just as you would any other list in python:
'''
    # qry = hmod.Quote.objects.all()
    # print('<>>>>>>>>>>>>>>>>>>>>>>>>>')
    # for q in qry:
    #     print(q.id, q.author, q.text)
    #     for qt in q.quote_tags.all():
    #         print(qt.tag.text)

    # print('>>>>>>>>>>>>>>>>>>>>>')
    # table = QuotesTable()
    # table.append(['Cell 1a', 'Cell 1b', 'Cell 1c'])
    # table.append(['Cell 2a', 'Cell 2b', 'Cell 2c'])
    # print(table)

    table_id = 'quotes_table'
    headings = [
        'Quote ID',
        'Author',
        'Quote Text',
        'Tags',
    ]

    def __str__(self):
        '''
        Prints the html for the table.
        '''
        # start the table
        html = []
        html.append('<table id="{}">'.format(self.table_id))
        # table headings
        html.append('<thead>')
        html.append('<tr class="header_row">')
        for val in self.headings:
            html.append('<th>{}</th>'.format(val))
        html.append('</tr>')
        html.append('</thead>')
        # table data
        html.append('<tbody>')
        for row_i, row in enumerate(self):
            html.append('<tr class="data_row" data-row="{}">'.format(row_i))
            for val in row:
                html.append('<td>{}</td>'.format(val))
            html.append('</tr>')
        html.append('</tbody>')
        # end the table and return
        html.append('</table>')
        return '\n'.join(html)
