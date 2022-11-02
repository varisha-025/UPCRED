import django_filters
from django_filters import CharFilter

from .models import *

class ContactFilter(django_filters.FilterSet):
	
	email = CharFilter(field_name='email', lookup_expr='icontains')

	class Meta:
		model = Contact
		fields = ['email']