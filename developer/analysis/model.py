"""Functions for fitting the regression model."""

from statsmodels.iolib.smpickle import load_pickle
import statsmodels.api as sm

def fit_multi_logit_model(data):
    """Fit a logit model to data."""

    outcome_name = 'utility'
    explanatory_vars = [col for col in data.columns if "att" in col]

    X = data[explanatory_vars].astype(int)
    y = data[outcome_name].astype(int)

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    return model


def load_model(path):
    """Load statsmodels model.

    Args:
        path (str or pathlib.Path): Path to model file.

    Returns:
        statsmodels.base.model.Results: The stored model.

    """
    return load_pickle(path)
