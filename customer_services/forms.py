from django import forms
from .models import ServiceRequest, RequestAttachment, CustomerProfile, RequestNote
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class RequestAttachmentForm(forms.ModelForm):
    class Meta:
        model = RequestAttachment
        fields = ['file', 'description']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['address', 'phone_number']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if not re.fullmatch(r'\d{10}', phone):
            raise ValidationError('Phone number must be exactly 10 digits.')
        return phone

class RequestNoteForm(forms.ModelForm):
    class Meta:
        model = RequestNote
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

class ServiceRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status', 'priority', 'assigned_to']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] 