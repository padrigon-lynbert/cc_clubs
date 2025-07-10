from django.urls import path
from .views import terms_and_conditions

urlpatterns =[
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
]