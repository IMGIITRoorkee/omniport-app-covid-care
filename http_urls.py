from django.urls import path

from Covid_Care.views.hello_world import HelloWorld

app_name = 'Covid_Care'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
