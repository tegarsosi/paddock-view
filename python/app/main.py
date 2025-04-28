from app.drivers import get_drivers_for_session
from app.enum.session_types import SessionType


def main(
    year: int,
    gp: str,
    session: SessionType
):
    drivers = get_drivers_for_session(year, gp, session)
    print(drivers)


if __name__ == "__main__":
    main(2024, "Monaco", SessionType.FP2)
