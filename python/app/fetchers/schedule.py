import fastf1 as ff1
import pandas as pd
from typing import List, Dict, Any


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
    schedule = get_schedule(2025, False)
    for event in schedule:
        print(f"Round {event['RoundNumber']}: {event['EventName']} - {event['Country']}")
        for session in event['sessions']:
            print(f"  {session['name']}: {session['date_utc']}")
