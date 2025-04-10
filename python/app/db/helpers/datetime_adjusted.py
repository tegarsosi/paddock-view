from typing import Any

from tortoise import fields


class DatetimeAdjustedField(fields.DatetimeField):
    """Datetime adjusted field.

    Ensure that the datetime is stored without timezone information
    (timezone-naive)
    """

    def to_db_value(self, value: Any, instance: Any) -> Any:
        """Convert the datetime value to a database datetime value.

        :param value: Datetime value.
        :param instance: Instance of the model.
        :return: Datetime value without timezone information.
        """
        if value:
            return value.replace(tzinfo=None)
        return value
