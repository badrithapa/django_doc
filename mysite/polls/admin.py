from django.contrib import admin
from .models import Question
admin.site.register(Question) # this makes the polls app modifiable
##this arlso tell the admin that Question objects have admin interface so that it will be displyed in admin index page

# Register your models here.
