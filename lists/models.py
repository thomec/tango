# lists/models.py


from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    list = models.ForeignKey(List, default=None, null=True)
    text = models.TextField(default='')



