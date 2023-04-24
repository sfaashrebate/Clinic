from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from account.serializers import AccountSerializer
from account.models import Account

@api_view(['POST', ])
def registration_view(request):

  if request.method == 'POST':
    serializer = AccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
      serializer.save()
      data['response'] = 'successfully registered new user.'
      data.update(serializer.data)
    else:
      data = serializer.errors
    return Response(data)   


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def account_properties_view(request):
  account = request.user
  if request.method == 'GET':
    serializer = AccountSerializer(instance=account)
    return Response(serializer.data)
