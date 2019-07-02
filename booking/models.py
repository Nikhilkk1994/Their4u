from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from customer import models as customer_model
from technician import models as technician_models


class Booking(models.Model):
    STATUS = (
        (0, 'Pending'),
        (1, 'Active'),
        (2, 'Complete'),
        (3, 'Cancelled')
    )
    customer = models.ForeignKey(customer_model.Customer, on_delete=models.CASCADE)
    technician = models.ForeignKey(technician_models.Technician, on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(_('status of booking'), choices=STATUS, default=0)
    location = models.ForeignKey(customer_model.Location, on_delete=models.CASCADE)
    service_type = models.ForeignKey(technician_models.Service, on_delete=models.CASCADE)
    start_date = models.DateTimeField(_('start date'), blank=False, null=False)
    end_date = models.DateTimeField(verbose_name=_('End Date'), null=False, blank=False)

    class Meta:
        verbose_name = _('booking')
        verbose_name_plural = _('bookings')

    def __unicode__(self):
        return self.customer.user.email + ' {status} '.format(status=self.get_status_display()) + self.service_type.name
