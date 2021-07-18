from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
1. "python manage.py makemigration"
make migrations = make changes in models, save them in a file,
for example:
    if we make the length of charfield more or less, then to implement changes, we need to run this command.

2. "python manage.py migrate"
migrate = apply the changes, created by makemigrations
it means apply the pending changes, like makemigration saves the changings in a file,, and by the command later,
we make the changes as confirmed, and apply to our database(in file db.sqlite3)
'''

# tables/model for registration of user
class Register(models.Model):
    userMain = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    email = models.EmailField(('email address'), max_length=50, unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    password = models.CharField(('Password'), max_length=20, blank=True)
    profile_pic = models.ImageField( upload_to='users/', null=True, blank=True)


    DESIGNATION = (
        ('User', 'Just a User'),
        ('Contributor', 'Contributor'),
        ('Editor', 'Editor'),
    )

    designation = models.CharField(
        ('designation'), max_length=20, choices=DESIGNATION, default='User')
    date_registered = models.DateTimeField('Date Registered', null=True)



    @staticmethod
    def get_user_by_email(email):
        return Register.objects.get(email=email)

    def get_user_id(id):
        return Register.object.get(id=id)

    def __str__(self):
        return '{} <{}>'.format(self.first_name, self.email)


# tables/model for contact by user
class Contact(models.Model):
    register = models.ForeignKey(Register, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    SUGGESTION = 'SUGGESTION'
    COMPLAINT = 'COMPLAINT'
    APPRECIATION = 'APPRECIATION'
    REQUEST = 'REQUEST'

    PURPOSE = (
        ('Suggession', 'Suggession'),
        ('Complaint', 'Complaint'),
        ('Appreciation', 'Appreciation'),
        ('Request', 'Request'),
    )

    purpose = models.CharField(('purpose'), max_length=20, choices=PURPOSE, default='Suggession')
    date_registered = models.DateTimeField('Date Sent')

    message = models.TextField(('Message'), max_length=500)
    date_messaged = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.first_name+" "+self.last_name


# courses available
class Courses(models.Model):
    COURSES = (
        ('ITC', 'ITC'),  
        ('EMT', 'EMT'),
        ('Calculus-1', 'Calculus-1'),
        ('Writing-Wrokshop', 'Writing-Wrokshop'),
        ('Statistics', 'Statistics'),
    )

    courseTitle = models.CharField(('COURSES'), max_length=20, choices=COURSES, default='PDF Notes')
    
    def __str__(self):
        return self.courseTitle


# contribution file types, like gd, or a link etc
class ContributionFileType(models.Model):
    contFileType = (
        ('PDF Notes', 'PDF Notes'),
        ('PDF Books', 'PDF Books'),
        ('Link', 'Link'),
    )
    contFileType = models.CharField(('contFileType'), max_length=20, choices=contFileType, default='PDF Notes')

    def __str__(self):
        return self.contFileType
    

# contribution by editors or moderators
class Contributions(models.Model):
    register = models.ForeignKey(Register, null=True, on_delete=models.SET_NULL)
    courseTitle = models.ForeignKey(Courses, null=True, on_delete=models.DO_NOTHING)
    contribFileType = models.ForeignKey(ContributionFileType, null=True, on_delete=models.DO_NOTHING)
    

    author_name = models.CharField(max_length=100)
    contribution_title = models.CharField(max_length=100)
    contribution_file = models.FileField(max_length=100, upload_to='contributions/', null=True, blank=True)
    contribution_link = models.URLField(("Content-Link"),max_length=128, null=True, blank=True)

    def __str__(self):
        return self.author_name 
