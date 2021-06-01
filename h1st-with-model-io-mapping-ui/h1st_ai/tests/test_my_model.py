from django.test import TestCase

from h1st_ai.models import MyModel


class MyModelTestCase(TestCase):
    def test_model_output(self):
        model = MyModel()
        self.assertEqual(model.predict(0), 0)
