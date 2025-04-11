import asyncio
import fastf1 as ff1
import pandas as pd
from typing import List, Dict, Any

from app.db.db import init_db, close_db
from app.db.models.grand_prix import GrandPrix
from app.db.models.session_types import SessionType
from app.db.models.sessions import Session
from app.enums.session_type import SessionType as SessionTypeEnum

SESSION_TYPE_NAME_TO_CODE = {v.value: v.name for v in SessionTypeEnum}


async def store_schedule_in_db(year: int, include_testing: bool) -> None:
    """ Store the schedule in the database.

    :param year: The year to store the schedule for.
    :param include_testing: Whether to include testing events in the schedule.
    """
    await init_db()
    schedule = get_schedule(year, include_testing)

    for event in schedule:
        gp, _ = await GrandPrix.get_or_create(
            round=event["RoundNumber"],
            event_name=event["EventName"],
            location=event["Location"],
            country=event["Country"],
            year=year,
        )

        for session in event["sessions"]:
            name = session["name"]
            code = SESSION_TYPE_NAME_TO_CODE.get(name)
            session_type, _ = await SessionType.get_or_create(
                name=name,
                code=code,
            )
            await Session.get_or_create(
                grand_prix=gp,
                session_type=session_type,
                date_utc=session["date_utc"],
            )
    await close_db()


def get_schedule(year: int, include_testing: bool) -> List[Dict[str, Any]]:
    """ Get the schedule for a given year and include testing events.

    :param year: The year to get the schedule for.
    :param include_testing: Whether to include testing events in the schedule.
    :return: A list of dictionaries containing the schedule for the given year.
    """
    schedule = ff1.get_event_schedule(year, include_testing=include_testing)
    events_with_sessions = []

    for _, event in schedule.iterrows():
        event_dict = event.to_dict()
        sessions = []

        for i in range(1, 6):
            session_name = event_dict[f"Session{i}"]
            session_date_utc = event_dict[f"Session{i}DateUtc"]

            if pd.notna(session_name):
                session_info = {
                    "name": session_name,
                    "date_utc": session_date_utc,
                }

                sessions.append(session_info)

        event_dict["sessions"] = sessions
        events_with_sessions.append(event_dict)

    return events_with_sessions


if __name__ == "__main__":
    asyncio.run(store_schedule_in_db(2025, False))
    # schedule = get_schedule(2025, False)
    # for event in schedule:
    #     print(f"Round {event['RoundNumber']}: {event['EventName']} - {event['Country']}")
    #     for session in event['sessions']:
    #         print(f"  {session['name']}: {session['date_utc']}")
