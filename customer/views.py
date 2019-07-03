from __future__ import unicode_literals

from rest_framework import (
    mixins as rest_mixins,
    permissions as rest_permissions
)
from rest_framework.viewsets import GenericViewSet

from customer import serilizers as customer_serilizer


class UserSignIn(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    ViewSet for Sign In new Customer
    """
    permission_classes = (rest_permissions.IsAuthenticated,)
    serializer_class = customer_serilizer.CustomerSignInSerilizer


class UserLogin(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    ViewSet for login
    """
    serializer_class = customer_serilizer.CustomerSignInSerilizer
