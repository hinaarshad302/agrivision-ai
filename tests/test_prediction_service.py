"""Safety tests for AgriVision AI disease prediction service.

Run with: python -m unittest discover -s tests -v
"""

import unittest
from unittest.mock import patch

import numpy as np

from services import prediction_service as service


class FakeModel:
    def __init__(self, probabilities):
        self.probabilities = np.asarray([probabilities], dtype=np.float64)

    def predict(self, image, verbose=0):
        return self.probabilities


class CropNameTests(unittest.TestCase):
    def test_supported_local_crop_aliases(self):
        self.assertEqual(service.normalize_crop_name("Tamatar"), "Tomato")
        self.assertEqual(service.normalize_crop_name("Aloo"), "Potato")
        self.assertEqual(service.normalize_crop_name("Makai"), "Corn")
        self.assertEqual(service.normalize_crop_name("Seb"), "Apple")

    def test_unsupported_crop_is_not_normalized(self):
        self.assertIsNone(service.normalize_crop_name("Wheat"))
        self.assertIsNone(service.normalize_crop_name("Rice"))


class PredictionSafetyTests(unittest.TestCase):
    def setUp(self):
        self.labels = [
            "Apple___Apple_scab",
            "Corn___Common_rust",
            "Potato___Early_blight",
            "Tomato___Early_blight",
            "Tomato___Late_blight",
            "Tomato___healthy",
        ]

    @patch.object(service, "load_model")
    def test_unsupported_crop_does_not_load_or_run_model(self, load_model):
        result = service.predict_disease(object(), expected_crop="Wheat")

        self.assertEqual(result["status"], "unsupported")
        load_model.assert_not_called()

    @patch.object(service, "preprocess_image", return_value=np.zeros((1, 224, 224, 3)))
    @patch.object(service, "load_temperature", return_value=1.0)
    @patch.object(service, "load_class_labels")
    @patch.object(service, "load_model")
    def test_crop_mismatch_blocks_disease_result(
        self, load_model, load_labels, load_temperature, preprocess
    ):
        load_model.return_value = FakeModel([0.80, 0.05, 0.05, 0.04, 0.03, 0.03])
        load_labels.return_value = self.labels

        result = service.predict_disease(object(), expected_crop="Tomato")

        self.assertEqual(result["status"], "mismatch")
        self.assertNotIn("disease", result)

    @patch.object(service, "preprocess_image", return_value=np.zeros((1, 224, 224, 3)))
    @patch.object(service, "load_temperature", return_value=1.0)
    @patch.object(service, "load_class_labels")
    @patch.object(service, "load_model")
    def test_success_returns_only_same_crop_alternatives(
        self, load_model, load_labels, load_temperature, preprocess
    ):
        load_model.return_value = FakeModel([0.02, 0.02, 0.02, 0.55, 0.25, 0.14])
        load_labels.return_value = self.labels

        result = service.predict_disease(object(), expected_crop="Tamatar")

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["crop"], "Tomato")
        self.assertEqual(len(result["top_predictions"]), 3)
        self.assertTrue(
            all(item["crop"] == "Tomato" for item in result["top_predictions"])
        )


if __name__ == "__main__":
    unittest.main()
