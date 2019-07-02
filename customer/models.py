from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token

from customer.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Location(models.Model):
    zip_code = models.CharField(_('zip_code'), max_length=40, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __unicode__(self):
        return self.zip_code


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(_('address'), max_length=100, blank=True, null=True)
    city = models.CharField(_('city'), max_length=40, blank=False, null=False)
    state = models.CharField(_('state'), max_length=40, blank=False, null=False)
    zip_code = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __unicode__(self):
        return self.user.email


@receiver(post_save, sender=User)
def make_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
