from django import forms
from .models import SurveyModel

class NameForm(forms.Form):
    yourName = forms.CharField(label = "Your Name:", max_length=100, required = False)

class FormView(forms.ModelForm):
    class_context = {'class': 'input_field'}
    username_context = {'class': 'input_field','placeholder': 'Enter Your Name.'}
    email_context = {'class': 'input_field','placeholder': 'Enter Your Email.'}
    age_context = {'class': 'input_field','placeholder': 'Enter Your Age.'}
    CURRENT_POS = (
        ('','Select an option'),
        ('student', 'Student'),
        ('job', 'Full Time Job'),
        ('learner', 'Full Time Learner'),
        ('preferNo', 'Prefer not to say'),
        ('other', 'Other'),
    )
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    LANGUAGE_CHOICE = (
        ('C', 'C'),
        ('cplus', 'C++'),
        ('csharp', 'C#'),
        ('html', 'Html'),
        ('jscript', 'Javascript'),
        ('python', 'Python'),
        ('java', 'Java'),
    )

    username = forms.CharField(label = "Name:", required = True,max_length=120,
                               widget=forms.TextInput(attrs= username_context))
    email = forms.EmailField(label = "Email:", required = True,
                             widget=forms.TextInput(attrs= email_context))
    age = forms.IntegerField(label = "Age:", required = True, max_value = 125,
                             widget=forms.TextInput(attrs= age_context))
    currentPos = forms.ChoiceField(choices=CURRENT_POS, label= "Which option best describe your current role:",
                                   widget=forms.Select(attrs= {'class':'dropdown'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required= False, label= "Gender:",
                               widget= forms.RadioSelect())
    languageProficient = forms.MultipleChoiceField(choices=LANGUAGE_CHOICE, label= "Programming Language you know:",
                                           widget= forms.CheckboxSelectMultiple())
    address = forms.CharField(label = 'Address',required= False,
                              widget= forms.Textarea(attrs= {'class':'address', 'placeholder':'Address'}))
    image = forms.ImageField()


    class Meta:
        model = SurveyModel
        fields = ('username', 'email', 'age', 'currentPos', 'gender', 'languageProficient', 'address','image',)


    def clean_username(self):
        username = self.cleaned_data['username']
        print('checkusername')
        print(username)
        try:
            user = SurveyModel.objects.get(username=username)
        except Exception:
            return username
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if len(username) < 5:
    #         raise forms.ValidationError("Less than 5", code="username",)
    #     if len(username) < 100:
    #         raise forms.ValidationError("Give me a username", code="username",)
    #     return  username

    # def clean(self):
    #     print(self.cleaned_data)
    #     email1 = self.cleaned_data['email']
    #     if len(email1) < 100:
    #         raise forms.ValidationError("you can't go below 100", code='email',)
    #     return  self.cleaned_data
