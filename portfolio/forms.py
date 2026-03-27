from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'What is this about?'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about your project or idea...',
                'rows': 6,
            }),
        }
