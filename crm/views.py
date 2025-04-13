from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company, Contact
from .serializers import CompanySerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticated

# Company Views
class CompanyListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all().order_by('-created_at')
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# Contact Views
class ContactListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.select_related('company').all().order_by('-created_at')
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['company']
    search_fields = ['first_name', 'last_name', 'email', 'phone']

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.select_related('company').all()
    serializer_class = ContactSerializer
