from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime
# from kdmail.templatetags import tags
# Create your models here.


class edit_profile(models.Model):
    user=models.OneToOneField(User,primary_key=True)
    id_field=models.TextField(default="Enter comma separated Gmail Ids")
    pass_field=models.TextField(default="Enter comma separated passwords in sequence")
    def __unicode__(self):
        return self.id_field

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        q= edit_profile()
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
        verbose_name_plural=u'User profiles'

