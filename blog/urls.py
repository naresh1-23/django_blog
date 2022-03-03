from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index' ),
    path('post/<str:pk>', views.post , name = 'post'),
    path('input', views.input, name = 'input'),
]