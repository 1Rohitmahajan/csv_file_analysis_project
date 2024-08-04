from django.urls import path
from allmembers import views


urlpatterns = [
    path('login_user',views.login_user,name="login"),
    path('logoutuser',views.logoutuser,name="logout"),

]
