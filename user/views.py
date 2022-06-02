from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from django.db.utils import IntegrityError
from rest_framework.exceptions import AuthenticationFailed, ParseError, ValidationError, NotFound
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import User


class AuthenticationViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False, url_path='register', url_name='register')
    def register(self, request):
        if 'email' not in request.data:
            raise ParseError({'message': 'Email cannot be empty'})

        if 'password' not in request.data:
            raise ParseError({'message': 'Password cannot be empty'})

        try:
            user = User.objects.create_user(email=request.data['email'])
            user.set_password(request.data['password'])
            user.is_active = True
            user.save()
            return Response({'message': 'success'})
        except IntegrityError:
            return Response({'message': 'User with this email already exist'})


    @action(methods=['POST'], detail=False)
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'email': ['Email must be provided']})
        if 'password' not in request.data:
            raise ValidationError({'password': ['Password must be provided']})

        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'message': 'User with provided credentials does not exist'})

        if not user.check_password(request.data.get('password')):
            raise AuthenticationFailed({'message': 'Incorrect password'})

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response

    @action(methods=['GET'], detail=False,
            permission_classes=[IsAuthenticated], url_path='me')
    def user(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response(data)
