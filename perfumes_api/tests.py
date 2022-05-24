from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Perfume

# Testing the model
class PerfumeTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testperfume = Perfume.objects.create(perfume_name = "test_perfume", perfume_description="Testing perfume")
        testperfume.save()


    def test_perfumes_model(self):
        perfume = Perfume.objects.get(id=1)
        actual_name = perfume.perfume_name
        self.assertEqual(actual_name, "test_perfume")