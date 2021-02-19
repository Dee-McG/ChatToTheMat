from django.test import TestCase


class TestViews(TestCase):
    def test_private_messages_redirect_when_not_logged_in(self):
        """ Test private messages page redirects when not logged in """
        response = self.client.get('/private_messages/')
        self.assertEqual(response.status_code, 302)