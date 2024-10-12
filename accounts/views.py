from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer, SectionSerializer, WorkerSerializer, WorkerSectionSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Section, Workers, SectionUser
from django.shortcuts import get_object_or_404


class RegisterView(APIView):
    """This is a view for registering users"""
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


class SectionListView(generics.ListAPIView):
    """This view returns all sections, only accessible by admin users"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    # permission_classes = [IsAdminUser]


class WorkerListView(generics.ListAPIView):
    """This view returns all workers, only accessible by admin users"""
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializer
    # permission_classes = [IsAdminUser]


class WorkersBySectionView(APIView):
    """This view is for listing workers in a specific section"""
    def get(self, request, section_name):
        section = Section.objects.get(name=section_name)
        section_users = SectionUser.objects.filter(section=section)
        workers = [section_user.user for section_user in section_users]
        serializer = WorkerSectionSerializer(workers, many=True)
        return Response(serializer.data)


class WorkerDetailView(APIView):
    """This view handles adding, updating, and deleting workers"""

    def post(self, request):
        """Add a new worker"""
        serializer = WorkerSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Update an existing worker"""
        worker = get_object_or_404(Workers, pk=pk)
        serializer = WorkerSectionSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """Partially update an existing worker"""
        worker = get_object_or_404(Workers, pk=pk)
        serializer = WorkerSectionSerializer(worker, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a worker"""
        worker = Workers.objects.get(pk=pk)
        worker.delete()
        return Response({"message": "Worker deleted successfully"}, status=status.HTTP_200_OK)

