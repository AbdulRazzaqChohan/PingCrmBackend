from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListCreate.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('contacts/', views.ContactListCreate.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', views.ContactDetail.as_view(), name='contact-detail'),
]
