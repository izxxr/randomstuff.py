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
    """
    Represents the closed cases of a country COVID-19 data.
    
    Attributes
    ----------
    
    percentage: ClosedCasesPercentage
        The percentage of closed cases.
    
    total: str
        The total closed cases.
    """
    percentage: ClosedCasesPercentage = None
    total: str = None


@dataclass(frozen=True)
class CountryCovidData:
    """
    Represents the COVID-19 data of a country.
    
    This is generally returned when a country is specified in :meth:``get_covid_data`` method.
    
    Attributes
    ----------
    
    country: Country
        The country related to the data.

 
    cases: Cases
        The cases count.
    
    closed_cases: ClosedCases
        The closed cases count.
    """
    country: Country = None
    cases: Cases = None
    closed_cases: ClosedCases = None


