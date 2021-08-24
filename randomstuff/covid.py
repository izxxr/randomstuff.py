from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class CovidCondition:
    mild: str = None
    critical: str = None

@dataclass(frozen=True)
class GlobalCovidData:
    total_cases : str = None
    total_deaths : str = None
    total_recovered : str = None
    active_cases : str = None
    closed_cases : str = None
    condition: CovidCondition = None

@dataclass(frozen=True)
class Country:
    name: str = None
    flag_img: str = None

@dataclass(frozen=True)
class Cases:
    total: str = None
    recovered: str = None
    deaths: str = None

@dataclass(frozen=True)
class ClosedCasesPercentage:
    death: str = None
    discharge: str = None


@dataclass(frozen=True)
class ClosedCases:
    percentage: ClosedCasesPercentage = None
    total: str = None


@dataclass(frozen=True)
class CountryCovidData:
    country: Country = None
    cases: Cases = None
    closed_cases: ClosedCases = None


