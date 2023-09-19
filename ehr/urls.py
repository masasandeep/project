from django.urls import path
from . import views
urlpatterns = [
    path('',views.Alltests,name='all tests'),
    path('create/',views.create,name="create"),
    path('test/<str:pk>/',views.test,name = 'test'),
    path('search/',views.search,name = 'search'),
    path('report_section/',views.reports,name = 'reportsection'),
    path('All reports/',views.viewReports,name = 'reports'),
    path('upload/',views.upload,name = 'upload'),
    path('download_pdf/<str:pk>/',views.download_pdf,name = 'download'),
]
