from enum import Enum


class SessionType(str, Enum):
    FP1 = "FP1"     # Free Practice 1
    FP2 = "FP2"     # Free Practice 2
    FP3 = "FP3"     # Free Practice 3
    Q = "Q"         # Qualifying
    S = "S"         # Sprint
    SS = "SS"       # Sprint Shootout
    SQ = "SQ"       # Qualifying Shootout
    R = "R"         # Race
