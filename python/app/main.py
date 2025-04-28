from python.app.drivers import get_drivers_for_session
from python.enum.session_types import SessionType


def main():
    drivers = get_drivers_for_session(2024, "Monza", SessionType.R)
    print(drivers)


if __name__ == "__main__":
    main()
