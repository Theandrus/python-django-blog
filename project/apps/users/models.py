from datetime import datetime
from django.db import models
from django.urls import reverse


class Group(models.Model):
    group_name = models.CharField('name of the group', max_length=73)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    group_description = models.CharField('description of the group', max_length=123)

    def __str__(self):
        return self.group_name


class User(models.Model):
    user_name = models.CharField('user name', max_length=43)
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created = models.DateTimeField('date of publication', default=datetime.now)

    def __str__(self):
        return self.user_name
