from django.urls import path
from analysisApp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about',views.about,name="about"),
    path('contact', views.contact, name="contact"),

    path('services',views.services,name="servies"),
    
    path('upload', views.upload_file, name='upload'),
    path('result', views.get_plot, name='result'),
    path('data_analysis_results/', views.data_analysis_results, name='data_analysis_results'),
    path('display_data_analysis/', views.display_data_analysis, name='display_data_analysis')
]
