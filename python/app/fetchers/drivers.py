import fastf1 as ff1
from python.app.enums.grand_prix import GrandPrix
from python.app.enums.session_type import SessionType
from typing import List, Dict, Any


def get_driver_for_session(
        year: int,
        gp: GrandPrix,
        session_type: SessionType,
) -> List[Dict[str, Any]]:
    """ Get the drivers for a given session.

    :param year: The year of the session.
    :param gp: The grand prix of the session.
    :param session_type: The type of session.
    :return: A list of dictionaries containing the drivers for the given session.
    """
    session = ff1.get_session(year, gp, session_type)
    session.load()

    drivers = []

    for number in session.drivers:
        driver_info = session.get_driver(number)
        driver_dict = {
            'number': number,
            'abbreviation': driver_info['Abbreviation'],
            'name': driver_info['FirstName'] + ' ' + driver_info['LastName'],
            'team': driver_info['TeamName'],
        }

        if session_type == SessionType.R:
            driver_dict['status'] = driver_info['Status']

        drivers.append(driver_dict)

    return drivers


if __name__ == "__main__":
    drivers = get_driver_for_session(2025, GrandPrix.JAPAN, SessionType.R)
    for i in range(len(drivers)):
        print(f"P{i + 1} {drivers[i]['number']} - {drivers[i]['name']} - {drivers[i]['team']} - {drivers[i]['status']}")
