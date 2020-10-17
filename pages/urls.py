from django.urls import path

from .views import ( 
    HomeView,
    download_free_pdf, 
)


app_name = 'pages'
urlpatterns = [

    path('', HomeView.as_view(), name='index'),
    path('download/<slug:slug>', download_free_pdf, name='download'),

]