from django.contrib.auth.models import User
from django.core.exceptions import (
        ObjectDoesNotExist,
        PermissionDenied,
    )
from scheducal.serializers import UserSerializer 
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user

        # Checks to see if user is admin or checking 
        # their own account
        if int(user.pk) != int(self.kwargs['pk']):
            if user.is_staff == False:
                raise PermissionDenied
        return User.objects.all()
