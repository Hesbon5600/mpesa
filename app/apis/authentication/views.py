from django.conf import settings
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import (RegistrationSerializer, UserRetrieUpdateSerializer, LoginSerializer,
                          UserSearchSerializer)
from ..helpers.renderers import RequestJSONRenderer
from ..helpers.constants import (SIGNUP_SUCCESS_MESSAGE)
from ..helpers.pagination_helper import Pagination
from .models import User


class RegistrationAPIView(generics.CreateAPIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Handle user Signup
        """
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        data = serializer.data

        return_message = {'message': SIGNUP_SUCCESS_MESSAGE,
                          'user': data}
        return Response(return_message, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.CreateAPIView):
    # Login user class
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Handle user signup
        """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """
    Class that handles retrieving and updating user info
    """
    permission_classes = (IsAuthenticated,)
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = UserRetrieUpdateSerializer

    def get(self, request, *args, **kwargs):
        """
        retrieve user details from the token provided
        """
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        """
        Update user
        """
        data = request.data
        serializer = self.serializer_class(
            request.user, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersRetrieveSearchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve: Return users.
    list: Return a list of users
    """
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(
        deleted=False, is_active=True).order_by('first_name')
    serializer_class = UserSearchSerializer
    pagination_class = Pagination
    filter_backends = (SearchFilter,)
    search_fields = ('first_name', 'last_name',
                     'email', 'phone_number',)

    @action(methods=['GET'], detail=False, url_name='Search users')
    def search(self, request, *args, **kwargs):
        """
        Search users
        """
        return super().list(request, *args, **kwargs)