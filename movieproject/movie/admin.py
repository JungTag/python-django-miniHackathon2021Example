from django.contrib import admin
from .models import Movie, Comment, Staff

# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Staff)