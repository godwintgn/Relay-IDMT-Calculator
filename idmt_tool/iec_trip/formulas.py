import math
from .curves import IECCurve

def trip_time_from_multiple(curve: IECCurve, multiple: float, tms: float) -> float:
    if multiple <= 1:
        return math.inf
    numerator = curve.k
    denominator = (multiple ** curve.alpha) - 1
    if denominator <= 0:
        return math.inf
    return tms * (numerator / denominator)

def trip_time_from_currents(curve: IECCurve, fault: float, pickup: float, tms: float) -> float:
    if pickup <= 0:
        raise ValueError("Pickup must be > 0")
    multiple = fault / pickup
    return trip_time_from_multiple(curve, multiple, tms)
