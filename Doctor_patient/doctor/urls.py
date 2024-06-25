# urls.py
from django.urls import path
from .views import SignUpView
from .views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('patient_api/', get_all_patient_info, name='patient_api'),
    path('patient_create/', patient_create, name='patient_create'),
    path('edit_patient_details/', edit_patient_details, name='edit_patient_details'),
]
