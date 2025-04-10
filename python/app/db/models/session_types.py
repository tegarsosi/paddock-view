from tortoise import fields

from app.db.models.base import BaseModel

MAX_CHAR_LENGTH = 255


class SessionType(BaseModel):
    """Session type model."""
    name = fields.CharField(max_length=MAX_CHAR_LENGTH)
    code = fields.CharField(max_length=MAX_CHAR_LENGTH)

    class Meta:
        table = "session_types"
