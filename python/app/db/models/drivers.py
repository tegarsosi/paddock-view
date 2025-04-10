from tortoise import fields

from app.db.models.base import BaseModel

MAX_CHAR_LENGTH = 255


class Driver(BaseModel):
    """Driver model."""
    number = fields.IntField()
    abbreviation = fields.CharField(max_length=MAX_CHAR_LENGTH)
    first_name = fields.CharField(max_length=MAX_CHAR_LENGTH)
    last_name = fields.CharField(max_length=MAX_CHAR_LENGTH)
    team = fields.ForeignKeyField("models.Team", related_name="drivers")

    class Meta:
        table = "drivers"
