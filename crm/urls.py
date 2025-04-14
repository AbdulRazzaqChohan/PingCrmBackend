from django.urls import path
from .views import CompanyListCreateView, CompanyDetailView, ContactListCreateView, ContactDetailView

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
