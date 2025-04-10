import datetime
from typing import Any

from tortoise import fields, models

from app.db.helpers.datetime_adjusted import DatetimeAdjustedField


class BaseModel(models.Model):
    """Base model."""
    id = fields.IntField(pk=True)
    created_at = DatetimeAdjustedField()
    updated_at = DatetimeAdjustedField()

    async def save(self, *args: Any, **kwargs: Any) -> None:
        """Pre-save hook.

        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        """
        setattr(self, "created_at", datetime.datetime.now(tz=datetime.timezone.utc))
        setattr(self, "updated_at", datetime.datetime.now(tz=datetime.timezone.utc))
        await super().save(*args, **kwargs)

    class Meta:
        abstract = True
