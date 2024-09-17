from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.utils import timezone
from .models import ECommerce

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_customer_money(self):
        now = timezone.now()
        rich = ECommerce.objects.create(
            name = "20/21 Third Kit",
            time = now,
            description = "Manchester United Third Kit for the 20/21 Season",
            quantity = 10,
            size = "L",
            season = "23/24",
            type = "third",
        )
        self.assertFalse(rich.is_customer_rich)
