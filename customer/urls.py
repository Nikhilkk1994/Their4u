from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework import routers

from customer import views as api_views

router = routers.SimpleRouter()

router.register(r'customer/sign-in', api_views.UserSignIn, base_name='customer_sign_in')

urlpatterns = [
]

urlpatterns += router.urls