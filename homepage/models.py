from django.db import models
import textwrap



class Author(models.Model):
    '''An author of a quote'''
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        elif self.last_name:
            return self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return 'Unspecified'


class Quote(models.Model):
    '''A quote about software development'''
    text = models.TextField()
    author = models.ForeignKey(Author, related_name='quotes')

    def __str__(self):
        wrapped_text = textwrap.wrap(self.text, width=40)
        lines = [ '{:4d}.  {:42s} by {:20} {}'.format(
            self.id,
            wrapped_text[0],
            str(self.author)[:20],
            [ qt.tag.text for qt in self.quote_tags.all() ],
        )]
        for wt in wrapped_text[1:]:
            lines.append('       {}'.format(wt))
        return '\n'.join(lines)


class Tag(models.Model):
    '''A single word that describes a quote.'''
    text = models.TextField()


class QuoteTag(models.Model):
    '''Association class that connects tags and quotes'''
    tag = models.ForeignKey(Tag, related_name='quote_tags')
    quote = models.ForeignKey(Quote, related_name='quote_tags')
