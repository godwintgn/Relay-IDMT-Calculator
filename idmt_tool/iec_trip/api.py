import math
from .curves import IEC_CURVES
from .formulas import trip_time_from_currents

def compute_trip_time(curve_name: str, pickup: float, fault: float, tms: float) -> float:
    if curve_name not in IEC_CURVES:
        raise ValueError(f"Unknown curve: {curve_name}")
    curve = IEC_CURVES[curve_name]
    if fault <= pickup:
        return math.inf
    return trip_time_from_currents(curve, fault, pickup, tms)
