from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    def test_checkout_page_redirects_when_logged_out(self):
        """ Test checkout redirects when user is logged out """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)