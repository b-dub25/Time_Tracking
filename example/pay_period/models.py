from django.db import models
import datetime

class PayPeriod(models.Model):
    name = models.CharField(max_length=20,unique=True)
    start = models.DateField()
    end = models.DateField()

    def __unicode__(self):
        return unicode(self.name)

    @staticmethod
    def _get_current_period():
       today = datetime.datetime.utcnow().date()
       return PayPeriod.objects.get(start__lte=today,
                                    end__gte=today) 

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'start': unicode(self.start),
            'end': unicode(self.end),
        }
