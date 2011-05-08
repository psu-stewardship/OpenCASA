import arkpy
from django.db import models, IntegrityError
from services.settings import NAME_AUTHORITY, TEMPLATE


class Identifier(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        while True:
            self.name = self.mint()
            try:
                super(Identifier, self).save(*args, **kwargs)
            except IntegrityError:
                continue
            else:
                return

    def mint(self):
        return arkpy.mint(authority=NAME_AUTHORITY,
                          template=TEMPLATE,
                          bare=False)
