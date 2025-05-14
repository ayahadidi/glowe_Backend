from django.test import TestCase
from Backend.models import Colors
from Backend.models import PromoCode
class ColorTestCase(TestCase):
    fixtures=['color.json']
    def test_color_count(self):
        self.assertEqual(Colors.objects.count(),20)

class PromoCodeTestCase(TestCase):
    fixtures=['promoCode.json']
    def test_promoCode_count(self):
        self.assertEqual(PromoCode.objects.count(),20)
