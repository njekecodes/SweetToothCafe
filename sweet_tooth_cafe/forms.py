from django import forms

from sweet_tooth_cafe.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput,
            'dob': forms.DateInput(attrs={'min': '1940-01-01', 'max': '2005-01-01', 'type': 'date'}),

        }


#
# class SearchFilters(forms.ModelForm):
#     class Meta:
#         model = SearchFilters
#

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'email',
            'dob',
            'profile_pic',
            'password'
        )

        widgets = {
            'password': forms.PasswordInput(),
            'dob': forms.DateInput(attrs={'min': '1940-01-01', 'max': '2005-01-01', 'type': 'date'}),

        }
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
