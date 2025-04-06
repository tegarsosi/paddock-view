from enum import Enum


class SessionType(str, Enum):
    FP1 = "Practice 1"
    FP2 = "Practice 2"
    FP3 = "Practice 3"
    Q = "Qualifying"
    R = "Race"
    S = "Sprint"
    SQ = "Sprint Qualifying"
    SS = "Sprint Shootout"
