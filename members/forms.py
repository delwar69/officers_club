from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name', 'designation', 'joining_date', 'department', 'date_of_birth',
            'spouse_name', 'religion', 'gender', 'permanent_address',
            'present_address', 'email', 'mobile', 'phone_office',
            'phone_residence', 'blood_group', 'profile_picture', 'signature'
        ]
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email or '.' not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit() or len(mobile) != 11:
            raise forms.ValidationError("Enter a valid 11-digit mobile number.")
        return mobile