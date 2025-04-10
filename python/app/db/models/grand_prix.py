from tortoise import fields

from app.db.models.base import BaseModel

MAX_CHAR_LENGTH = 255


class GrandPrix(BaseModel):
    """Grand Prix model."""
    round = fields.IntField()
    event_name = fields.CharField(max_length=MAX_CHAR_LENGTH)
    location = fields.CharField(max_length=MAX_CHAR_LENGTH)
    country = fields.CharField(max_length=MAX_CHAR_LENGTH)
    year = fields.IntField()

    class Meta:
        table = "grand_prix"
