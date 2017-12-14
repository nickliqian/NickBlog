from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class TimeStampMixin(models.Model):
    created = models.DateTimeField(
        verbose_name=_('date created'),
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        verbose_name=_('last modified'),
        auto_now=True,
    )

    class Meta:
        abstract = True
        ordering = ('-modified', '-created',)


class LastSeenMixin(models.Model):
    last_seen = models.DateTimeField(
        verbose_name=_('last seen'),
        auto_now_add=True,
    )

    class Meta:
        abstract = True

    def save(self, update_last_seen=False, *args, **kwargs):
        if update_last_seen:
            self.last_seen = timezone.now()
        super(LastSeenMixin, self).save(*args, **kwargs)


class AdminAbsoluteUrlMixin(object):
    def get_absolute_url(self):
        opts = self._meta
        # support for proxy
        if opts.proxy:
            opts = opts.concrete_model._meta
        return reverse(
            'admin:{}_{}_change'.format(
                opts.app_label, opts.model_name
            ), args=(self.pk,)
        )