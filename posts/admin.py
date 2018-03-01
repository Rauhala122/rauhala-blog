# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Posts
from .models import Authors
from .models import Categories
from .models import Comment

admin.site.register(Posts)
admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(Comment)

# Register your models here.
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
