import typing as t
import numpy as np
import pandas as pd


from datetime import timedelta
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


def build_estimator(hyperparams: t.Dict[str, t.Any]):
    estimator_mapping = get_estimator_mapping()
    steps = []
    for name, params in hyperparams.items():
        estimator = estimator_mapping[name](**params)
        steps.append((name, estimator))
    model = Pipeline(steps)
    return model


def get_estimator_mapping():
    return {
        "regressor": RandomForestRegressor,
        "BikeRentalFeatureExtractor": BikeRentalFeatureExtractor,
        "CustomColumnTransformer": CustomColumnTransformer,
    }


class BikeRentalFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def rolling_feactures(self):
        self.new_features['rolling_tem_3'] = self.new_features.temp.rolling(3 ,win_type = 'triang').mean()
        self.new_features['rolling_tem_4'] = self.new_features.temp.rolling(4 ,win_type = 'triang').mean()
        self.new_features['rolling_windspeed_3'] = self.new_features.temp.rolling(2 ,win_type = 'triang').mean()
        self.new_features['rolling_windspeed_4'] = self.new_features.temp.rolling(3 ,win_type = 'triang').mean()
        # self.new_features['cnt_7_day_before'] = self.new_features.cnt.rolling(7, win_type = 'triang').mean()
        self.new_features['registered_4_day_before'] = self.new_features.registered.rolling(4, win_type = 'triang').mean()
        self.new_features['registered_2_day_before'] = self.new_features.registered.rolling(2, win_type = 'triang').mean()


        self.new_features.temp.fillna(self.new_features.loc[self.new_features.index[0], 'temp'] , inplace = True)
        self.new_features.windspeed.fillna(self.new_features.loc[self.new_features.index[0], 'windspeed'] , inplace = True)


        # self.new_features.cnt_7_day_before.fillna(self.new_features.loc[self.new_features.index[0], 'cnt'] , inplace = True)
        self.new_features.registered_4_day_before.fillna(self.new_features.loc[self.new_features.index[0], 'registered'] , inplace = True)
        self.new_features.registered_2_day_before.fillna(self.new_features.loc[self.new_features.index[0], 'registered'] , inplace = True)
        self.new_features.rolling_tem_3.fillna(self.new_features.loc[self.new_features.index[0], 'temp'] , inplace = True)
        self.new_features.rolling_tem_4.fillna(self.new_features.loc[self.new_features.index[0], 'temp'] , inplace = True)
        self.new_features.rolling_windspeed_3.fillna(self.new_features.loc[self.new_features.index[0], 'windspeed'] , inplace = True)
        self.new_features.rolling_windspeed_4.fillna(self.new_features.loc[self.new_features.index[0], 'windspeed'] , inplace = True)


    def transform(self, X):
        self.new_features = X.copy()
        X = X.copy()
        self.rolling_feactures()
        # print(self.new_features.columns)
        return self.new_features


class CustomColumnTransformer(BaseEstimator, TransformerMixin):
    _categorical_columns = (
        "season,yr,mnth,hr,holiday,weekday,workingday,weathersit"
    ).split(",")


    _float_columns = (
        "temp,atemp,hum,windspeed,registered,rolling_tem_3,rolling_tem_4,rolling_windspeed_3,"
        + "rolling_windspeed_4,registered_4_day_before,registered_2_day_before"
    ).split(",")


    def __init__(self):
        self._column_transformer = ColumnTransformer(
            transformers=[
                (
                    "one_hot_encoder",
                    OneHotEncoder(handle_unknown="ignore", sparse=False),
                    type(self)._categorical_columns,
                ),
                ("scaler", StandardScaler(), type(self)._float_columns),
            ],
            remainder="drop",
        )   

    def fit(self, X, y=None):
        # print(list(X.columns))
        # print(self._float_columns)
        # print(self._categorical_columns)
        self._column_transformer = self._column_transformer.fit(X, y=y)
        return self

    def transform(self, X):
        return self._column_transformer.transform(X)


# class SimplifiedTransformer(BaseEstimator, TransformerMixin):
#     """This is just for easy of demonstration"""

#     _columns_to_keep = "HouseAge,GarageAge,LotArea,Neighborhood,HouseStyle".split(",")

#     def __init__(self):
#         self._column_transformer = ColumnTransformer(
#             transformers=[
#                 ("binarizer", OrdinalEncoder(handle_unknown="ignore"), ["Neighborhood", "HouseStyle"]),
                
#             ],
#             remainder="drop",
#         )

#     def fit(self, X, y=None):
#         columns = type(self)._columns_to_keep
#         X_ = X[columns]
#         self._column_transformer = self._column_transformer.fit(X_, y=y)
#         return self

#     def transform(self, X):
#         columns = type(self)._columns_to_keep
#         X_ = X[columns] 
#         X_ = self._column_transformer.transform(X_)
#         return X_
