from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_orgarnizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    
    def __str__(self):
        return f' User {self.first_name} {self.last_name}'

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f' Profile {self.user.first_name} {self.user.last_name}'

class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    orgarnization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f' Agent {self.user.first_name} {self.user.last_name}'

class Category(models.Model):
    name = models.CharField(max_length=30)
    orgarnization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f' Category {self.name}'

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=150)
    description = models.TextField()
    address = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    agent = models.ForeignKey(Agent,null=True,blank=True,on_delete=models.SET_NULL)
    orgarnization = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='leads',null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f' Lead {self.first_name} {self.last_name}'


def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user = instance)
        
post_save.connect(create_profile,sender=User)