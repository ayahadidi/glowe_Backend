from django.test import TestCase
from Backend.models import Colors

class ColorTestCase(TestCase):
    fixtures=['color.json']
    def test_color_count(self):
        self.assertEqual(Colors.objects.count(),20)
