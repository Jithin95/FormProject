from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class SurveyModel(models.Model):

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

    username = models.CharField(max_length=120)
    email = models.EmailField()
    age = models.IntegerField()
    currentPos = models.CharField(max_length =100, choices = CURRENT_POS)
    gender = models.CharField(max_length =10, choices = GENDER_CHOICE)
    languageProficient = MultiSelectField(choices = LANGUAGE_CHOICE)
    address = models.TextField()
    image = models.ImageField(upload_to='documents/', blank = True)

    def __str__(self):
        return self.username
