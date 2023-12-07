from django.urls import path
from .views import home,scholarship_form,success_view,update_scholarship

app_name = 'scholarship'

urlpatterns = [
  path('', home, name='home'),
  path('scholarship_form/', scholarship_form, name='scholarship_form'),
  path('success_page/', success_view, name='success_page'),
  path('update/<int:scholarship_id>/', update_scholarship, name='update'),
]



