from django.urls import path
from . import views
urlpatterns = [
    path('',views.Alltests,name='all tests'),
    path('create/',views.create,name="create"),
    path('test/<str:pk>/',views.test,name = 'test'),
    path('reports/',views.reports,name = 'report'),
    path('repo/',views.Allreports,name = 'repo'),
    path('upload/',views.upload,name = 'upload'),
    path('view/<str:pk>/',views.ViewReport,name = 'view'),
    
]
