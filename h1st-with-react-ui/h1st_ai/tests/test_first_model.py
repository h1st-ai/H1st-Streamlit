from django.test import TestCase

from h1st_ai.models import FirstModel


class FirstModelTestCase(TestCase):
    def test_model_output(self):
        model = FirstModel()
        self.assertEqual(model.predict(0), 0)
