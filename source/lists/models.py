# lists/models.py


from django.db import models
from django.core.urlresolvers import reverse


class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):

    list = models.ForeignKey(List, default=None)
    text = models.TextField(default='')

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text