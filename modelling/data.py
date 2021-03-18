import typing as t
import typing_extensions as te
import holidays
from datetime import date ,datetime
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from random import randint


Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [(4, (date(Y,  1,  1),  date(Y,  3, 20))),
        (1, (date(Y,  3, 21),  date(Y,  6, 20))),
        (2, (date(Y,  6, 21),  date(Y,  9, 22))),
        (3, (date(Y,  9, 23),  date(Y, 12, 20))),
        (4, (date(Y, 12, 21),  date(Y, 12, 31)))]


class DatasetReader(te.Protocol):
    def __call__(self) -> pd.DataFrame:
        ...


SplitName = te.Literal["train", "test"]


def get_dataset(reader: DatasetReader, splits: t.Iterable[SplitName]):
    df = reader()
    df = clean_dataset(df)
    Y = df["cnt"]
    X = df.drop(columns=["cnt" ,"casual"])
    index_T = df['yr'] == 0

    X_train, y_train = X[index_T] , Y[index_T]
    X_test, y_test = X[~index_T], Y[~index_T]

    split_mapping = {"train": (X_train, y_train), "test": (X_test, y_test)}

    assert X.shape[0] == X_train.shape[0] + X_test.shape[0]

    return {k: split_mapping[k] for k in splits}


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    us_holidays = holidays.UnitedStates()
    
    df['datetime'] =  pd.to_datetime(df['dteday']) + df['hr'].apply(pd.Timedelta, unit='h')
    df = df.set_index('datetime')
    df = df.reindex(pd.date_range(start=df.index[0] , end=df.index[-1] , freq='1H'))
    df.drop(columns=['dteday', 'instant'] , inplace = True)

    null_index = df[df.isna().any(axis = 1)].index

    for index in null_index:
        df.loc[index , ['hr' , 'yr' , 'mnth']] = (index.hour , int(index.year == 2012) , index.month)
        df.loc[index , ['holiday' , 'weekday' , 'workingday','season','weathersit']] = \
                            (int(index in us_holidays) , index.dayofweek , int(index.dayofweek in [0,1,2,3,4]) ,_get_season(index),randint(1,4))
    
    df['temp'].fillna(df['temp'].rolling(60,min_periods=1).mean(),inplace = True)
    df['atemp'].fillna(df['atemp'].rolling(60,min_periods=1).mean(),inplace = True)
    df['hum'].fillna(df['hum'].rolling(60,min_periods=1).mean(),inplace = True)
    df['windspeed'].fillna(df['windspeed'].rolling(60,min_periods=1).mean(),inplace = True)
    df['casual'].fillna(df['casual'].rolling(60,min_periods=1).mean(),inplace = True)
    df['registered'].fillna(df['registered'].rolling(60,min_periods=1).mean(),inplace = True)
    df['cnt'] = df['registered'] + df['casual']

    assert ((365 * 24 * 2) + 24) == df.shape[0]
    
    return df

def _get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)


