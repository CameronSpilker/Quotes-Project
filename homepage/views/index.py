from django.conf import settings
from django import forms
from django_mako_plus import view_function
from django.contrib.postgres.search import SearchVector

from homepage import models as hmod
from .. import dmp_render, dmp_render_to_string


@view_function
def process_request(request):
    '''Shows the quotes, processing the search form if submitted.'''
    # render the context
    context = {
    }
    return dmp_render(request, 'index.html', context)






class QuotesTable(list):
    '''
    A simple class to create an HTML table.
    This inherits from list, so add to it just as you would any other list in python:

        qry = hmod.Quote.objects.....()

        table = QuotesTable()
        table.append([ 'Cell 1a', 'Cell 1b', 'Cell 1c' ])
        table.append([ 'Cell 2a', 'Cell 2b', 'Cell 2c' ])
        print(table)
    '''
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
