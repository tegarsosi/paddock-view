import fastf1 as f1
from typing import List, Dict, Any

from python.enum.session_types import SessionType


def get_drivers_for_session(
        year: int,
        gp_name: str,
        session_type: SessionType
) -> List[Dict[str, Any]]:
    session = f1.get_session(year, gp_name, session_type)
    session.load()

    drivers = []
    for number in session.drivers:
        driver_info = session.get_driver(number)
        drivers.append({
            "position": int(driver_info["Position"]),
            "number": number,
            "abbreviation": driver_info["Abbreviation"],
            "full_name": driver_info["FullName"],
            "team_name": driver_info["TeamName"],
        })
    return drivers
