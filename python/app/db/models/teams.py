from tortoise import fields

from app.db.models.base import BaseModel

MAX_CHAR_LENGTH = 255


class Team(BaseModel):
    """Team model."""
    name = fields.CharField(max_length=MAX_CHAR_LENGTH)
    short_name = fields.CharField(max_length=MAX_CHAR_LENGTH)
    country = fields.CharField(max_length=MAX_CHAR_LENGTH)

    class Meta:
        table = "teams"
