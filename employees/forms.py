from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter username',
            'id': 'username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter password',
            'id': 'password',
        })
    )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'department', 'designation', 'salary',
            'date_joined', 'status', 'photo', 'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'id': 'first_name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'id': 'last_name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'id': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'id': 'phone',
            }),
            'department': forms.Select(attrs={
                'class': 'form-select',
                'id': 'department',
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Title / Designation',
                'id': 'designation',
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'id': 'salary',
                'step': '0.01',
            }),
            'date_joined': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'id': 'date_joined',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'id': 'status',
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'photo',
                'accept': 'image/*',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Full Address',
                'rows': 3,
                'id': 'address',
            }),
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by name, email, department...',
            'id': 'search_query',
        })
    )
    department = forms.ChoiceField(
        required=False,
        choices=[('', 'All Departments')] + [
            ('HR', 'Human Resources'),
            ('IT', 'Information Technology'),
            ('Finance', 'Finance'),
            ('Marketing', 'Marketing'),
            ('Operations', 'Operations'),
            ('Sales', 'Sales'),
            ('Admin', 'Administration'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'dept_filter',
        })
    )
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'All Status'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('On Leave', 'On Leave')],
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'status_filter',
        })
    )
