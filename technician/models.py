from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from customer import models as customer_model


class Company(models.Model):
    name = models.CharField(_('Company'), max_length=100, blank=False, null=False)
    owner = models.ForeignKey(customer_model.Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companys')

    def __unicode__(self):
        return self.name


class Technician(models.Model):
    customer = models.OneToOneField(customer_model.Customer, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('technician')
        verbose_name_plural = _('technicians')

    def __unicode__(self):
        return self.customer.user.email


class Service(models.Model):
    name = models.CharField(_('Service name'), max_length=100, blank=False, null=False)
    technicians = models.ManyToManyField(Technician, through='TechnicianToService')

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __unicode__(self):
        return self.name


class TechnicianToService(models.Model):
    RATING = (
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent')
    )
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)
    fee = models.IntegerField(_('fee'), default=0, blank=True, null=True)
    rating = models.IntegerField(_('rating'), choices=RATING, default=0)

    class Meta:
        verbose_name = _('service_to_technician')
        verbose_name_plural = _('service_to_technicians')

    def __unicode__(self):
        return self.technician.customer.user.email + ' To ' + self.service_type.name
