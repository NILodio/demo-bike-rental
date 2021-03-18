from sklearn.metrics import mean_absolute_error, make_scorer


def get_metric_name_mapping():
    return {_mae(): bike_number_error}


def get_metric_function(name: str, **params):
    mapping = get_metric_name_mapping()

    def fn(y, y_pred):
        return mapping[name](y, y_pred, **params)

    return fn



def bike_number_error(y_true, y_pred, understock_price=0.3, overstock_price=0.7):
  e = y_true - y_pred
  return sum(map(lambda err: overstock_price *err*(-1) if err < 0 else understock_price*err , e)) / len(e)


def get_scoring_function(name: str, **params):
    mapping = {
        _mae(): make_scorer(mean_absolute_error, greater_is_better=True, **params)
    }
    return mapping[name]


def _mae():
    return "bike number error"