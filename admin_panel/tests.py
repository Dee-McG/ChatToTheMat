from django.test import TestCase


class TestViews(TestCase):
    def test_admin_panel_redirect_when_not_logged_in(self):
        """ Test admin panel redirects when not logged in """
        response = self.client.get('/profiles/admin_panel/')
        self.assertEqual(response.status_code, 302)
