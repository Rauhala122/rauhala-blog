# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Comment(models.Model):
    text = models.TextField()
    creator = models.CharField(max_length=50, default="Unknown", blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return "{id}".format(id=self.id)

    class Meta:
        verbose_name_plural = "Comments"


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    author = models.ManyToManyField(Authors)
    category = models.ManyToManyField(Categories)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
