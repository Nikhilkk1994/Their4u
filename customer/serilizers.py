from __future__ import unicode_literals

from rest_framework.authtoken.models import Token
from rest_framework import (
    serializers as rest_serializers
)

from customer import models as customer_models


class BaseUserSerializer(rest_serializers.ModelSerializer):
    """
    Serializer for user(customer, ect)
    """
    class Meta:
        model = customer_models.User
        fields = ('email', 'first_name', 'last_name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


class CustomerSignInSerilizer(rest_serializers.ModelSerializer):
    """
    Serializer for New Customer Sign In
    """
    user = BaseUserSerializer()
    zip_code = rest_serializers.CharField(max_length=40, required=True, trim_whitespace=True)
    is_technician = rest_serializers.SerializerMethodField()
    is_company_owner = rest_serializers.SerializerMethodField()
    access_token = rest_serializers.SerializerMethodField()

    class Meta:
        model = customer_models.Customer
        fields = ('user', 'zip_code', 'address', 'city', 'state', 'is_technician', 'is_company_owner', 'access_token',)
        extra_kwargs = {
            'is_technician': {
                'read_only': True
            },
            'is_company_owner': {
                'read_only': True
            }
        }

    def get_access_token(self, instance):
        return Token.objects.get(user=instance.user).key

    def get_is_technician(self, instane):
        return False

    def get_is_company_owner(self, instance):
        return False

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = customer_models.User.objects.create(**user)
        # create Location
        zip_code = validated_data.pop('zip_code')
        zip_code,_ = customer_models.Location.objects.get_or_create(zip_code=zip_code)
        validated_data['zip_code'] = zip_code
        # create customer object
        validated_data['user'] = user
        customer = customer_models.Customer.objects.create(**validated_data)
        return customer
