from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterSerializer , UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import *


class RegisterView(APIView):
    """ this is a view for registering the users """
    srz_variable = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class AllUsersView(APIView):
    permission_classes = [IsAdminUser , IsAuthenticated]
    def get(self , request):
        query_set = User.objects.all()
        srz_data = UserSerializer(instance=query_set , many=True)
        return Response(data=srz_data.data)
    


