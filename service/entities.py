import typing as t
import typing_extensions as te

from pydantic import BaseModel, Field, ConstrainedInt, PositiveInt, PositiveFloat


# class ModelInput(BaseModel):
#     YrSold: int
#     YearBuilt: int
#     YearRemodAdd: int
#     GarageYrBlt: int
#     LotArea: int
#     Neighborhood: str
#     HouseStyle: str


# NeighborhoodLiteral = te.Literal[
#     "Blmgtn",
#     "Blueste",
#     "BrDale",
#     "BrkSide",
#     "ClearCr",
#     "CollgCr",
#     "Crawfor",
#     "Edwards",
#     "Gilbert",
#     "IDOTRR",
#     "Meadow",
#     "Mitchel",
#     "Names",
#     "NoRidge",
#     "NPkVill",
#     "NridgHt",
#     "NWAmes",
#     "OldTwon",
#     "SWISU",
#     "Sawyer",
#     "SawyerW",
#     "Somerst",
#     "StoneBr",
#     "Timber",
#     "Veenker",
# ]
# HouseStyleLiteral = te.Literal[
#     "1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"
# ]


# class ModelInput(BaseModel):
#     YrSold: PositiveInt
#     YearBuilt: PositiveInt
#     YearRemodAdd: PositiveInt
#     GarageYrBlt: PositiveInt
#     LotArea: PositiveFloat
#     Neighborhood: NeighborhoodLiteral
#     HouseStyle: HouseStyleLiteral

Holiday_Literal = te.Literal[0 , 1]
Week_Literal = te.Literal[0 , 1 ,2 , 3 , 4 , 5 , 6]
WorkingDay_Literal = te.Literal[0 , 1 ]
Weathersit_Literal = te.Literal[1 ,2 , 3 , 4]
mnth_Literal = te.Literal[1 , 2 , 3 , 4 , 5 , 6 , 7 ,8 ,9 ,10 ,11 ,12]

class SeasonInteger(ConstrainedInt):
    ge = 1
    le = 4

class HourInteger(ConstrainedInt):
    ge = 0
    le = 23


class ModelInput(BaseModel):
    season: SeasonInteger
    yr: int
    mnth : mnth_Literal
    hr: HourInteger
    holiday: Holiday_Literal
    weekday: Week_Literal
    workingday: WorkingDay_Literal
    weathersit: Weathersit_Literal
    temp : float
    atemp : float
    hum : float
    windspeed : float
    registered: int 