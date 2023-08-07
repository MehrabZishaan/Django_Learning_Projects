from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="User name", initial='Rahim', help_text='Total length must be more than 10', required=False, disabled=False, widget=forms.Textarea(attrs = {'id' : 'text_area', 'class': 'class1 class2', 'placeholder': 'Enter your name'}))
    file = forms.FileField()
    email = forms.EmailField()
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs= {'type': 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs= {'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect)
    MEAL =[('P', 'Pepperoni'), ('M', 'Mushroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget= forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name =forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Enter a name with atleast 10 characters')
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Enter a valid email')
#     #     return valemail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter a name with atleast 10 characters')
#         if '.com' not in valemail:
#             raise forms.ValidationError('Enter a valid email')
    
class StudentData(forms.Form):
    name =forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with atleast 10 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(34, message='Age must be under 35'), validators.MinValueValidator(24, message='Age must be over 23')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message='File extension must be ended with pdf or png')])
                           
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = self.super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password doesen't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be atleast 15 chars")