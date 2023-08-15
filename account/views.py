from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser
from rest_framework.permissions import IsAuthenticated
from account.serializers import AccountSerializer, PasswordSerializer
from account.models import Account
from rest_framework import viewsets
from rest_framework import mixins, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action


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

class PasswordView(
    viewsets.GenericViewSet
):
    queryset = Account.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'
    parser_classes = [MultiPartParser,FormParser,JSONParser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
