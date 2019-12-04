from django.db import models
from conduit.apps.core.models import TimestampedModel


class Country(TimestampedModel):
    country = models.CharField(max_length=255)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.country
