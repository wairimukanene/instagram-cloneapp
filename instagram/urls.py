from django.urls import path
from instagram import views


urlpatterns = [
  path('',views.index, name='index')
]