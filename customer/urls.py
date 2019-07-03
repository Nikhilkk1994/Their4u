from __future__ import unicode_literals

from rest_framework import routers

from customer import views as api_views

router = routers.SimpleRouter()

router.register(r'customer/sign-in', api_views.UserSignIn, base_name='customer_sign_in')
router.register(r'customer/login-in', api_views.UserLogin, base_name='customer_login_in')

urlpatterns = [
]

urlpatterns += router.urls