from rest_framework.serializers import ModelSerializer
from api.models import Group, Project, Student


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['number']


class StudentSerializer(ModelSerializer):
    group_data = GroupSerializer(source='group')
    project_data = ProjectSerializer(source='projects', many=True)
    class Meta:
        model = Student
        exclude = ['group', 'projects']
