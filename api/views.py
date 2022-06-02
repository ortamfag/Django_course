from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework
from django.db.models import Q
from api.serializers import GroupSerializer, ProjectSerializer, StudentSerializer
from api.models import Group, Project, Student

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user', 'projects', 'group']


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OneViewSet(ModelViewSet):
    queryset = Group.objects.filter(Q(number='201-321'))
    serializer_class = GroupSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
