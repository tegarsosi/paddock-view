import datetime
from typing import Any

import pandas as pd
from tortoise import fields


class DatetimeAdjustedField(fields.DatetimeField):
    """Datetime field that accepts Pandas Timestamps, ensures UTC
    and strips tzinfos.
    """

    def to_db_value(self, value: Any, instance: Any) -> Any:
        """Convert the datetime value to a database datetime value.

        :param value: Datetime value.
        :param instance: Instance of the model.
        :return: Datetime value without timezone information.
        """
        if value is None:
            return value

        if isinstance(value, pd.Timestamp):
            value = value.to_pydatetime()

        if value.tzinfo is None:
            value = value.replace(tzinfo=datetime.timezone.utc)

        return value.replace(tzinfo=None)
