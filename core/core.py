from core.classification import classifier
from core.constants import NEXT_ACTIVITY, \
    CLASSIFICATION, REGRESSION
from core.next_activity import next_activity
from core.regression import regression
from encoders.common import encode_logs
from logs.splitting import prepare_logs


def calculate(job):
    """ Main entry method for calculations"""
    print("Start job {} with {}".format(job['type'], get_run(job)))
    training_log, test_log = prepare_logs(job['split'])

    # Python dicts are bad
    if 'prefix_length' in job:
        prefix_length = job['prefix_length']
    else:
        prefix_length = 1
    zero_padding = True if 'zero_padding' in job else False

    training_df, test_df = encode_logs(training_log, test_log, job['encoding'], job['type'],
                                       prefix_length=prefix_length, zero_padding=zero_padding)

    if job['type'] == CLASSIFICATION:
        results = classifier(training_df, test_df, job)
    elif job['type'] == REGRESSION:
        results = regression(training_df, test_df, job)
    elif job['type'] == NEXT_ACTIVITY:
        results = next_activity(training_df, test_df, job)
    else:
        raise ValueError("Type not supported", job['type'])
    print("End job {}, {} . Results {}".format(job['type'], get_run(job), results))
    return results


def get_run(job):
    """Defines job identity"""
    if job['type'] == CLASSIFICATION:
        return run_identity(job['method'], job['encoding'], job['clustering'])
    elif job['type'] == NEXT_ACTIVITY:
        return run_identity(job['method'], job['encoding'], job['clustering'])
    elif job['type'] == REGRESSION:
        return run_identity(job['method'], job['encoding'], job['clustering'])


def run_identity(method, encoding, clustering):
    return method + '_' + encoding + '_' + clustering
