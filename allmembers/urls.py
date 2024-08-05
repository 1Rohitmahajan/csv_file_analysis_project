from django.urls import path
from allmembers.views import Signup, Loginuser, logoutuser

urlpatterns = [
    path('signup', Signup.as_view(), name='signup'),
    path('login', Loginuser.as_view(), name='login'),
    path('logout', logoutuser, name='logout'),
]
