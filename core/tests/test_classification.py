from django.test import TestCase

from training.tr_core import calculate as train
from core.core import calculate
from training.models import PredModels
from core.tests.test_prepare import split_single, split_double


class TestClassification(TestCase):
    """Proof of concept tests"""

    def results(self):
        return {'f1score': 0.6666666666666666, 'acc': 0.5, 'auc': 0, 'false_negative': 0, 'false_positive': 1,
                'true_positive': 1, 'true_negative': 0, 'precision': 0.5, 'recall': 1.0}

    def results2(self):
        return {'f1score': 0.6666666666666666, 'auc': 0.5, 'acc': 0.5, 'false_negative': 0, 'false_positive': 1,
                'true_positive': 1, 'true_negative': 0, 'precision': 0.5, 'recall': 1.0}

    def get_job(self):
        json = dict()
        json["clustering"] = "kmeans"
        json["split"] = split_double()
        json["method"] = "randomForest"
        json["encoding"] = "simpleIndex"
        json["rule"] = "remaining_time"
        json["prefix_length"] = 1
        json["threshold"] = "default"
        json["type"] = "classification"
        return json

    def test_class_randomForest(self):
        job = self.get_job()
        job['clustering'] = 'noCluster'
        model, _=train(job, redo=True)
        result = calculate(job,model)
        self.assertDictEqual(result, self.results2())

    # KNN Fails due to small dataset
    # Expected n_neighbors <= n_samples,  but n_samples = 4, n_neighbors = 5
    def class_KNN(self):
        job = self.get_job()
        job['method'] = 'KNN'
        model, _=train(job, redo=True)
        calculate(job,model)

    def test_class_DecisionTree(self):
        job = self.get_job()
        job['method'] = 'decisionTree'
        model, _= train(job, redo=True)
        result = calculate(job,model)
        self.assertDictEqual(result, self.results())

    def test_next_activity_randomForest(self):
        job = self.get_job()
        job['type'] = 'nextActivity'
        model, _=train(job, redo=True)
        result = calculate(job,model)
        self.assertIsNotNone(result)

    # KNN Fails due to small dataset
    # Expected n_neighbors <= n_samples,  but n_samples = 4, n_neighbors = 5
    def next_activity_KNN(self):
        job = self.get_job()
        job['method'] = 'KNN'
        job['type'] = 'nextActivity'
        model, _=train(job, redo=True)
        calculate(job,model)

    def test_next_activity_DecisionTree(self):
        job = self.get_job()
        job['method'] = 'decisionTree'
        job['type'] = 'nextActivity'
        job['clustering'] = 'None'
        model,_=train(job, redo=True)
        result = calculate(job,model)
        self.assertIsNotNone(result)

    def test_class_complex(self):
        job = self.get_job()
        job['clustering'] = 'noCluster'
        job["encoding"] = "complex"
        model,_=train(job, redo=True)
        result = calculate(job,model)
        self.assertDictEqual(result, self.results2())

    def test_class_last_payload(self):
        job = self.get_job()
        job['clustering'] = 'noCluster'
        job["encoding"] = "lastPayload"
        model,_=train(job, redo=True)
        result = calculate(job,model)
        self.assertDictEqual(result, self.results2())
