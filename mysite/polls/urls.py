from django.urls import path
from polls.views import res
from polls.views import dynamic_view

urlpatterns = [
    path('', res),
    path("<str:name>", dynamic_view)
]