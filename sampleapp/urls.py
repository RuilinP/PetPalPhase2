from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>/<int:age>', views.hello),
    path('myclass/<str:code>/<int:year>/<str:semester>', views.myclass),
]