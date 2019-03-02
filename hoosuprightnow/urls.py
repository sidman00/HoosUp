from django.urls import path, include
from . import views

app_name = 'hoosuprightnow'

urlpatterns = [
    # /
    path('', views.index, name = 'index'),

    #/logout_view
    #path('logout_view/', views.logout_view,name = 'logout_view'),

    # /signup
    path('signup/' , views.SignUp.as_view(), name = 'signup'),
]
