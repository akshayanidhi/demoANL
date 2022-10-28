from django.urls import path

from . import views
app_name='banking_app'
urlpatterns = [
    path('', views.operations, name="operations"),

]

