from django.urls import path
from . import views
urlpatterns = [
    path('',views.Alltests,name='all tests'),
    path('test/<str:pk>/',views.test,name = 'test')
]
