from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name="create"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('profile/<str:pk>',views.userProfile,name="profile"),
    path('test/<str:pk>/',views.test,name = 'test'),
    path('search/',views.search,name = 'search'),
    path('report_section/',views.reports,name = 'reportsection'),
    path('All reports/',views.viewReports,name = 'reports'),
    path('upload/',views.upload,name = 'upload'),
    path('download_pdf/<str:pk>/',views.download_pdf,name = 'download'),
]
