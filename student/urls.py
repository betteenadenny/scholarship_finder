# student/urls.py
from django.urls import path
from .views import register,dashboard_view,registration_success,login_view,update_profile
from django.contrib.auth.views import LogoutView

app_name = 'student'

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='student/logout.html'), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('registration_success/', registration_success, name='registration_success'),
    path('login/', login_view, name='login'),
    path('update_profile/', update_profile, name='update_profile'),
]


