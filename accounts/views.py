from rest_framework.response import Response
from rest_framework import status, generics , viewsets
from rest_framework.views import APIView
from .serializers import  UserSerializer, SectionSerializer, WorkerSerializer, WorkerSectionSerializer , HelpWorkerSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Section, Workers, SectionUser , Help
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication





class SectionListView(generics.ListAPIView):
    """This view returns all sections, only accessible by admin users"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]



class WorkersBySectionView(APIView):
    """This view is for listing workers in a specific section"""

    def get(self, request, section_name):
        try:
            section = Section.objects.get(value=section_name)
        except Section.DoesNotExist:
            return Response({"message": "بخش یافت نشد."}, status=status.HTTP_404_NOT_FOUND)
        
        workers = Workers.objects.filter(section=section)

        serializer = WorkerSectionSerializer(workers, many=True)
        
        return Response(serializer.data)

class WorkerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing workers.
    """
    queryset = Workers.objects.all()
    serializer_class = WorkerSectionSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "کاربر با موفقیت حذف شد."}, status=status.HTTP_200_OK)
    


class HelpWorkerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing workers helps money
    """
    queryset = Help.objects.all()
    serializer_class = HelpWorkerSerializer
    permission_classes = [IsAdminUser , IsAuthenticated]

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "کاربر با موفقیت حذف شد."}, status=status.HTTP_200_OK)
    
    
    
class TokenVerifyView(APIView):
    """
    this view is for verifying the tokens using GET request
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        auth = JWTAuthentication()

        try:
            token = request.headers.get('Authorization').split(' ')[1]
            auth.get_validated_token(token)
            return Response({"message": "توکن معتبر است"}, status=status.HTTP_200_OK)
        except (InvalidToken, AttributeError):
            return Response({"message": "توکن معتبر نیست یا کاربر موجود نیست"}, status=status.HTTP_401_UNAUTHORIZED)

