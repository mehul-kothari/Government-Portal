from django import forms
from django.contrib.auth.models import User

from Login.models import form2, Area,Locality,Areas,Localities,Discussion,UserProfile,SpecificLocality

CATEGORIES = (
    ('Mumbai Central', 'mumbai central'),
    ('Goregaon', 'goregaon'),


)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('area1',)

    #birthdate = forms.DateField(widget=extras.SelectDateWidget,required=False)
    area1=forms.ChoiceField(choices=[])
    #locality = forms.ModelChoiceField(queryset=GeneralProblems.objects.all(), empty_label=None)
    def __init__(self, *args, **kwargs):
        super(AreaForm, self).__init__(*args, **kwargs)
        print("anything1")
        self.fields['area1'].choices = [(x.pk, x.areas1) for x in Areas.objects.all()]
        print("anything1")


class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ( 'locality1',)

    #birthdate = forms.DateField(widget=extras.SelectDateWidget,required=False)
    #area=forms.ModelChoiceField(queryset=GeneralProblems.objects.all(),empty_label=None)
    locality1 = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(LocalityForm, self).__init__(*args, **kwargs)
        self.fields['locality1'].choices = [(x.pk, x.localities1) for x in Localities.objects.all().filter(areas2__areas1="Mumbai central")]

class form2form(forms.ModelForm):
    class Meta:
        model = form2
        fields = ('details',)

    details = forms.CharField(widget=forms.Textarea(attrs={'class' : 'md-form','placeholder':"comment"}),label='')


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ('comment',)

    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'md-form','placeholder':"comment"}),label='')




class Spec_LocalityForm(forms.ModelForm):
    class Meta:
        model = SpecificLocality
        fields = ('comment',)

    comment = forms.CharField(widget=forms.Textarea(attrs={'class' : 'md-form','placeholder':"comment"}),label='')




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('photo',)

    photo = forms.ImageField(required=False)




class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)



class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"),
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                    )
        return password2

