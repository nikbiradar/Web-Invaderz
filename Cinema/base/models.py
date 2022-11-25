from django.db import models
import uuid


# Constructing a Base model to uniquely identify an object of a model
class BaseModel(models.Model):
    # Universal Unique Identifier, is a python library that helps in generating random objects of 128 bits as ids
    uid = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    # Date-Time Created at, Updated at
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        abstract = True 