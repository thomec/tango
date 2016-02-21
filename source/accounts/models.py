# accounts/models.py


from django.db import models


class User(models.Model):
    email = models.EmailField()
    REQUIRED_FIELDS = ()
    USERNAME_FIELD = 'email'
