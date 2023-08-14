from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser
from rest_framework.permissions import IsAuthenticated
from account.serializers import AccountSerializer
from account.models import Account
from rest_framework import viewsets
from rest_framework import mixins, generics
from rest_framework.parsers import MultiPartParser


@api_view(['POST', ])
@parser_classes([MultiPartParser, FormParser])
def registration_view(request):
    pass

#   if request.method == 'POST':
#     serializer = AccountSerializer(data=request.data)
#     data = {}
#     if serializer.is_valid():
#       serializer.save()
#       data['response'] = 'successfully registered new user.'
#       data.update(serializer.data)
#     else:
#       data = serializer.errors
#     return Response(data)


class RegisterViewSet(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'successfully registered new user.'
            data.update(serializer.data)
        else:
            data = serializer.errors
        return Response(data)

# @api_view(['GET', ])
# @permission_classes((IsAuthenticated, ))
# def account_properties_view(request):
#   account = request.user
#   if request.method == 'GET':

#     serializer = AccountSerializer(instance=account)
#     return Response(serializer.data)


class AccountViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'
    parser_classes = [MultiPartParser,FormParser,JSONParser]
