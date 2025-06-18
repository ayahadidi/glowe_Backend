from django.test import TestCase
from Backend.Models import Colors
from Backend.Models import PromoCode
from Backend.Models import UserPromoCode
class ColorTestCase(TestCase):
    fixtures=['color.json']
    def test_color_count(self):
        self.assertEqual(Colors.objects.count(),20)

class PromoCodeTestCase(TestCase):
    fixtures=['promoCode.json']
    def test_promoCode_count(self):
        self.assertEqual(PromoCode.objects.count(),20)

class UserPromoCodeTestCase(TestCase):
    fixtures=['user_promoCode_fixture.json']
    def test_promoCode_count(self):
        self.assertEqual(UserPromoCode.objects.count(),20)

