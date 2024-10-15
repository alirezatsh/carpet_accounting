from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import  UserSerializer, SectionSerializer, WorkerSerializer, WorkerSectionSerializer , HelpWorkerSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Section, Workers, SectionUser , Help
from rest_framework import viewsets




class SectionListView(generics.ListAPIView):
    """This view returns all sections, only accessible by admin users"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    # permission_classes = [IsAdminUser]



class WorkersBySectionView(APIView):
    """This view is for listing workers in a specific section"""
    def get(self, request, section_name):
        section = Section.objects.get(value=section_name)
        section_users = SectionUser.objects.filter(section=section)
        workers = [section_user.user for section_user in section_users]
        serializer = WorkerSectionSerializer(workers, many=True)
        return Response(serializer.data)

class WorkerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing workers.
    """
    queryset = Workers.objects.all()
    serializer_class = WorkerSectionSerializer
    
    
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
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "کاربر با موفقیت حذف شد."}, status=status.HTTP_200_OK)

