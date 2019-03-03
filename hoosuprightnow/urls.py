from django.urls import path, include
from . import views

app_name = 'hoosuprightnow'

urlpatterns = [
    # /
    path('', views.index, name = 'index'),

    # /signup
    path('signup/' , views.SignUp.as_view(), name = 'signup'),

    # /interests
    path('update_activity/' , views.update_activity, name = 'update_activity'),

    # /interests
    path('hoos_online/' , views.hoos_online, name = 'hoos_online'),
]


