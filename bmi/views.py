from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.serializers import AccountSerializer
from account.models import Account
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser

from bmi.serializers import BMISerializer


class BmiViewSet(GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = BMISerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser,JSONParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('******')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
