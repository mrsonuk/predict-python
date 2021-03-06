"""Common methods for all training methods"""

import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from core.constants import KNN, RANDOM_FOREST, DECISION_TREE, XGBOOST


def calculate_results(prediction, actual):
    true_positive = 0
    false_positive = 0
    false_negative = 0
    true_negative = 0

    for i in range(0, len(actual)):
        if actual[i]:
            if actual[i] == prediction[i]:
                true_positive += 1
            else:
                false_positive += 1
        else:
            if actual[i] == prediction[i]:
                true_negative += 1
            else:
                false_negative += 1
    try:
        precision = float(true_positive) / (true_positive + false_positive)
    except ZeroDivisionError:
        precision = 0

    try:
        recall = float(true_positive) / (true_positive + false_negative)
    except ZeroDivisionError:
        recall = 0

    try:
        f1score = (2 * precision * recall) / (precision + recall)
    except ZeroDivisionError:
        f1score = 0

    acc = float(true_positive + true_negative) / (true_positive + true_negative + false_negative + false_positive)
    row = {'f1score': f1score, 'acc': acc, 'true_positive': true_positive, 'true_negative': true_negative,
           'false_negative': false_negative, 'false_positive': false_positive, 'precision': precision, 'recall': recall}
    return row


def choose_classifier(job: dict):
    method, config = get_method_config(job)
    print("Using method {} with config {}".format(method, config))
    if method == KNN:
        clf = KNeighborsClassifier(**config)
    elif method == RANDOM_FOREST:
        clf = RandomForestClassifier(**config)
    elif method == DECISION_TREE:
        clf = DecisionTreeClassifier(**config)
    elif method == XGBOOST:
        clf = xgb.XGBClassifier(**config)
    else:
        raise ValueError("Unexpected classification method {}".format(method))
    return clf


def get_method_config(job: dict):
    method = job['method']
    method_conf_name = "{}.{}".format(job['type'], method)
    config = job[method_conf_name]
    return method, config


def add_actual(training_df, test_df):
    training_df['actual'] = training_df['label']
    test_df['actual'] = test_df['label']
    return training_df, test_df
