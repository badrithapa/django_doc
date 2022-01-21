from django.contrib import admin
from .models import Question, Choice
admin.site.register(Question) # this makes the polls app modifiable
##this arlso tell the admin that Question objects have admin interface so that it will be displyed in admin index page
admin.site.register(Choice) ## this tells that choice can be seen in admin index and modified there withou any command lines

# Register your models here.
