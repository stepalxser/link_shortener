from tortoise import models, fields


class Link(models.Model):
    id = fields.IntField(pk=True)
    slug = fields.CharField(max_length=64, unique=True)
    url = fields.CharField(max_length=2084)