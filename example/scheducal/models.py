from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from rest_framework.authtoken.models import Token
from pay_period.models import PayPeriod

class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)
    is_project = models.BooleanField()

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'is_project': self.is_project
        }

    def __unicode__(self):
        return unicode(self.name)

class BaseEvent(models.Model):
    user = models.ForeignKey(User)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    comments = models.TextField(blank=True, null=True)

    @property
    def duration(self):
        stime = timedelta(hours=self.start_time.hour,minutes=self.start_time.minute)
        etime = timedelta(hours=self.end_time.hour,minutes=self.end_time.minute)
        return etime-stime
    
    def __unicode__(self):
        return unicode(self.category)	

    class Meta:
        abstract = True

class WorkEvent(BaseEvent):
    category = models.ForeignKey(Category)
    on_campus = models.BooleanField()

    @property
    def pay_period(self):
        return PayPeriod.objects.filter(start__lte=self.start_date) \
                         .filter(end__gte=self.start_date)[0]

    def to_dict(self):
        return {
            'id': self.pk,
            'user': self.user.id,
            'start_time': unicode(self.start_time),
            'end_time': unicode(self.end_time),
            'start_date': unicode(self.start_date),
            'comments': self.comments,
            'duration': unicode(self.duration),
            'category': self.category.id,
            'on_campus': self.on_campus
        }
    
# To be used when adding schedule functionality
class ScheduleEvent(BaseEvent):
    end_date = models.TimeField()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
