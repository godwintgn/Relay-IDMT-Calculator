from dataclasses import dataclass

@dataclass(frozen=True)
class IECCurve:
    name: str
    k: float
    alpha: float

IEC_CURVES = {
    "IEC Normal Inverse": IECCurve("IEC Normal Inverse", k=0.14, alpha=0.02),
    "IEC Very Inverse": IECCurve("IEC Very Inverse", k=13.5, alpha=1.0),
    "IEC Extremely Inverse": IECCurve("IEC Extremely Inverse", k=80.0, alpha=2.0),
    "IEC Long Time Inverse": IECCurve("IEC Long Time Inverse", k=120.0, alpha=1.0)
}
