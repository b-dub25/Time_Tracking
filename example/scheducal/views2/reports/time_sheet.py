from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from scheducal.models import WorkEvent
from scheducal.serializers import ViewWorkEventSerializer
from pay_period.models import PayPeriod

from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def view(request, user_id=None, payperiod_id=None):
    """
        This view will return timesheets from PayPeriod model ranges. If no user id is specified, all
        time sheets will be returned. If no PayPeriod is specified, current period will be returned.
    """
    if not isinstance(request.user, User) or not request.user.is_staff:
        raise PermissionDenied

    payperiod = PayPeriod.objects.get(id=payperiod_id) \
        if payperiod_id \
        else PayPeriod._get_current_period()

    dates = (payperiod.start, payperiod.end)
    query = WorkEvent.objects.filter(start_date__range=dates)
    if user_id:
        query = query.filter(user_id=user_id)
    serializer = ViewWorkEventSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
