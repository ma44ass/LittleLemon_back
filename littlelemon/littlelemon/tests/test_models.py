
from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu.objects.create(
            title="IceCream",
            price=80,
            inventory=100
            )
        expected_str = "IceCream : 80"
        self.assertEqual(str(menu_item), expected_str)