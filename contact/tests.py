from django.test import TestCase


class TestViews(TestCase):
    def test_contact_page(self):
        """ Test contact page template renders correct page """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'contact/contact.html')