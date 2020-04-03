from django.urls import path
from .views import (RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView,
                    UsersRetrieveSearchViewSet)
urlpatterns = [
    path('signup', RegistrationAPIView.as_view(), name='user-registration'),
    path('login', LoginAPIView.as_view(), name='user-login'),
    path('profile', UserRetrieveUpdateAPIView.as_view(),
         name='user-retrieve-update'),
    path('retrieve', UsersRetrieveSearchViewSet.as_view(
        {'get': 'search'}), name='users-retrieve-search')

]
