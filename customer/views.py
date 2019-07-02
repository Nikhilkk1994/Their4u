from __future__ import unicode_literals

from rest_framework import (
    mixins as rest_mixins
)
from rest_framework.viewsets import GenericViewSet

from customer import serilizers as customer_serilizer


class UserSignIn(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    ViewSet for Sign In new Customer
    """
    serializer_class = customer_serilizer.CustomerSignInSerilizer

class CustomerLogin(rest_mixins.CreateModelMixin, GenericViewSet):
    """
    ViewSet for Customer Login
    """


