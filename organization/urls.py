from django.urls import path
from .views import register, login_view, dashboard_view,registration_success,logout_view

app_name = 'organization'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('registration_success/', registration_success, name='registration_success'),
    path('logout/', logout_view, name='logout'),
]

