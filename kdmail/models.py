from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime


# from kdmail.templatetags import tags
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class edit_profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    consultant_name = models.TextField(default="Enter Candidates Name")
    technology = models.TextField(default="Enter domain for which to be marketted")
    job_location = models.TextField(default="Enter Job location for the Candidate")
    requested_email = models.EmailField(default="Enter email you want to recv reqs")

    def __unicode__(self):
        return self.consultant_name

class user_stats(models.Model):
    user = models.ForeignKey(User)
    consultant_name = models.TextField(default="Enter Candidates Name")
    technology = models.TextField(default="Enter domain for which to be marketted")
    job_location = models.TextField(default="Enter Job location for the Candidate")
    requested_email = models.EmailField(default="email")
    requirements_count = models.IntegerField()
    date_added = models.DateField(default=datetime.date.today())

    def __unicode__(self):
        return self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        q = edit_profile()
        q.user = instance
        q.save()
        # UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


class EmailUser(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = u'User profiles'
