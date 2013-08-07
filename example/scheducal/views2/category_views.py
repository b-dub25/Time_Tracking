from django.contrib.auth.models import (
        User,
        AnonymousUser,
    )
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from scheducal.models import Category
from pay_period.models import PayPeriod
from scheducal.serializers import (
        UserSerializer, 
        CategorySerializer
    )
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
