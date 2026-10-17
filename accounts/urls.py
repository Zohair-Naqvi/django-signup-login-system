from django.contrib import admin
from django.contrib.admin import views
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',view=views.signup, name='signup'),
    path('login/', view=views.login, name='login'),
    path('dashboard/', view=views.dashboard, name='dashboard'),
    path('logout/', view=views.logout, name='logout'),
]
