from django.contrib.auth.models import (
        User,
        AnonymousUser,
    )
from django.core.exceptions import (
        PermissionDenied,
        ObjectDoesNotExist,
    )
from rest_framework.response import Response
from rest_framework import status
from scheducal.models import WorkEvent, Category
from pay_period.models import PayPeriod
from scheducal.serializers import (
        SaveWorkEventSerializer,
        UserSerializer, 
        CategorySerializer,
    )
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class WorkEventList(generics.ListCreateAPIView):
    serializer_class = SaveWorkEventSerializer

    def get_queryset(self):
        return WorkEvent.objects.filter(user=self.request.user.pk)

    def pre_save(self, obj):
        obj.user = self.request.user

class WorkEventListForPayPeriod(generics.ListCreateAPIView):
    serializer_class = SaveWorkEventSerializer

    def get_queryset(self):
        pay_period = self.kwargs['pay_period']
        pay_period = PayPeriod.objects.get(pk=pay_period) 
        if not pay_period:
            raise ObjectDoesNotExist 
        try:
            return WorkEvent.objects.filter(user=self.request.user, 
                                            start_date__range=[pay_period.start, pay_period.end])
        except:
            raise PermissionDenied

    def pre_save(self, obj):
        obj.user = self.request.user

class WorkEventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaveWorkEventSerializer

    def get_queryset(self):
        event = WorkEvent.objects.get(pk=self.kwargs['pk'])
        user = self.request.user
        if event.user != user:
            if user.is_staff == False:
                raise PermissionDenied
        return WorkEvent.objects.all()

    def pre_save(self, obj):
        obj.user = self.request.user
