from django.urls import path
from . import views

urlpatterns=[
    path('generate-invoice/', views.generate_Invoice, name='generate-invoice'),
]