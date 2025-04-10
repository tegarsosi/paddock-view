from tortoise import fields

from app.db.helpers.datetime_adjusted import DatetimeAdjustedField
from app.db.models.base import BaseModel

MAX_CHAR_LENGTH = 255


class Session(BaseModel):
    """Session model."""
    date_utc = DatetimeAdjustedField()
    grand_prix = fields.ForeignKeyField("models.GrandPrix", related_name="sessions")
    session_type = fields.ForeignKeyField("models.SessionType", related_name="sessions")

    class Meta:
        table = "sessions"
