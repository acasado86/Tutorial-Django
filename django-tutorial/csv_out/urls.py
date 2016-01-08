from django.conf.urls import url

from . import views

app_name = 'csv_out'
urlpatterns = [
    url(r'^$', views.some_view, name='some_view_csv'),
]