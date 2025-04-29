import fastf1 as f1
from typing import List, Dict, Any

from app.enum.session_types import SessionType


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
        driver_dict = {
            "number": number,
            "abbreviation": driver_info["Abbreviation"],
            "full_name": driver_info["FullName"],
            "team_name": driver_info["TeamName"],
        }

        if session_type == SessionType.R and "Position" in driver_info:
            driver_dict["position"] = int(driver_info["Position"])

        drivers.append(driver_dict)

    return drivers
