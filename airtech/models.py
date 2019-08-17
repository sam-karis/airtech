from django.db import models


class BaseModel(models.Model):
    '''
    Base model inherited by all other model

    attributes:
      - created_at: Holds the time an instance is created
      - update_at: Holds the last time an instance was updated
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
